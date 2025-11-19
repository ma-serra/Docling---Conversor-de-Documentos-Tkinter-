#!/usr/bin/env python3
"""
Script CLI para testar as funcionalidades do Docling Converter
Versão sem interface gráfica para testes em ambiente headless
"""

import os
import json
import sys
from pathlib import Path

def test_docling_conversion():
    """Testa a conversão usando a biblioteca docling"""

    print("=" * 70)
    print("DOCLING CONVERTER - TESTES DE FUNCIONALIDADES")
    print("=" * 70)
    print()

    try:
        print("📦 Importando biblioteca docling...")
        from docling.document_converter import DocumentConverter
        print("✅ Docling importado com sucesso!")
        print()

        # Criar conversor
        print("🔧 Inicializando conversor...")
        converter = DocumentConverter()
        print("✅ Conversor inicializado!")
        print()

        # Diretório de testes
        test_dir = Path("/home/user/Docling---Conversor-de-Documentos-Tkinter-/test_files")
        output_dir = Path("/home/user/Docling---Conversor-de-Documentos-Tkinter-/test_output")
        output_dir.mkdir(exist_ok=True)

        # Listar arquivos de teste
        test_files = list(test_dir.glob("*"))
        print(f"📁 Arquivos de teste encontrados: {len(test_files)}")
        for f in test_files:
            print(f"   - {f.name}")
        print()

        # Testar cada arquivo
        results = []
        for test_file in test_files:
            print("-" * 70)
            print(f"🔄 Convertendo: {test_file.name}")
            print(f"   Tamanho: {test_file.stat().st_size} bytes")

            try:
                # Converter para Markdown
                print("   Formato: Markdown")
                result = converter.convert(str(test_file))

                # Salvar resultado em Markdown
                md_output = output_dir / f"{test_file.stem}_converted.md"
                with open(md_output, 'w', encoding='utf-8') as f:
                    f.write(result.document.export_to_markdown())

                print(f"   ✅ Conversão para Markdown concluída: {md_output.name}")

                # Salvar resultado em JSON
                json_output = output_dir / f"{test_file.stem}_converted.json"
                with open(json_output, 'w', encoding='utf-8') as f:
                    json.dump(result.document.export_to_dict(), f, indent=2, ensure_ascii=False)

                print(f"   ✅ Conversão para JSON concluída: {json_output.name}")

                results.append({
                    'file': test_file.name,
                    'status': 'success',
                    'markdown': str(md_output),
                    'json': str(json_output)
                })

            except Exception as e:
                print(f"   ❌ Erro na conversão: {str(e)}")
                results.append({
                    'file': test_file.name,
                    'status': 'error',
                    'error': str(e)
                })

        print()
        print("=" * 70)
        print("RESUMO DOS TESTES")
        print("=" * 70)

        success_count = sum(1 for r in results if r['status'] == 'success')
        error_count = sum(1 for r in results if r['status'] == 'error')

        print(f"✅ Sucessos: {success_count}")
        print(f"❌ Erros: {error_count}")
        print(f"📊 Total: {len(results)}")
        print()

        # Mostrar primeiras linhas dos arquivos convertidos
        if success_count > 0:
            print("-" * 70)
            print("PREVIEW DOS RESULTADOS")
            print("-" * 70)

            for result in results:
                if result['status'] == 'success':
                    print(f"\n📄 {result['file']} → Markdown:")
                    print("-" * 70)
                    with open(result['markdown'], 'r', encoding='utf-8') as f:
                        lines = f.readlines()[:15]
                        for line in lines:
                            print(f"   {line.rstrip()}")
                        if len(f.readlines()) > 15:
                            print("   [...]")

        print()
        print("=" * 70)
        print(f"✅ TESTES CONCLUÍDOS! Arquivos salvos em: {output_dir}")
        print("=" * 70)

    except ImportError as e:
        print("❌ Erro: Biblioteca docling não está instalada!")
        print(f"   Detalhes: {e}")
        print()
        print("💡 Execute: pip install docling")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    test_docling_conversion()
