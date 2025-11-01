"""
Document Analyzer - Análise e Extração de Formatação de Documentos
Extrai estrutura, layout e formatação de documentos para clonagem
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from bs4 import BeautifulSoup


class DocumentAnalyzer:
    """Analisa documentos e extrai estrutura e formatação"""

    def __init__(self):
        self.document_structure = {}
        self.formatting_rules = {}
        self.layout_elements = []

    def analyze_document(self, file_path: str) -> Dict[str, Any]:
        """
        Analisa documento e extrai toda informação de estrutura e formatação

        Args:
            file_path: Caminho para o documento

        Returns:
            Dicionário com estrutura completa do documento
        """
        file_ext = Path(file_path).suffix.lower()

        if file_ext == '.html':
            return self.analyze_html(file_path)
        elif file_ext in ['.pdf', '.docx']:
            return self.analyze_with_docling(file_path)
        else:
            return self.analyze_text(file_path)

    def analyze_html(self, file_path: str) -> Dict[str, Any]:
        """Analisa documento HTML e extrai estrutura"""
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        # Extrair estrutura
        structure = {
            'title': self._extract_title(soup),
            'sections': self._extract_sections(soup),
            'styles': self._extract_styles(soup),
            'layout': self._extract_layout(soup),
            'elements': self._extract_elements(soup)
        }

        return structure

    def _extract_title(self, soup: BeautifulSoup) -> str:
        """Extrai título do documento"""
        title_tag = soup.find('title')
        if title_tag:
            return title_tag.text.strip()

        h1 = soup.find('h1')
        if h1:
            return h1.text.strip()

        return "Documento"

    def _extract_sections(self, soup: BeautifulSoup) -> List[Dict[str, Any]]:
        """Extrai seções do documento"""
        sections = []

        # Procurar por divs com classes específicas ou headings
        for i, section in enumerate(soup.find_all(['div', 'section', 'article'])):
            section_data = {
                'id': i,
                'type': section.name,
                'class': section.get('class', []),
                'content': section.get_text(strip=True)[:100],  # Preview
                'subsections': []
            }

            # Procurar headings dentro da seção
            headings = section.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            if headings:
                section_data['title'] = headings[0].get_text(strip=True)

            sections.append(section_data)

        return sections

    def _extract_styles(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """Extrai estilos CSS do documento"""
        styles = {
            'inline': {},
            'classes': {},
            'fonts': set(),
            'colors': set()
        }

        # Extrair estilos inline
        for element in soup.find_all(style=True):
            tag = element.name
            style_str = element.get('style', '')

            if tag not in styles['inline']:
                styles['inline'][tag] = []

            styles['inline'][tag].append(self._parse_style_string(style_str))

        # Extrair fontes e cores
        for element in soup.find_all(style=True):
            style_dict = self._parse_style_string(element.get('style', ''))

            if 'font-family' in style_dict:
                styles['fonts'].add(style_dict['font-family'])

            if 'color' in style_dict:
                styles['colors'].add(style_dict['color'])

            if 'background-color' in style_dict:
                styles['colors'].add(style_dict['background-color'])

        # Converter sets para listas
        styles['fonts'] = list(styles['fonts'])
        styles['colors'] = list(styles['colors'])

        return styles

    def _parse_style_string(self, style_str: str) -> Dict[str, str]:
        """Converte string de estilo CSS em dicionário"""
        style_dict = {}

        for declaration in style_str.split(';'):
            if ':' in declaration:
                prop, value = declaration.split(':', 1)
                style_dict[prop.strip()] = value.strip()

        return style_dict

    def _extract_layout(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """Extrai informações de layout do documento"""
        layout = {
            'type': 'unknown',
            'columns': 1,
            'grid': False,
            'flexbox': False
        }

        # Detectar layout por classes comuns
        body = soup.find('body') or soup

        # Procurar por grid
        if body.find(class_=re.compile(r'grid|container')):
            layout['grid'] = True

        # Procurar por colunas
        columns = body.find_all(class_=re.compile(r'col|column'))
        if columns:
            layout['columns'] = len(columns)

        return layout

    def _extract_elements(self, soup: BeautifulSoup) -> List[Dict[str, Any]]:
        """Extrai elementos individuais do documento"""
        elements = []

        # Headers
        for i, header in enumerate(soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])):
            elements.append({
                'id': f'header_{i}',
                'type': 'header',
                'level': int(header.name[1]),
                'text': header.get_text(strip=True),
                'style': self._get_element_style(header)
            })

        # Parágrafos
        for i, para in enumerate(soup.find_all('p')):
            text = para.get_text(strip=True)
            if text:  # Ignorar parágrafos vazios
                elements.append({
                    'id': f'paragraph_{i}',
                    'type': 'paragraph',
                    'text': text,
                    'style': self._get_element_style(para)
                })

        # Tabelas
        for i, table in enumerate(soup.find_all('table')):
            elements.append({
                'id': f'table_{i}',
                'type': 'table',
                'rows': len(table.find_all('tr')),
                'columns': len(table.find('tr').find_all(['td', 'th'])) if table.find('tr') else 0,
                'style': self._get_element_style(table)
            })

        # Listas
        for i, lst in enumerate(soup.find_all(['ul', 'ol'])):
            elements.append({
                'id': f'list_{i}',
                'type': 'list',
                'ordered': lst.name == 'ol',
                'items': len(lst.find_all('li')),
                'style': self._get_element_style(lst)
            })

        return elements

    def _get_element_style(self, element) -> Dict[str, str]:
        """Extrai estilo de um elemento específico"""
        style = {}

        # Estilo inline
        if element.get('style'):
            style.update(self._parse_style_string(element.get('style')))

        # Classes
        classes = element.get('class', [])
        if classes:
            style['classes'] = ' '.join(classes)

        return style

    def analyze_with_docling(self, file_path: str) -> Dict[str, Any]:
        """Analisa documento usando Docling"""
        try:
            from docling.document_converter import DocumentConverter

            converter = DocumentConverter()
            result = converter.convert(file_path)

            # Exportar para markdown para análise
            markdown = result.document.export_to_markdown()

            # Analisar markdown
            structure = self.analyze_markdown(markdown)
            structure['source'] = 'docling'
            structure['file_path'] = file_path

            return structure

        except ImportError:
            return {'error': 'Docling não instalado'}
        except Exception as e:
            return {'error': str(e)}

    def analyze_markdown(self, markdown_text: str) -> Dict[str, Any]:
        """Analisa texto markdown e extrai estrutura"""
        lines = markdown_text.split('\n')

        structure = {
            'title': '',
            'sections': [],
            'elements': []
        }

        current_section = None
        element_id = 0

        for line in lines:
            stripped = line.strip()

            if not stripped:
                continue

            # Headers
            if stripped.startswith('#'):
                level = len(stripped) - len(stripped.lstrip('#'))
                text = stripped.lstrip('#').strip()

                if level == 1 and not structure['title']:
                    structure['title'] = text

                element = {
                    'id': f'header_{element_id}',
                    'type': 'header',
                    'level': level,
                    'text': text
                }
                structure['elements'].append(element)

                # Nova seção
                if level <= 2:
                    current_section = {
                        'title': text,
                        'level': level,
                        'elements': []
                    }
                    structure['sections'].append(current_section)

                element_id += 1

            # Listas
            elif stripped.startswith(('- ', '* ', '+ ')) or re.match(r'^\d+\.', stripped):
                element = {
                    'id': f'list_item_{element_id}',
                    'type': 'list_item',
                    'text': re.sub(r'^[-*+\d.]\s*', '', stripped)
                }
                structure['elements'].append(element)
                element_id += 1

            # Parágrafos
            else:
                element = {
                    'id': f'paragraph_{element_id}',
                    'type': 'paragraph',
                    'text': stripped
                }
                structure['elements'].append(element)
                element_id += 1

        return structure

    def analyze_text(self, file_path: str) -> Dict[str, Any]:
        """Analisa arquivo de texto simples"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        return self.analyze_markdown(content)

    def create_template_from_analysis(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Cria template baseado na análise do documento"""
        template = {
            'name': analysis.get('title', 'Template'),
            'structure': [],
            'styles': analysis.get('styles', {}),
            'layout': analysis.get('layout', {}),
            'fields': []
        }

        # Converter elementos em campos editáveis
        for element in analysis.get('elements', []):
            field = {
                'id': element['id'],
                'type': element['type'],
                'label': self._generate_field_label(element),
                'default': element.get('text', ''),
                'style': element.get('style', {})
            }
            template['fields'].append(field)

        return template

    def _generate_field_label(self, element: Dict[str, Any]) -> str:
        """Gera label para campo baseado no elemento"""
        elem_type = element['type']

        if elem_type == 'header':
            return f"Título Nível {element.get('level', 1)}"
        elif elem_type == 'paragraph':
            preview = element.get('text', '')[:30]
            return f"Parágrafo: {preview}..."
        elif elem_type == 'table':
            return f"Tabela {element.get('rows', 0)}x{element.get('columns', 0)}"
        elif elem_type == 'list_item':
            return f"Item de Lista"
        else:
            return elem_type.title()

    def export_template(self, template: Dict[str, Any], output_path: str):
        """Exporta template para arquivo JSON"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(template, f, indent=4, ensure_ascii=False)

    def load_template(self, template_path: str) -> Dict[str, Any]:
        """Carrega template de arquivo JSON"""
        with open(template_path, 'r', encoding='utf-8') as f:
            return json.load(f)


if __name__ == "__main__":
    # Teste
    analyzer = DocumentAnalyzer()

    print("=== Testando Document Analyzer ===\n")

    # Testar com template existente
    test_file = "templates/confissao_divida.html"
    if Path(test_file).exists():
        print(f"Analisando: {test_file}\n")
        analysis = analyzer.analyze_document(test_file)

        print(f"Título: {analysis.get('title', 'N/A')}")
        print(f"Seções: {len(analysis.get('sections', []))}")
        print(f"Elementos: {len(analysis.get('elements', []))}")
        print(f"Fontes detectadas: {analysis.get('styles', {}).get('fonts', [])}")
        print(f"Cores detectadas: {analysis.get('styles', {}).get('colors', [])}")

        # Criar template
        template = analyzer.create_template_from_analysis(analysis)
        print(f"\nTemplate criado com {len(template['fields'])} campos")

        # Salvar template
        output = "templates/confissao_divida_template.json"
        analyzer.export_template(template, output)
        print(f"Template salvo em: {output}")
    else:
        print(f"Arquivo de teste não encontrado: {test_file}")
