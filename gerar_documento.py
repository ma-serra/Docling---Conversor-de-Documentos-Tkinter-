#!/usr/bin/env python3
"""
GERADOR SIMPLES DE DOCUMENTOS - SEM INTERFACE GRÁFICA
Funciona direto na linha de comando
"""

from template_manager import TemplateManager
import sys

def main():
    print("=" * 70)
    print("GERADOR DE DOCUMENTOS - LINHA DE COMANDO")
    print("=" * 70)

    manager = TemplateManager("templates")
    templates = manager.get_available_templates()

    # Listar templates
    print("\nTemplates disponíveis:")
    for i, t in enumerate(templates, 1):
        if t['field_count'] > 0:
            print(f"  {i}. {t['title']} ({t['field_count']} campos)")

    # Escolher template
    print("\nDigite o número do template que quer usar:")
    try:
        escolha = int(input("Número: "))
        template = [t for t in templates if t['field_count'] > 0][escolha - 1]
    except:
        print("Escolha inválida!")
        return

    print(f"\nVocê escolheu: {template['title']}")
    print(f"Campos a preencher: {template['field_count']}")
    print("\n" + "-" * 70)

    # Preencher campos
    dados = {}
    print("\nPreencha os campos (ou pressione Enter para usar valor padrão):\n")

    for field in template['fields']:
        default = field['default']
        valor = input(f"{field['label']} [{default}]: ").strip()
        dados[field['name']] = valor if valor else default

    # Gerar documento
    print("\n" + "=" * 70)
    print("GERANDO DOCUMENTO...")
    print("=" * 70)

    try:
        html = manager.fill_template(template['name'], dados)

        # Salvar
        output = f"output_examples/documento_gerado.html"
        manager.save_filled_template(html, output)

        print(f"\n✅ SUCESSO!")
        print(f"   Documento salvo em: {output}")
        print(f"   Tamanho: {len(html):,} bytes")
        print(f"\nAbra o arquivo no navegador para ver o resultado.")
        print("=" * 70)

    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
