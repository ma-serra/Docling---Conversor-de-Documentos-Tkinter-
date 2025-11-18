#!/usr/bin/env python3
"""
MENU PRINCIPAL - DOCLING LEGAL
Escolha qual sistema você quer usar
"""

import subprocess
import sys

def print_header():
    print("=" * 70)
    print("🚀 DOCLING LEGAL - MENU PRINCIPAL")
    print("=" * 70)
    print()

def print_menu():
    print("Escolha o sistema que deseja executar:")
    print()
    print("  1️⃣  📊 ANÁLISE E CONVERSÃO PARA PLANILHA")
    print("      Converte documentos em Excel/CSV")
    print("      Execute: app_analise_planilha.py")
    print()
    print("  2️⃣  🔄 CLONAGEM DE FORMATAÇÃO")
    print("      Clona formatação de documentos existentes")
    print("      Execute: app_clone_documentos.py")
    print()
    print("  3️⃣  📝 GERADOR DE DOCUMENTOS JURÍDICOS")
    print("      Templates predefinidos (Confissão Dívida, etc)")
    print("      Execute: app_legal.py")
    print()
    print("  4️⃣  📄 CONVERSOR SIMPLES")
    print("      Converte PDF/DOCX para Markdown/JSON")
    print("      Execute: app_tkinter.py")
    print()
    print("  5️⃣  ⚡ GERADOR RÁPIDO (Terminal)")
    print("      Gera documento rapidamente sem interface")
    print("      Execute: gerar_rapido.py")
    print()
    print("  6️⃣  🔍 VALIDAR SISTEMA")
    print("      Testa se tudo está funcionando")
    print("      Execute: validate_system.py")
    print()
    print("  0️⃣  ❌ SAIR")
    print()
    print("=" * 70)

def run_system(choice):
    systems = {
        '1': ('app_analise_planilha.py', 'Análise e Conversão para Planilha'),
        '2': ('app_clone_documentos.py', 'Clonagem de Formatação'),
        '3': ('app_legal.py', 'Gerador de Documentos Jurídicos'),
        '4': ('app_tkinter.py', 'Conversor Simples'),
        '5': ('gerar_rapido.py', 'Gerador Rápido'),
        '6': ('validate_system.py', 'Validação do Sistema'),
    }

    if choice in systems:
        script, name = systems[choice]
        print()
        print(f"🚀 Executando: {name}")
        print(f"Arquivo: {script}")
        print("=" * 70)
        print()

        try:
            subprocess.run([sys.executable, script])
        except FileNotFoundError:
            print(f"❌ ERRO: Arquivo {script} não encontrado")
        except KeyboardInterrupt:
            print("\n\n⚠️ Execução interrompida pelo usuário")
        except Exception as e:
            print(f"❌ ERRO: {e}")

        print()
        input("Pressione ENTER para voltar ao menu...")

def show_system_info():
    print()
    print("📁 ARQUIVOS DISPONÍVEIS:")
    print()

    import os
    apps = [
        'app_analise_planilha.py',
        'app_clone_documentos.py',
        'app_legal.py',
        'app_tkinter.py',
        'gerar_rapido.py',
        'validate_system.py'
    ]

    for app in apps:
        if os.path.exists(app):
            size = os.path.getsize(app)
            print(f"  ✓ {app} ({size:,} bytes)")
        else:
            print(f"  ✗ {app} (NÃO ENCONTRADO)")

    print()
    print("📚 DOCUMENTAÇÃO:")
    docs = [
        'CONVERSAO_PLANILHA.md',
        'SISTEMA_CLONAGEM.md',
        'COMO_USAR_SIMPLES.md',
        'GUIA_USO.md',
        'README_LEGAL.md'
    ]

    for doc in docs:
        if os.path.exists(doc):
            print(f"  ✓ {doc}")

    print()

def main():
    while True:
        print_header()
        show_system_info()
        print_menu()

        choice = input("Digite sua escolha: ").strip()

        if choice == '0':
            print()
            print("👋 Até logo!")
            print()
            break
        elif choice in ['1', '2', '3', '4', '5', '6']:
            run_system(choice)
        else:
            print()
            print("❌ Opção inválida! Digite um número de 0 a 6")
            input("Pressione ENTER para continuar...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Até logo!")
