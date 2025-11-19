#!/usr/bin/env python3
"""
Conversor Simples - Demonstração
Converte documentos básicos (TXT, MD, HTML) para Markdown e JSON
Versão simplificada que funciona sem dependências pesadas
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser


class HTMLToText(HTMLParser):
    """Extrai texto de HTML"""

    def __init__(self):
        super().__init__()
        self.text = []
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag[1])
            self.text.append('\n' + '#' * level + ' ')
        elif tag == 'p':
            self.text.append('\n\n')
        elif tag == 'br':
            self.text.append('\n')
        elif tag == 'li':
            self.text.append('\n- ')
        elif tag == 'strong' or tag == 'b':
            self.text.append('**')
        elif tag == 'em' or tag == 'i':
            self.text.append('*')
        elif tag == 'code':
            self.text.append('`')

    def handle_endtag(self, tag):
        if tag == 'strong' or tag == 'b':
            self.text.append('**')
        elif tag == 'em' or tag == 'i':
            self.text.append('*')
        elif tag == 'code':
            self.text.append('`')
        self.current_tag = None

    def handle_data(self, data):
        self.text.append(data)

    def get_text(self):
        return ''.join(self.text).strip()


class SimpleConverter:
    """Conversor simplificado de documentos"""

    def __init__(self):
        self.supported_formats = ['.txt', '.md', '.html', '.htm']

    def convert_file(self, file_path):
        """Converte um arquivo para formato estruturado"""

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

        if file_path.suffix.lower() not in self.supported_formats:
            raise ValueError(f"Formato não suportado: {file_path.suffix}")

        # Ler conteúdo do arquivo
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Converter baseado no formato
        if file_path.suffix.lower() == '.txt':
            markdown_text = self._txt_to_markdown(content)
        elif file_path.suffix.lower() == '.md':
            markdown_text = content  # Já está em Markdown
        elif file_path.suffix.lower() in ['.html', '.htm']:
            markdown_text = self._html_to_markdown(content)
        else:
            markdown_text = content

        # Criar estrutura JSON
        json_data = self._create_json_structure(file_path, markdown_text)

        return {
            'markdown': markdown_text,
            'json': json_data,
            'metadata': {
                'original_file': str(file_path),
                'format': file_path.suffix,
                'size_bytes': file_path.stat().st_size,
                'converted_at': datetime.now().isoformat()
            }
        }

    def _txt_to_markdown(self, text):
        """Converte TXT para Markdown básico"""

        lines = text.split('\n')
        markdown = []

        for line in lines:
            stripped = line.strip()

            # Detectar títulos (linhas em maiúsculas)
            if stripped and stripped.isupper() and len(stripped) > 3:
                markdown.append(f"## {stripped.title()}")
            # Detectar listas numeradas
            elif re.match(r'^\d+\.', stripped):
                markdown.append(line)
            # Detectar listas com traços
            elif stripped.startswith('-'):
                markdown.append(line)
            else:
                markdown.append(line)

        return '\n'.join(markdown)

    def _html_to_markdown(self, html):
        """Converte HTML para Markdown básico"""

        parser = HTMLToText()
        parser.feed(html)
        return parser.get_text()

    def _create_json_structure(self, file_path, markdown_text):
        """Cria estrutura JSON do documento"""

        # Extrair seções baseadas em cabeçalhos
        sections = []
        current_section = None

        for line in markdown_text.split('\n'):
            if line.startswith('#'):
                if current_section:
                    sections.append(current_section)

                level = len(line) - len(line.lstrip('#'))
                title = line.lstrip('#').strip()

                current_section = {
                    'level': level,
                    'title': title,
                    'content': []
                }
            elif current_section is not None:
                if line.strip():
                    current_section['content'].append(line)

        if current_section:
            sections.append(current_section)

        return {
            'document': {
                'name': file_path.name,
                'type': file_path.suffix,
                'sections': sections,
                'total_sections': len(sections),
                'total_lines': len(markdown_text.split('\n')),
                'total_characters': len(markdown_text)
            }
        }


def run_tests():
    """Executa testes de conversão"""

    print("=" * 70)
    print("CONVERSOR SIMPLIFICADO - DEMONSTRAÇÃO DE FUNCIONALIDADES")
    print("=" * 70)
    print()

    # Criar conversor
    print("🔧 Inicializando conversor simplificado...")
    converter = SimpleConverter()
    print(f"✅ Formatos suportados: {', '.join(converter.supported_formats)}")
    print()

    # Diretórios
    test_dir = Path("/home/user/Docling---Conversor-de-Documentos-Tkinter-/test_files")
    output_dir = Path("/home/user/Docling---Conversor-de-Documentos-Tkinter-/test_output")
    output_dir.mkdir(exist_ok=True)

    # Listar arquivos de teste
    test_files = [f for f in test_dir.glob("*") if f.suffix.lower() in converter.supported_formats]

    print(f"📁 Arquivos de teste encontrados: {len(test_files)}")
    for f in test_files:
        print(f"   - {f.name} ({f.stat().st_size} bytes)")
    print()

    # Testar conversões
    results = []

    for test_file in test_files:
        print("-" * 70)
        print(f"🔄 Convertendo: {test_file.name}")

        try:
            # Converter
            result = converter.convert_file(test_file)

            # Salvar Markdown
            md_output = output_dir / f"{test_file.stem}_simple.md"
            with open(md_output, 'w', encoding='utf-8') as f:
                f.write(result['markdown'])
            print(f"   ✅ Markdown: {md_output.name}")

            # Salvar JSON
            json_output = output_dir / f"{test_file.stem}_simple.json"
            with open(json_output, 'w', encoding='utf-8') as f:
                json.dump(result['json'], f, indent=2, ensure_ascii=False)
            print(f"   ✅ JSON: {json_output.name}")

            # Mostrar metadata
            print(f"   📊 Tamanho original: {result['metadata']['size_bytes']} bytes")
            print(f"   📊 Total de linhas: {result['json']['document']['total_lines']}")
            print(f"   📊 Total de seções: {result['json']['document']['total_sections']}")

            results.append({
                'file': test_file.name,
                'status': 'success',
                'markdown_path': str(md_output),
                'json_path': str(json_output)
            })

        except Exception as e:
            print(f"   ❌ Erro: {str(e)}")
            results.append({
                'file': test_file.name,
                'status': 'error',
                'error': str(e)
            })

    # Resumo
    print()
    print("=" * 70)
    print("RESUMO DOS TESTES")
    print("=" * 70)

    success_count = sum(1 for r in results if r['status'] == 'success')
    error_count = len(results) - success_count

    print(f"✅ Conversões bem-sucedidas: {success_count}/{len(results)}")
    print(f"❌ Erros: {error_count}")
    print()

    # Preview dos resultados
    if success_count > 0:
        print("=" * 70)
        print("PREVIEW DOS RESULTADOS (PRIMEIRAS 20 LINHAS)")
        print("=" * 70)

        for result in results:
            if result['status'] == 'success':
                print()
                print(f"\n📄 {result['file']} → MARKDOWN")
                print("-" * 70)

                with open(result['markdown_path'], 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines[:20], 1):
                        print(f"{i:3d} | {line.rstrip()}")

                    if len(lines) > 20:
                        print("... [mais linhas]")

                print()
                print(f"📄 {result['file']} → JSON (estrutura)")
                print("-" * 70)

                with open(result['json_path'], 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    print(json.dumps(data, indent=2, ensure_ascii=False)[:500])
                    print("... [mais dados]")

    print()
    print("=" * 70)
    print(f"✅ TESTES CONCLUÍDOS!")
    print(f"📂 Arquivos salvos em: {output_dir}")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
