#!/usr/bin/env python3
"""
Script de Validação do Sistema
Testa se tudo está configurado corretamente SEM abrir interface gráfica
"""

print("=" * 70)
print("🔍 VALIDANDO SISTEMA DOCLING LEGAL")
print("=" * 70)
print()

# 1. Verifica arquivos principais
import os
from pathlib import Path

print("📁 VERIFICANDO ARQUIVOS...")
files_to_check = [
    'app_legal.py',
    'template_manager.py',
    'demo_template.py',
    'templates/confissao_divida.html',
    'templates/guia_morador.html',
    'templates/templates_config.json',
]

all_files_ok = True
for file in files_to_check:
    if Path(file).exists():
        size = Path(file).stat().st_size
        print(f"   ✓ {file} ({size:,} bytes)")
    else:
        print(f"   ✗ {file} NÃO ENCONTRADO")
        all_files_ok = False

print()

# 2. Testa sintaxe do código principal
print("🐍 VERIFICANDO SINTAXE DO CÓDIGO...")
import py_compile

code_files = ['app_legal.py', 'template_manager.py', 'demo_template.py']
syntax_ok = True

for code_file in code_files:
    try:
        py_compile.compile(code_file, doraise=True)
        print(f"   ✓ {code_file} - sintaxe OK")
    except py_compile.PyCompileError as e:
        print(f"   ✗ {code_file} - ERRO DE SINTAXE")
        print(f"      {e}")
        syntax_ok = False

print()

# 3. Testa template manager
print("📋 TESTANDO TEMPLATE MANAGER...")
try:
    from template_manager import TemplateManager
    manager = TemplateManager()
    templates = manager.get_available_templates()

    print(f"   ✓ TemplateManager carregado")
    print(f"   ✓ {len(templates)} templates encontrados")

    for t in templates:
        print(f"      • {t['title']} ({t['field_count']} campos)")

    template_ok = True
except Exception as e:
    print(f"   ✗ Erro ao testar TemplateManager: {e}")
    template_ok = False

print()

# 4. Verifica dependências opcionais
print("📦 VERIFICANDO DEPENDÊNCIAS...")

dependencies = {
    'beautifulsoup4': 'bs4',
    'lxml': 'lxml',
    'docling': 'docling',
}

deps_status = {}
for name, import_name in dependencies.items():
    try:
        __import__(import_name)
        print(f"   ✓ {name} instalado")
        deps_status[name] = True
    except ImportError:
        print(f"   ⚠ {name} não instalado (opcional)")
        deps_status[name] = False

print()

# 5. Status final
print("=" * 70)
print("📊 RESULTADO DA VALIDAÇÃO")
print("=" * 70)

status_items = [
    ("Arquivos principais", all_files_ok),
    ("Sintaxe do código", syntax_ok),
    ("Template Manager", template_ok),
    ("BeautifulSoup4", deps_status.get('beautifulsoup4', False)),
]

all_ok = all(status for _, status in status_items)

for item, status in status_items:
    icon = "✓" if status else "✗"
    print(f"   {icon} {item}")

print()
print("=" * 70)

if all_ok:
    print("✅ SISTEMA VALIDADO COM SUCESSO!")
    print()
    print("O código está correto e pronto para uso.")
    print()
    print("PRÓXIMO PASSO:")
    print("  Execute no seu computador com interface gráfica:")
    print("  python app_legal.py")
else:
    print("⚠️  ATENÇÃO: Alguns itens precisam de atenção")
    print()
    print("Instale dependências faltantes:")
    print("  pip install beautifulsoup4 lxml")
    print()
    print("Para usar o conversor (opcional):")
    print("  pip install docling")

print("=" * 70)
