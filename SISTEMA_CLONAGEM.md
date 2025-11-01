# 🔄 Sistema de Clonagem de Formatação de Documentos

## ✅ O QUE ESTE SISTEMA FAZ

**CLONA A FORMATAÇÃO** de documentos existentes e permite **REUTILIZAR** o layout em novos documentos.

---

## 🎯 FUNCIONALIDADES PRINCIPAIS

### 1️⃣ **Análise de Documentos**
- Carrega PDF, DOCX, HTML, TXT
- Extrai estrutura e formatação
- Identifica elementos (títulos, parágrafos, tabelas, listas)
- Detecta estilos (fontes, cores, tamanhos)

### 2️⃣ **Clonagem de Formatação**
- Cria template baseado no documento original
- Mantém a estrutura de layout
- Preserva hierarquia de elementos

### 3️⃣ **Editor de Conteúdo**
- Interface dividida em duas colunas
- Esquerda: Documento original
- Direita: Template editável
- Seleciona texto e envia para campos

### 4️⃣ **Replicação**
- Aplica formatação a novos conteúdos
- Exporta em múltiplos formatos
- Mantém layout original

---

## 🚀 COMO USAR

### **Interface Principal**

```
┌─────────────────────────────────────────────────────────────┐
│  🔄 Sistema de Clonagem de Documentos                        │
├─────────────────────────────────────────────────────────────┤
│  [📂 Carregar] [🔍 Analisar] [⚡ Auto] [💾 Exportar]       │
├──────────────────────┬──────────────────────────────────────┤
│  📄 DOCUMENTO        │  📝 TEMPLATE / EDITOR                │
│                      │                                      │
│  [Texto extraído]    │  Campo 1: [__________]              │
│  do documento        │  Campo 2: [__________]              │
│  original            │  Campo 3: [__________]              │
│                      │  ...                                │
│  Selecione texto → ➡️│                                     │
│                      │  ← Texto vai para campo selecionado │
└──────────────────────┴──────────────────────────────────────┘
```

---

## 📋 PASSO A PASSO

### **1. Carregar Documento**
```bash
# Execute o sistema
python app_clone_documentos.py

# Clique em "📂 Carregar Documento"
# Escolha: PDF, DOCX, HTML, TXT
```

**O documento aparecerá no painel esquerdo**

---

### **2. Analisar Estrutura**
```bash
# Clique em "🔍 Analisar"
```

**O que acontece:**
- Sistema analisa estrutura do documento
- Identifica elementos (títulos, parágrafos, etc.)
- Cria campos editáveis no painel direito
- Mostra número de campos detectados

**Resultado:**
```
Análise concluída: 20 campos detectados
```

---

### **3. Preencher Campos**

**Forma Manual (Selecionar e Enviar):**
1. Selecione texto no documento (esquerda)
2. Clique no campo desejado (direita)
3. Clique em "➡️ Enviar Seleção para Campo"
4. Texto é copiado para o campo

**Forma Automática:**
1. Clique em "⚡ Preencher Auto"
2. Sistema tenta preencher baseado em padrões
3. (Em desenvolvimento: usa regex e ML)

---

### **4. Exportar Documento**
```bash
# Clique em "💾 Exportar"
# Escolha formato: HTML, JSON, Markdown
# Salve o arquivo
```

**Formatos disponíveis:**
- **HTML**: Com formatação completa
- **JSON**: Dados estruturados
- **Markdown**: Texto formatado

---

## 🔧 FUNCIONALIDADES TÉCNICAS

### **Análise de Documento**

```python
from document_analyzer import DocumentAnalyzer

analyzer = DocumentAnalyzer()

# Analisar documento
analysis = analyzer.analyze_document("meu_documento.pdf")

# Ver estrutura
print(f"Título: {analysis['title']}")
print(f"Seções: {len(analysis['sections'])}")
print(f"Elementos: {len(analysis['elements'])}")

# Criar template
template = analyzer.create_template_from_analysis(analysis)

# Salvar template
analyzer.export_template(template, "template.json")
```

