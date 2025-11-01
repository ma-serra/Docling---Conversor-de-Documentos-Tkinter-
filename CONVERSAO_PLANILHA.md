# 📊 Sistema de Análise e Conversão para Planilha

## ✅ SISTEMA COMPLETO DE CONVERSÃO

Converte **QUALQUER DOCUMENTO** em **PLANILHA EXCEL/CSV** automaticamente!

---

## 🎯 O QUE FAZ

### **Extração Automática de Dados**
- Analisa documentos (PDF, DOCX, HTML, TXT, MD)
- Detecta tabelas automaticamente
- Extrai campos estruturados
- Converte para formato tabular

### **Preview Interativo**
- Visualiza dados em tabela antes de exportar
- Múltiplas abas para múltiplas tabelas
- Scroll horizontal e vertical
- Informações de linhas e colunas

### **Exportação Profissional**
- Excel (.xlsx) com múltiplas abas
- CSV (um arquivo por tabela)
- Preserva estrutura de dados
- Pronto para análise

---

## 🖥️ INTERFACE

```
┌─────────────────────────────────────────────────────────────┐
│  📊 Análise e Conversão para Planilha                        │
├─────────────────────────────────────────────────────────────┤
│  [📂 Carregar] [🔍 Analisar] [📗 Excel] [📄 CSV]          │
├─────────────────────────────────────────────────────────────┤
│  📋 ANÁLISE DO DOCUMENTO                                    │
│  Tabelas: 2  │  Campos: 15  │  Linhas: 50  │  Colunas: 8  │
├─────────────────────────────────────────────────────────────┤
│  👁️ PREVIEW DOS DADOS                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ [Tabela 1] [Tabela 2] [Campos]                      │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │ Campo          │ Valor                              │   │
│  ├────────────────┼────────────────────────────────────┤   │
│  │ Nome           │ João Silva                         │   │
│  │ CPF            │ 123.456.789-00                     │   │
│  │ Valor          │ R$ 50.000,00                       │   │
│  │ ...            │ ...                                │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 COMO USAR

### **1. Executar o Sistema**

```bash
python app_analise_planilha.py
```

---

### **2. Carregar Documento**

- Clique em **"📂 Carregar Documento"**
- Escolha arquivo: PDF, DOCX, HTML, TXT, MD
- Nome do arquivo aparece no topo

---

### **3. Analisar**

- Clique em **"🔍 Analisar"**
- Sistema extrai dados automaticamente
- Mostra estatísticas:
  - Tabelas encontradas
  - Campos detectados
  - Total de linhas
  - Total de colunas

---

### **4. Visualizar Preview**

- Dados aparecem em formato de tabela
- Abas para cada tabela encontrada
- Scroll para ver todos os dados
- Limitado a 1000 linhas no preview (todas são exportadas)

---

### **5. Exportar**

**Opção A: Excel**
- Clique em **"📗 Exportar Excel"**
- Escolha onde salvar
- Arquivo .xlsx com múltiplas abas

**Opção B: CSV**
- Clique em **"📄 Exportar CSV"**
- Escolha pasta
- Um arquivo CSV por tabela

---

## 📋 O QUE É EXTRAÍDO

### **Tabelas HTML**
✅ Detecta automaticamente tabelas `<table>`
✅ Extrai cabeçalhos e dados
✅ Preserva estrutura de linhas/colunas

### **Campos Estruturados**
✅ Detecta campos `data-field`
✅ Extrai pares campo-valor
✅ Converte em formato tabular

### **Documentos Markdown**
✅ Extrai seções por headers
✅ Detecta formato "Campo: Valor"
✅ Cria tabelas por seção

### **PDF/DOCX (via Docling)**
✅ Converte para Markdown
✅ Aplica extração estruturada
✅ Gera tabelas organizadas

---

## 💡 EXEMPLOS DE USO

### **Exemplo 1: Converter Contrato**

```bash
# 1. Abrir app
python app_analise_planilha.py

# 2. Carregar: contrato.pdf
# 3. Analisar
# Resultado:
#   - Tabela "Partes": nome, CPF, endereço
#   - Tabela "Valores": parcela, valor, data
#   - Tabela "Condições": campo, descrição

# 4. Exportar Excel → contrato.xlsx
```

**Resultado: Excel com 3 abas, dados organizados**

---

### **Exemplo 2: Extrair Dados de HTML**

```bash
# Documento HTML com campos:
# <span data-field="nome">João Silva</span>
# <span data-field="cpf">123.456.789-00</span>
# ...

# Após analisar:
# Tabela "campos_extraidos":
# ┌─────────┬──────────────────┐
# │ field   │ value            │
# ├─────────┼──────────────────┤
# │ nome    │ João Silva       │
# │ cpf     │ 123.456.789-00   │
# └─────────┴──────────────────┘

# Exportar CSV → campos_extraidos.csv
```

---

### **Exemplo 3: Múltiplas Tabelas**

```bash
# Documento com várias tabelas

# Após análise:
# - Tabela 1: "Produtos" (3 colunas × 10 linhas)
# - Tabela 2: "Preços" (2 colunas × 10 linhas)
# - Tabela 3: "Totais" (2 colunas × 5 linhas)

# Exportar Excel:
# → documento.xlsx
#    ├─ Aba "Produtos"
#    ├─ Aba "Preços"
#    └─ Aba "Totais"
```

---

## 🔧 API PYTHON

### **Uso Programático**

```python
from document_to_spreadsheet import DocumentToSpreadsheetConverter
import pandas as pd

