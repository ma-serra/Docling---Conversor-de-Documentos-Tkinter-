#!/usr/bin/env python3
"""
GERAÇÃO RÁPIDA - GERA DOCUMENTO JÁ PRONTO
Não precisa preencher nada, só executar
"""

from template_manager import TemplateManager
from datetime import datetime

print("=" * 70)
print("GERADOR RÁPIDO - CONFISSÃO DE DÍVIDA")
print("=" * 70)

manager = TemplateManager("templates")

# Dados já preenchidos (você pode editar aqui)
dados = {
    "credor_nome": "MINHA EMPRESA LTDA",
    "credor_cnpj": "12.345.678/0001-90",
    "credor_endereco": "Rua das Flores, 100, Centro, São Paulo/SP, CEP 01000-000",
    "credor_representante": "João da Silva",
    "credor_rg": "12.345.678-9 SSP/SP",
    "credor_cpf": "123.456.789-00",

    "devedor_nome": "MARIA SANTOS OLIVEIRA",
    "devedor_rg": "98.765.432-1 SSP/SP",
    "devedor_cpf": "987.654.321-00",
    "devedor_endereco": "Av. Paulista, 1000, Apto 52, São Paulo/SP, CEP 01310-100",

    "valor_total": "R$ 50.000,00 (cinquenta mil reais)",
    "motivo_divida": "prestação de serviços jurídicos realizados entre janeiro e junho de 2025",
    "num_parcelas": "10 (dez)",
    "valor_parcela": "R$ 5.000,00 (cinco mil reais)",
    "data_primeira_parcela": "15/12/2025",

    "juros_mora": "1% ao mês",
    "multa_atraso": "2%",
    "dados_bancarios": "Banco do Brasil, Agência 1234-5, Conta Corrente 12345-6",
    "foro": "São Paulo/SP",
    "cidade": "São Paulo/SP",
    "data_assinatura": datetime.now().strftime("%d/%m/%Y")
}

print("\n📝 Gerando documento com dados de exemplo...")
print(f"   Credor: {dados['credor_nome']}")
print(f"   Devedor: {dados['devedor_nome']}")
print(f"   Valor: {dados['valor_total']}")

# Gerar
html = manager.fill_template("confissao_divida.html", dados)

# Salvar
output_html = "output_examples/confissao_divida_gerada.html"
manager.save_filled_template(html, output_html)

# Markdown
markdown = manager.export_to_markdown(html)
output_md = "output_examples/confissao_divida_gerada.md"
with open(output_md, 'w', encoding='utf-8') as f:
    f.write(markdown)

print("\n" + "=" * 70)
print("✅ DOCUMENTO GERADO COM SUCESSO!")
print("=" * 70)
print(f"\nArquivos criados:")
print(f"  📄 {output_html}")
print(f"  📝 {output_md}")
print(f"\nAbra o arquivo HTML no navegador para ver o documento completo.")
print(f"Tamanho: {len(html):,} bytes")
print("=" * 70)