---

## 📊 O QUE É EXTRAÍDO

### **Estrutura:**
- ✅ Títulos (H1, H2, H3, etc.)
- ✅ Parágrafos
- ✅ Listas (ordenadas e não ordenadas)
- ✅ Tabelas (estrutura)
- ✅ Seções e divisões

### **Formatação:**
- ✅ Fontes utilizadas
- ✅ Cores (texto e fundo)
- ✅ Tamanhos de fonte
- ✅ Estilos inline
- ✅ Classes CSS

### **Layout:**
- ✅ Número de colunas
- ✅ Grid/Flexbox detection
- ✅ Hierarquia de elementos

---

## 💡 CASOS DE USO

### **1. Replicar Contratos**
- Carrega contrato existente
- Analisa estrutura
- Reutiliza layout para novos contratos

### **2. Padronizar Documentos**
- Carrega documento modelo
- Extrai formatação
- Aplica em documentos variados

### **3. Migração de Formatos**
- Carrega documento antigo
- Preserva formatação
- Exporta em formato moderno

### **4. Templates Personalizados**
- Carrega documento desejado
- Cria template editável
- Reutiliza infinitas vezes

---

## 📁 ARQUIVOS CRIADOS

```
app_clone_documentos.py      ← Interface principal
document_analyzer.py          ← Motor de análise
templates/
└── *_template.json          ← Templates gerados
```

---

## 🎮 EXEMPLO PRÁTICO

```bash
# 1. Execute
python app_clone_documentos.py

# 2. Carregue um documento
# Clique: 📂 Carregar → Escolha: contrato.pdf

# 3. Analise
# Clique: 🔍 Analisar
# Resultado: "Análise concluída: 15 campos detectados"

# 4. Edite campos
# Clique nos campos e modifique o conteúdo

# 5. Exporte
# Clique: 💾 Exportar → Escolha formato → Salve
```

---

## ⚙️ REQUISITOS

```bash
# Instalar dependências
pip install beautifulsoup4 lxml

# Opcional (para PDF):
pip install docling
```

---

## 🔍 ANÁLISE SUPORTADA

| Formato | Análise | Extração | Template |
|---------|---------|----------|----------|
| HTML | ✅ Completa | ✅ Total | ✅ Sim |
| PDF | ✅ Via Docling | ✅ Parcial | ✅ Sim |
| DOCX | ✅ Via Docling | ✅ Parcial | ✅ Sim |
| TXT | ✅ Básica | ✅ Texto | ✅ Sim |
| MD | ✅ Markdown | ✅ Total | ✅ Sim |

---

## 🎯 WORKFLOW COMPLETO

```
1. UPLOAD
   ↓
   Documento carregado

2. ANÁLISE
   ↓
   Estrutura extraída
   Formatação detectada
   Template criado

3. EDIÇÃO
   ↓
   Campos preenchidos
   Conteúdo personalizado

4. EXPORTAÇÃO
   ↓
   Documento novo com layout original
```

---

## 🆚 DIFERENÇA DOS OUTROS SISTEMAS

| Sistema | Função |
|---------|--------|
| `app_legal.py` | Templates **predefinidos** |
| `app_tkinter.py` | **Conversor** de formatos |
| `app_clone_documentos.py` | **Clona formatação** de qualquer documento |

---

## ✅ RESUMO

**O que este sistema faz:**
1. ✅ Carrega documento existente
2. ✅ Analisa estrutura e formatação
3. ✅ Cria template baseado no documento
4. ✅ Permite editar conteúdo
5. ✅ Exporta com layout replicado

**Diferencial:**
- Não precisa criar template do zero
- Usa documento existente como base
- Clone a formatação automaticamente
- Reutiliza layouts complexos

---

## 🚀 COMECE AGORA

```bash
python app_clone_documentos.py
```

**E comece a clonar formatação de documentos!** 🎉