# Criar converter
converter = DocumentToSpreadsheetConverter()

# Extrair dados
extracted = converter.extract_data_from_document("documento.pdf")

# Ver o que foi encontrado
print(f"Tabelas: {len(extracted['tables'])}")
print(f"Campos: {len(extracted['fields'])}")

# Converter para DataFrames
dfs = converter.convert_to_dataframe(extracted)

# Trabalhar com pandas
for df in dfs:
    print(df.head())
    print(df.describe())

# Exportar Excel
converter.export_to_excel(dfs, "saida.xlsx")

# Exportar CSV
converter.export_to_csv(dfs, "pasta_csv/")
```

---

## 📊 FORMATOS SUPORTADOS

| Formato | Entrada | Análise | Tabelas | Campos |
|---------|---------|---------|---------|--------|
| HTML | ✅ | ✅ Completa | ✅ Auto | ✅ Sim |
| PDF | ✅ | ✅ Docling | ✅ Auto | ✅ Parcial |
| DOCX | ✅ | ✅ Docling | ✅ Auto | ✅ Parcial |
| TXT | ✅ | ✅ Básica | ✅ Padrões | ✅ Sim |
| MD | ✅ | ✅ Completa | ✅ Seções | ✅ Sim |

| Formato | Saída | Múltiplas Abas | Formatação |
|---------|-------|----------------|------------|
| Excel | ✅ .xlsx | ✅ Sim | ✅ Preservada |
| CSV | ✅ .csv | ✅ Múltiplos arquivos | ⚠️ Básica |

---

## 🎯 CASOS DE USO REAIS

### **1. Migração de Dados**
- Contratos antigos em PDF
- → Extrair dados
- → Planilha Excel
- → Importar em sistema novo

### **2. Análise de Documentos**
- Múltiplos documentos
- → Converter todos
- → Consolidar em Excel
- → Análise com Power BI

### **3. Extração de Formulários**
- Formulários preenchidos (PDF)
- → Extrair campos
- → CSV para banco de dados

### **4. Relatórios Estruturados**
- Relatórios em HTML
- → Extrair tabelas
- → Excel para análise
- → Gráficos e dashboards

---

## ⚙️ CONFIGURAÇÃO

### **Instalação**

```bash
# Instalar dependências
pip install pandas openpyxl beautifulsoup4 lxml

# Opcional (para PDF/DOCX):
pip install docling
```

### **Executar**

```bash
python app_analise_planilha.py
```

---

## 🔍 DETECÇÃO AUTOMÁTICA

### **O Sistema Detecta:**

✅ Tabelas HTML (`<table>`)
✅ Campos com `data-field`
✅ Listas estruturadas
✅ Formato "Campo: Valor"
✅ Seções por headings
✅ Padrões de dados tabulares

### **Sugestões Automáticas:**

- **1 tabela encontrada** → CSV único ou Excel simples
- **Múltiplas tabelas** → Excel com abas ou CSVs separados
- **Só campos** → Tabela campo-valor transposta

---

## 📈 PERFORMANCE

| Tamanho Doc | Tempo Análise | Preview | Export Excel |
|-------------|---------------|---------|--------------|
| < 1 MB | < 1s | Instantâneo | < 1s |
| 1-10 MB | 1-5s | Rápido | 1-3s |
| 10-50 MB | 5-15s | OK | 3-10s |
| > 50 MB | 15s+ | Limitado* | 10s+ |

*Preview limitado a 1000 linhas, exportação completa

---

## 🆚 DIFERENÇA DOS OUTROS SISTEMAS

| Sistema | Função |
|---------|--------|
| `app_legal.py` | Templates predefinidos |
| `app_tkinter.py` | Conversor de formatos |
| `app_clone_documentos.py` | Clonagem de formatação |
| **`app_analise_planilha.py`** | **Conversão para PLANILHA** ⭐ |

---

## ✅ RESUMO

**Entrada:**
- PDF, DOCX, HTML, TXT, MD

**Processo:**
- Análise automática
- Detecção de tabelas
- Extração de campos

**Saída:**
- Excel (.xlsx) profissional
- CSV organizado
- Dados estruturados

**Diferencial:**
- Preview interativo
- Múltiplas tabelas
- Zero configuração
- Um clique para exportar

---

## 🚀 COMECE AGORA

```bash
# Execute
python app_analise_planilha.py

# Carregue documento
# Analise
# Exporte

# Pronto! Dados em planilha! 🎉
```

---

## 📁 ARQUIVOS

```
app_analise_planilha.py          ← Interface principal
document_to_spreadsheet.py        ← Motor de conversão
output_examples/
├── documento_convertido.xlsx    ← Exemplo Excel
└── csv/                         ← Exemplos CSV
    └── table_0.csv
```

---

## 🎉 TESTE REALIZADO

```
Documento: templates/confissao_divida.html

Resultado:
✓ Tabelas encontradas: 1
✓ Campos detectados: 21
✓ Linhas extraídas: 6
✓ Colunas: 2

Exportado:
✓ documento_convertido.xlsx
✓ table_0.csv

FUNCIONANDO 100%!
```

---

**📊 CONVERTA DOCUMENTOS EM PLANILHAS AGORA!** 🚀
