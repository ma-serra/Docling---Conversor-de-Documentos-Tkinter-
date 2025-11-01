"""
Conversor de Documentos para Planilha
Extrai dados estruturados de documentos e converte para Excel/CSV
"""

import pandas as pd
from typing import List, Dict, Any
from pathlib import Path
import re
from bs4 import BeautifulSoup


class DocumentToSpreadsheetConverter:
    """Converte documentos em planilhas (Excel/CSV)"""

    def __init__(self):
        self.data = []
        self.columns = []
        self.tables_found = []

    def extract_data_from_document(self, file_path: str) -> Dict[str, Any]:
        """
        Extrai dados estruturados de documento para conversão em planilha

        Returns:
            Dict com dados extraídos e metadados
        """
        file_ext = Path(file_path).suffix.lower()

        if file_ext == '.html':
            return self.extract_from_html(file_path)
        elif file_ext in ['.pdf', '.docx']:
            return self.extract_with_docling(file_path)
        else:
            return self.extract_from_text(file_path)

    def extract_from_html(self, file_path: str) -> Dict[str, Any]:
        """Extrai dados de HTML (tabelas e campos)"""
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        result = {
            'tables': [],
            'fields': [],
            'metadata': {}
        }

        # Extrair tabelas HTML
        tables = soup.find_all('table')
        for i, table in enumerate(tables):
            table_data = self._parse_html_table(table)
            if table_data:
                result['tables'].append({
                    'id': f'table_{i}',
                    'data': table_data['data'],
                    'columns': table_data['columns']
                })

        # Extrair campos data-field
        fields_data = []
        for element in soup.find_all(attrs={"data-field": True}):
            field_name = element.get('data-field')
            field_value = element.get_text(strip=True)

            fields_data.append({
                'field': field_name,
                'value': field_value
            })

        if fields_data:
            result['fields'] = fields_data

        # Se não tem tabelas, criar tabela de campos
        if not result['tables'] and fields_data:
            result['tables'].append({
                'id': 'campos_extraidos',
                'data': fields_data,
                'columns': ['field', 'value']
            })

        return result

    def _parse_html_table(self, table) -> Dict[str, Any]:
        """Parse tabela HTML para dados estruturados"""
        rows = table.find_all('tr')
        if not rows:
            return None

        data = []
        columns = []

        # Primeira linha pode ser cabeçalho
        first_row = rows[0]
        headers = first_row.find_all(['th', 'td'])

        # Detectar se primeira linha é cabeçalho
        is_header = bool(first_row.find_all('th'))

        if is_header:
            columns = [h.get_text(strip=True) for h in headers]
            data_rows = rows[1:]
        else:
            # Gerar colunas automáticas
            num_cols = len(headers)
            columns = [f'Coluna_{i+1}' for i in range(num_cols)]
            data_rows = rows

        # Extrair dados
        for row in data_rows:
            cells = row.find_all(['td', 'th'])
            if cells:
                row_data = {}
                for i, cell in enumerate(cells):
                    if i < len(columns):
                        row_data[columns[i]] = cell.get_text(strip=True)
                data.append(row_data)

        return {
            'columns': columns,
            'data': data
        }

    def extract_with_docling(self, file_path: str) -> Dict[str, Any]:
        """Extrai dados usando Docling"""
        try:
            from docling.document_converter import DocumentConverter

            converter = DocumentConverter()
            result = converter.convert(file_path)

            # Exportar para markdown
            markdown = result.document.export_to_markdown()

            # Analisar markdown para extrair dados tabulares
            return self.extract_from_markdown(markdown)

        except ImportError:
            return {'error': 'Docling não instalado', 'tables': [], 'fields': []}
        except Exception as e:
            return {'error': str(e), 'tables': [], 'fields': []}

    def extract_from_markdown(self, markdown_text: str) -> Dict[str, Any]:
        """Extrai dados estruturados de Markdown"""
        lines = markdown_text.split('\n')

        result = {
            'tables': [],
            'fields': [],
            'sections': []
        }

        current_section = None
        section_data = []

        for i, line in enumerate(lines):
            stripped = line.strip()

            if not stripped:
                continue

            # Headers = nova seção
            if stripped.startswith('#'):
                # Salvar seção anterior
                if current_section and section_data:
                    result['sections'].append({
                        'title': current_section,
                        'data': section_data
                    })

                level = len(stripped) - len(stripped.lstrip('#'))
                current_section = stripped.lstrip('#').strip()
                section_data = []

            # Itens de lista ou dados estruturados
            elif ':' in stripped:
                # Formato "Campo: Valor"
                parts = stripped.split(':', 1)
                if len(parts) == 2:
                    field = parts[0].strip().lstrip('-*•')
                    value = parts[1].strip()

                    section_data.append({
                        'field': field,
                        'value': value
                    })

        # Salvar última seção
        if current_section and section_data:
            result['sections'].append({
                'title': current_section,
                'data': section_data
            })

        # Converter seções em tabelas
        for section in result['sections']:
            if section['data']:
                result['tables'].append({
                    'id': section['title'],
                    'data': section['data'],
                    'columns': ['field', 'value']
                })

        return result

    def extract_from_text(self, file_path: str) -> Dict[str, Any]:
        """Extrai dados de arquivo texto"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        return self.extract_from_markdown(content)

    def convert_to_dataframe(self, extracted_data: Dict[str, Any]) -> List[pd.DataFrame]:
        """Converte dados extraídos para DataFrames"""
        dataframes = []

        tables = extracted_data.get('tables', [])

        for table in tables:
            try:
                df = pd.DataFrame(table['data'])

                # Adicionar nome da tabela como atributo
                df.name = table.get('id', 'Tabela')

                dataframes.append(df)

            except Exception as e:
                print(f"Erro ao converter tabela {table.get('id')}: {e}")
                continue

        return dataframes

    def export_to_excel(self, dataframes: List[pd.DataFrame], output_path: str):
        """Exporta DataFrames para Excel"""
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            for i, df in enumerate(dataframes):
                # Nome da aba (limitado a 31 caracteres)
                sheet_name = getattr(df, 'name', f'Tabela_{i+1}')
                sheet_name = sheet_name[:31]

                df.to_excel(writer, sheet_name=sheet_name, index=False)

        return output_path

    def export_to_csv(self, dataframes: List[pd.DataFrame], output_dir: str):
        """Exporta DataFrames para CSV (um arquivo por tabela)"""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        files_created = []

        for i, df in enumerate(dataframes):
            name = getattr(df, 'name', f'tabela_{i+1}')
            # Sanitizar nome do arquivo
            name = re.sub(r'[^\w\s-]', '', name).strip().replace(' ', '_')

            csv_path = output_path / f"{name}.csv"
            df.to_csv(csv_path, index=False, encoding='utf-8-sig')

            files_created.append(str(csv_path))

        return files_created

    def auto_detect_structure(self, file_path: str) -> Dict[str, Any]:
        """
        Detecta automaticamente a melhor forma de estruturar dados em planilha

        Returns:
            Sugestões de como organizar os dados
        """
        extracted = self.extract_data_from_document(file_path)

        suggestions = {
            'recommended_format': 'unknown',
            'tables_count': len(extracted.get('tables', [])),
            'fields_count': len(extracted.get('fields', [])),
            'export_options': []
        }

        tables_count = len(extracted.get('tables', []))

        if tables_count > 1:
            suggestions['recommended_format'] = 'excel_multi_sheet'
            suggestions['export_options'] = [
                'Excel com múltiplas abas',
                'Múltiplos arquivos CSV',
                'CSV único combinado'
            ]

        elif tables_count == 1:
            suggestions['recommended_format'] = 'csv_single'
            suggestions['export_options'] = [
                'Arquivo CSV único',
                'Excel com uma aba'
            ]

        else:
            suggestions['recommended_format'] = 'fields_to_rows'
            suggestions['export_options'] = [
                'Campo-Valor em CSV',
                'Transpor para colunas'
            ]

        return suggestions


if __name__ == "__main__":
    # Teste
    converter = DocumentToSpreadsheetConverter()

    print("=== Testando Conversor de Documentos para Planilha ===\n")

    test_file = "templates/confissao_divida.html"
    if Path(test_file).exists():
        print(f"Analisando: {test_file}\n")

        # Extrair dados
        extracted = converter.extract_data_from_document(test_file)

        print(f"Tabelas encontradas: {len(extracted.get('tables', []))}")
        print(f"Campos encontrados: {len(extracted.get('fields', []))}")

        # Converter para DataFrames
        dfs = converter.convert_to_dataframe(extracted)

        print(f"\nDataFrames criados: {len(dfs)}")

        for i, df in enumerate(dfs):
            print(f"\nTabela {i+1}: {getattr(df, 'name', 'Sem nome')}")
            print(f"  Linhas: {len(df)}")
            print(f"  Colunas: {len(df.columns)}")
            print(f"  Preview:")
            print(df.head().to_string(index=False))

        # Exportar
        if dfs:
            excel_file = "output_examples/documento_convertido.xlsx"
            converter.export_to_excel(dfs, excel_file)
            print(f"\n✓ Exportado para Excel: {excel_file}")

            csv_files = converter.export_to_csv(dfs, "output_examples/csv")
            print(f"✓ Exportado para CSV: {len(csv_files)} arquivos")

    else:
        print(f"Arquivo de teste não encontrado: {test_file}")
