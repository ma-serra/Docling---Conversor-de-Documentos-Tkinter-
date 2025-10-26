#!/usr/bin/env python3
"""
Script de Demonstração - Template Manager
Mostra como usar o sistema via código Python
"""

from template_manager import TemplateManager
from pathlib import Path

def main():
    print("=" * 60)
    print("DEMONSTRAÇÃO DO SISTEMA DE TEMPLATES JURÍDICOS")
    print("=" * 60)
    print()

    # Inicializa o gerenciador
    manager = TemplateManager()

    # Lista templates disponíveis
    print("📋 TEMPLATES DISPONÍVEIS:")
    print("-" * 60)
    templates = manager.get_available_templates()

    for i, template in enumerate(templates, 1):
        print(f"\n{i}. {template['title']}")
        print(f"   Arquivo: {template['name']}")
        print(f"   Campos: {template['field_count']}")

        if template['fields']:
            print(f"   Primeiros campos:")
            for field in template['fields'][:3]:
                print(f"      • {field['label']} ({field['type']})")

    print("\n" + "=" * 60)

    # Demonstra preenchimento do template de Confissão de Dívida
    if templates:
        print("\n📝 DEMONSTRAÇÃO: Preenchendo Confissão de Dívida")
        print("-" * 60)

        # Dados de exemplo
        dados = {
            "credor_nome": "ESCRITÓRIO XYZ ADVOCACIA LTDA",
            "credor_cnpj": "11.222.333/0001-44",
            "credor_endereco": "Rua Exemplo, 999, São Paulo/SP, CEP 01000-000",
            "credor_representante": "Dr. Carlos Alberto",
            "credor_rg": "11.222.333-4 SSP/SP",
            "credor_cpf": "111.222.333-44",

            "devedor_nome": "JOSÉ DA SILVA SANTOS",
            "devedor_rg": "99.888.777-6 SSP/SP",
            "devedor_cpf": "999.888.777-66",
            "devedor_endereco": "Av. Principal, 123, Apto 45, São Paulo/SP, CEP 02000-000",

            "valor_total": "R$ 100.000,00 (cem mil reais)",
            "motivo_divida": "prestação de serviços jurídicos entre janeiro e dezembro de 2024",
            "num_parcelas": "20 (vinte)",
            "valor_parcela": "R$ 5.000,00 (cinco mil reais)",
            "data_primeira_parcela": "15 de novembro de 2025",

            "juros_mora": "1,5% ao mês",
            "multa_atraso": "2%",
            "dados_bancarios": "Banco Itaú, Agência 1234, Conta Corrente 56789-0",
            "foro": "São Paulo/SP",
            "cidade": "São Paulo/SP",
            "data_assinatura": "26 de outubro de 2025"
        }

        print("\n✓ Dados preparados:")
        for key, value in list(dados.items())[:5]:
            print(f"   {key}: {value}")
        print("   ... (mais campos)")

        # Valida dados
        print("\n🔍 Validando dados...")
        errors = manager.validate_data("confissao_divida.html", dados)

        if errors:
            print("❌ Erros encontrados:")
            for field, msgs in errors.items():
                print(f"   • {field}: {', '.join(msgs)}")
        else:
            print("✓ Todos os dados estão válidos!")

        # Preenche template
        print("\n📄 Preenchendo template...")
        try:
            filled_html = manager.fill_template("confissao_divida.html", dados)

            # Salva documento
            output_dir = Path("output_examples")
            output_dir.mkdir(exist_ok=True)

            html_file = output_dir / "confissao_divida_exemplo.html"
            manager.save_filled_template(filled_html, str(html_file))
            print(f"✓ Documento HTML salvo em: {html_file}")

            # Exporta para Markdown
            markdown = manager.export_to_markdown(filled_html)
            md_file = output_dir / "confissao_divida_exemplo.md"
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(markdown)
            print(f"✓ Documento Markdown salvo em: {md_file}")

            print("\n" + "=" * 60)
            print("✅ DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO!")
            print("=" * 60)
            print(f"\nArquivos criados na pasta 'output_examples/':")
            print(f"  • {html_file.name} - Documento completo com formatação")
            print(f"  • {md_file.name} - Versão em texto Markdown")
            print("\nAbra o arquivo HTML no navegador para visualizar!")

        except Exception as e:
            print(f"❌ Erro ao processar template: {e}")

    print("\n" + "=" * 60)
    print("COMO USAR O SISTEMA COMPLETO:")
    print("=" * 60)
    print("\n1. Execute a aplicação gráfica:")
    print("   python app_legal.py")
    print("\n2. Vá para a aba 'Gerador de Documentos'")
    print("\n3. Selecione um template e clique em 'Carregar Template'")
    print("\n4. Preencha os campos e clique em 'Visualizar Documento'")
    print("\n5. Clique em 'Gerar e Salvar' para salvar o documento final")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
