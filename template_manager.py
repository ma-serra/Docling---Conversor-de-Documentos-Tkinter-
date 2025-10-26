"""
Template Manager for Legal Documents
Gerenciador de Templates para Documentos Jurídicos
"""

import os
import json
import re
from typing import Dict, List, Any, Optional
from pathlib import Path
from bs4 import BeautifulSoup


class TemplateManager:
    """Gerencia templates HTML de documentos jurídicos"""

    def __init__(self, templates_dir: str = "templates"):
        self.templates_dir = Path(templates_dir)
        self.templates_dir.mkdir(exist_ok=True)
        self.config_file = self.templates_dir / "templates_config.json"
        self.load_config()

    def load_config(self):
        """Carrega configuração de templates"""
        if self.config_file.exists():
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            self.config = {
                "templates": []
            }
            self.save_config()

    def save_config(self):
        """Salva configuração de templates"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)

    def get_available_templates(self) -> List[Dict[str, Any]]:
        """Retorna lista de templates disponíveis"""
        templates = []
        for html_file in self.templates_dir.glob("*.html"):
            template_info = self.get_template_info(html_file.name)
            templates.append(template_info)
        return templates

    def get_template_info(self, template_name: str) -> Dict[str, Any]:
        """Obtém informações sobre um template"""
        template_path = self.templates_dir / template_name

        if not template_path.exists():
            return {}

        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')

        # Extrai título do documento
        title_tag = soup.find('title')
        title = title_tag.text if title_tag else template_name

        # Extrai campos variáveis
        fields = self.extract_fields(content)

        return {
            "name": template_name,
            "title": title,
            "path": str(template_path),
            "fields": fields,
            "field_count": len(fields)
        }

    def extract_fields(self, html_content: str) -> List[Dict[str, str]]:
        """Extrai campos variáveis do template HTML"""
        soup = BeautifulSoup(html_content, 'html.parser')
        fields = []
        seen_fields = set()

        # Busca elementos com data-field
        for element in soup.find_all(attrs={"data-field": True}):
            field_name = element.get('data-field')
            if field_name and field_name not in seen_fields:
                field_label = self._generate_field_label(field_name)
                field_type = self._infer_field_type(field_name, element.text)

                fields.append({
                    "name": field_name,
                    "label": field_label,
                    "type": field_type,
                    "default": element.text.strip()
                })
                seen_fields.add(field_name)

        return fields

    def _generate_field_label(self, field_name: str) -> str:
        """Gera label legível a partir do nome do campo"""
        # Remove underscores e capitaliza
        words = field_name.split('_')
        return ' '.join(word.capitalize() for word in words)

    def _infer_field_type(self, field_name: str, default_value: str) -> str:
        """Infere o tipo de campo baseado no nome e valor padrão"""
        field_name_lower = field_name.lower()

        # Data
        if 'data' in field_name_lower or re.search(r'\d{2}/\d{2}/\d{4}', default_value):
            return "date"

        # CPF/CNPJ
        if 'cpf' in field_name_lower or 'cnpj' in field_name_lower:
            return "document"

        # Valores monetários
        if 'valor' in field_name_lower or 'R$' in default_value:
            return "money"

        # Números
        if 'numero' in field_name_lower or field_name_lower.startswith('num_'):
            return "number"

        # Email
        if 'email' in field_name_lower or '@' in default_value:
            return "email"

        # Telefone
        if 'telefone' in field_name_lower or 'fone' in field_name_lower:
            return "phone"

        # CEP
        if 'cep' in field_name_lower:
            return "cep"

        # Endereço (texto longo)
        if 'endereco' in field_name_lower or 'logradouro' in field_name_lower:
            return "textarea"

        # Texto padrão
        return "text"

    def fill_template(self, template_name: str, data: Dict[str, str]) -> str:
        """Preenche template com dados fornecidos"""
        template_path = self.templates_dir / template_name

        if not template_path.exists():
            raise FileNotFoundError(f"Template '{template_name}' não encontrado")

        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')

        # Substitui valores dos campos
        for field_name, field_value in data.items():
            elements = soup.find_all(attrs={"data-field": field_name})
            for element in elements:
                element.string = field_value

        return str(soup)

    def save_filled_template(self, html_content: str, output_path: str):
        """Salva template preenchido"""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

    def export_to_markdown(self, html_content: str) -> str:
        """Converte HTML para Markdown"""
        soup = BeautifulSoup(html_content, 'html.parser')

        # Remove scripts e styles
        for script in soup(["script", "style"]):
            script.decompose()

        # Extrai texto
        text = soup.get_text()

        # Limpa linhas vazias extras
        lines = [line.strip() for line in text.splitlines() if line.strip()]

        return '\n\n'.join(lines)

    def validate_data(self, template_name: str, data: Dict[str, str]) -> Dict[str, List[str]]:
        """Valida dados contra campos do template"""
        template_info = self.get_template_info(template_name)
        errors = {}

        required_fields = [field['name'] for field in template_info['fields']]

        # Verifica campos obrigatórios
        for field_name in required_fields:
            if field_name not in data or not data[field_name].strip():
                if field_name not in errors:
                    errors[field_name] = []
                errors[field_name].append("Campo obrigatório não preenchido")

        # Valida formatos específicos
        for field_name, field_value in data.items():
            field_info = next((f for f in template_info['fields'] if f['name'] == field_name), None)
            if not field_info:
                continue

            field_type = field_info['type']

            # Validação de CPF (formato básico)
            if field_type == "document" and 'cpf' in field_name.lower():
                if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', field_value):
                    if field_name not in errors:
                        errors[field_name] = []
                    errors[field_name].append("Formato de CPF inválido (esperado: 000.000.000-00)")

            # Validação de CNPJ (formato básico)
            if field_type == "document" and 'cnpj' in field_name.lower():
                if not re.match(r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', field_value):
                    if field_name not in errors:
                        errors[field_name] = []
                    errors[field_name].append("Formato de CNPJ inválido (esperado: 00.000.000/0000-00)")

            # Validação de data
            if field_type == "date":
                if not re.match(r'^\d{2}/\d{2}/\d{4}$', field_value):
                    if field_name not in errors:
                        errors[field_name] = []
                    errors[field_name].append("Formato de data inválido (esperado: DD/MM/AAAA)")

            # Validação de email
            if field_type == "email":
                if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', field_value):
                    if field_name not in errors:
                        errors[field_name] = []
                    errors[field_name].append("Formato de email inválido")

        return errors

    def create_template_from_html(self, html_path: str, template_name: str):
        """Cria um novo template a partir de arquivo HTML"""
        source_path = Path(html_path)
        if not source_path.exists():
            raise FileNotFoundError(f"Arquivo '{html_path}' não encontrado")

        dest_path = self.templates_dir / template_name

        # Copia arquivo
        with open(source_path, 'r', encoding='utf-8') as src:
            content = src.read()

        with open(dest_path, 'w', encoding='utf-8') as dst:
            dst.write(content)

        return self.get_template_info(template_name)


# Funções auxiliares para exportação
def html_to_pdf(html_content: str, output_path: str):
    """
    Converte HTML para PDF usando weasyprint
    Requer: pip install weasyprint
    """
    try:
        from weasyprint import HTML
        HTML(string=html_content).write_pdf(output_path)
        return True
    except ImportError:
        print("Biblioteca 'weasyprint' não encontrada. Instale com: pip install weasyprint")
        return False
    except Exception as e:
        print(f"Erro ao gerar PDF: {e}")
        return False


if __name__ == "__main__":
    # Teste do gerenciador
    manager = TemplateManager()

    print("=== Templates Disponíveis ===")
    templates = manager.get_available_templates()

    for template in templates:
        print(f"\nTemplate: {template['title']}")
        print(f"Arquivo: {template['name']}")
        print(f"Campos: {template['field_count']}")

        if template['fields']:
            print("\nCampos variáveis:")
            for field in template['fields'][:5]:  # Mostra primeiros 5
                print(f"  - {field['label']} ({field['type']})")
