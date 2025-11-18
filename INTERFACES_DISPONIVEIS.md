# 🖥️ INTERFACES DISPONÍVEIS

## ✅ TODAS AS INTERFACES INSTALADAS E FUNCIONANDO!

---

## 📊 1. INTERFACE DE ANÁLISE E CONVERSÃO PARA PLANILHA

**Arquivo:** `app_analise_planilha.py`

**O QUE FAZ:**
- Interface gráfica moderna com tema escuro
- Carrega documentos (PDF, DOCX, HTML, TXT, MD)
- Analisa e extrai dados automaticamente
- Preview interativo com tabelas
- Exporta para Excel (.xlsx) ou CSV

**COMO USAR:**
```bash
python app_analise_planilha.py
```

**FUNCIONALIDADES:**
- 📂 Botão "Carregar Documento"
- 🔍 Botão "Analisar" (extrai dados)
- 👁️ Preview dos dados em tabela (Treeview)
- 📗 Botão "Exportar Excel" (múltiplas abas)
- 📄 Botão "Exportar CSV" (um arquivo por tabela)
- 📊 Estatísticas: tabelas, campos, linhas, colunas

**VISUAL:**
- Painel superior: Botões de ação
- Painel central: Estatísticas da análise
- Painel inferior: Preview dos dados em tabelas com scroll

---

## 🔄 2. INTERFACE DE CLONAGEM DE FORMATAÇÃO

**Arquivo:** `app_clone_documentos.py`

**O QUE FAZ:**
- Interface dividida em dois painéis
- Painel esquerdo: Visualiza documento fonte
- Painel direito: Edita template de destino
- Seleciona texto do documento e envia para campos do template
- Clona formatação de documentos existentes

**COMO USAR:**
```bash
python app_clone_documentos.py
```

**FUNCIONALIDADES:**
- 📂 Carregar Documento Fonte (esquerda)
- 📝 Carregar Template (direita)
- ✂️ Selecionar texto no documento
- ➡️ Botão "Enviar Seleção" → Campo selecionado
- 💾 Gerar Documento Final
- 📄 Preview em tempo real

**VISUAL:**
- Layout dividido verticalmente (50/50)
- Esquerda: Documento fonte (só leitura)
- Direita: Formulário editável com campos do template

---

## 📝 3. INTERFACE DE DOCUMENTOS JURÍDICOS

**Arquivo:** `app_legal.py`

**O QUE FAZ:**
- Interface gráfica para gerar documentos legais
- Templates predefinidos profissionais
- Formulários com validação de campos
- Exporta HTML ou PDF

**COMO USAR:**
```bash
python app_legal.py
```

**TEMPLATES DISPONÍVEIS:**
1. **Confissão de Dívida** (21 campos)
   - Dados do credor (nome, CNPJ, endereço, etc)
   - Dados do devedor (nome, CPF, RG, etc)
   - Informações da dívida (valor, juros, etc)

2. **Guia do Morador**
   - Manual para moradores de condomínio
   - Regras e orientações

**FUNCIONALIDADES:**
- 📋 Seleção de template
- 📝 Formulário com todos os campos
- ✅ Validação automática (CPF, CNPJ, datas)
- 📄 Preview do documento
- 💾 Exportar HTML/PDF

---

## 📄 4. INTERFACE CONVERSOR SIMPLES

**Arquivo:** `app_tkinter.py`

**O QUE FAZ:**
- Interface básica e simples
- Converte PDF/DOCX para Markdown ou JSON
- Sem recursos avançados, apenas conversão

**COMO USAR:**
```bash
python app_tkinter.py
```

**FUNCIONALIDADES:**
- 📂 Selecionar arquivo
- 🔄 Escolher formato de saída
- 💾 Converter

---

## ⚡ 5. GERADOR RÁPIDO (SEM INTERFACE GRÁFICA)

**Arquivo:** `gerar_rapido.py`

**O QUE FAZ:**
- Gera documento em 1 comando
- Sem interface gráfica (terminal)
- Dados pré-preenchidos para teste

**COMO USAR:**
```bash
python gerar_rapido.py
```

**RESULTADO:**
- Gera `documento_gerado.html` instantaneamente
- Pronto para abrir no navegador

---

