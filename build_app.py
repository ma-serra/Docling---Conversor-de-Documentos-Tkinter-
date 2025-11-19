"""
Script para criar executável do Docling Converter usando PyInstaller
"""
import os
import subprocess
import sys

def build_executable():
    """Cria o executável usando PyInstaller"""
    print("=" * 60)
    print("Criando executável do Docling Document Converter...")
    print("=" * 60)

    # Nome do arquivo Python principal
    main_file = "app_tkinter.py"

    # Nome do executável
    app_name = "DoclingConverter"

    # Comando PyInstaller
    command = [
        "pyinstaller",
        "--name", app_name,
        "--onefile",  # Criar um único arquivo executável
        "--windowed",  # Não mostrar console (apenas GUI)
        "--clean",  # Limpar cache antes de buildar
        "--noconfirm",  # Sobrescrever sem perguntar
        main_file
    ]

    print("\nExecutando PyInstaller...")
    print(f"Comando: {' '.join(command)}\n")

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)

        print("\n" + "=" * 60)
        print("SUCESSO! Executável criado com sucesso!")
        print("=" * 60)
        print(f"\nExecutável localizado em: dist/{app_name}")
        print("\nVocê pode distribuir este arquivo para qualquer pessoa usar!")

    except subprocess.CalledProcessError as e:
        print("\n" + "=" * 60)
        print("ERRO ao criar executável!")
        print("=" * 60)
        print(f"\nErro: {e}")
        print(f"\nSaída: {e.stdout}")
        print(f"\nErro: {e.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    build_executable()
