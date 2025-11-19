# Guia de Uso do Docling Converter

## Introdução

O **Docling Document Converter** é uma ferramenta poderosa para conversão de documentos.

## Características

### Formatos Suportados

- **Entrada**: PDF, DOCX, TXT, MD, HTML, RTF
- **Saída**: Markdown, JSON

### Interface

A interface conta com:

1. Seleção de arquivos
2. Escolha de formato de saída
3. Visualização de progresso
4. Preview do resultado

## Exemplo de Código

```python
from docling.document_converter import DocumentConverter

converter = DocumentConverter()
result = converter.convert("document.pdf")
```

## Tabela de Recursos

| Recurso | Disponível | Descrição |
|---------|------------|-----------|
| Conversão PDF | ✅ | Extração de texto e layout |
| Conversão DOCX | ✅ | Suporte completo |
| Batch Processing | 🔄 | Em desenvolvimento |

## Links Úteis

- [Documentação](https://docling.readthedocs.io)
- [GitHub](https://github.com/docling)
- [PyPI](https://pypi.org/project/docling)

---

*Última atualização: 2025*