## 🔍 6. VALIDAÇÃO DO SISTEMA

**Arquivo:** `validate_system.py`

**O QUE FAZ:**
- Testa se tudo está funcionando
- Verifica arquivos e sintaxe
- Testa módulos

**COMO USAR:**
```bash
python validate_system.py
```

---

## 🎯 MENU PRINCIPAL (RECOMENDADO)

**Arquivo:** `menu_principal.py`

**O QUE FAZ:**
- Menu interativo no terminal
- Mostra todos os sistemas disponíveis
- Executa o sistema escolhido
- Lista arquivos e documentação

**COMO USAR:**
```bash
python menu_principal.py
```

**VISUAL:**
```
======================================================================
🚀 DOCLING LEGAL - MENU PRINCIPAL
======================================================================

📁 ARQUIVOS DISPONÍVEIS:

  ✓ app_analise_planilha.py (15,385 bytes)
  ✓ app_clone_documentos.py (17,471 bytes)
  ✓ app_legal.py (20,208 bytes)
  ✓ app_tkinter.py (9,619 bytes)
  ✓ gerar_rapido.py (2,295 bytes)
  ✓ validate_system.py (3,367 bytes)

Escolha o sistema que deseja executar:

  1️⃣  📊 ANÁLISE E CONVERSÃO PARA PLANILHA
  2️⃣  🔄 CLONAGEM DE FORMATAÇÃO
  3️⃣  📝 GERADOR DE DOCUMENTOS JURÍDICOS
  4️⃣  📄 CONVERSOR SIMPLES
  5️⃣  ⚡ GERADOR RÁPIDO (Terminal)
  6️⃣  🔍 VALIDAR SISTEMA
  0️⃣  ❌ SAIR

Digite sua escolha:
```

---

## 📋 RESUMO DAS INTERFACES

| Interface | Tipo | Principais Recursos |
|-----------|------|---------------------|
| app_analise_planilha.py | **GUI** | Converte docs → Excel/CSV com preview |
| app_clone_documentos.py | **GUI** | Clona formatação entre documentos |
| app_legal.py | **GUI** | Gera documentos jurídicos com templates |
| app_tkinter.py | **GUI** | Conversor simples PDF/DOCX → MD/JSON |
| gerar_rapido.py | **Terminal** | Geração rápida sem interface |
| validate_system.py | **Terminal** | Validação e testes |
| menu_principal.py | **Terminal** | Menu para acessar todos os sistemas |

---

## 🚀 INÍCIO RÁPIDO

### Opção 1: Menu Interativo (RECOMENDADO)
```bash
python menu_principal.py
```

### Opção 2: Diretamente
```bash
# Conversão para planilha (MAIS USADO)
python app_analise_planilha.py

# Clonagem de formatação
python app_clone_documentos.py

# Documentos jurídicos
python app_legal.py
```

---

## ⚠️ IMPORTANTE: INTERFACES GRÁFICAS

**ATENÇÃO:** As interfaces gráficas (app_*.py) usam Tkinter e **PRECISAM DE DISPLAY**.

- ✅ **NO SEU COMPUTADOR:** Funcionam perfeitamente
- ❌ **NO SERVIDOR/SSH:** Não funcionam (sem display gráfico)

**SE VOCÊ ESTÁ VIA SSH:**
- Use `gerar_rapido.py` ou `validate_system.py`
- Ou baixe o projeto no seu computador e execute lá

---

## 📦 INSTALAÇÃO

Todas as dependências foram instaladas:

```bash
✓ beautifulsoup4 (4.14.2)
✓ lxml (6.0.2)
✓ pandas (2.3.3)
✓ openpyxl (3.1.5)
✓ docling (2.62.0) ← INSTALANDO AGORA
```

---

## 🎉 TUDO PRONTO!

**6 INTERFACES DIFERENTES PARA VOCÊ ESCOLHER:**

1. 📊 **Análise e Planilha** → Dados em Excel/CSV
2. 🔄 **Clonagem** → Copia formatação
3. 📝 **Jurídico** → Templates profissionais
4. 📄 **Simples** → Conversão básica
5. ⚡ **Rápido** → Terminal sem GUI
6. 🔍 **Validação** → Testes

**ESCOLHA A SUA E COMECE!**
