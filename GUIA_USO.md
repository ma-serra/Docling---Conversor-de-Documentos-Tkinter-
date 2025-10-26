# 🎯 Guia Rápido de Uso - Docling Legal

## 🚀 Iniciando o Sistema

### 1. Abra o terminal no diretório do projeto

### 2. Execute a aplicação:
```bash
python app_legal.py
```

### 3. A janela principal abrirá com 3 abas:
- 📄 **Conversor de Documentos**
- 📝 **Gerador de Documentos**
- ⚖️ **Diagnóstico Jurídico** (em desenvolvimento)

---

## 📄 ABA 1: Conversor de Documentos

### Como Usar:
1. Clique em **"Browse"**
2. Selecione um arquivo (PDF, DOCX, TXT, etc.)
3. Escolha o formato de saída:
   - ⚪ Markdown
   - ⚪ JSON
4. Clique em **"Converter Documento"**
5. Aguarde a conversão
6. O resultado aparecerá na área de texto
7. Clique em **"Salvar Documento Convertido"** para salvar

### Formatos Suportados:
- PDF (`.pdf`)
- Word (`.docx`)
- Texto (`.txt`)
- Markdown (`.md`)
- HTML (`.html`)
- RTF (`.rtf`)

---

## 📝 ABA 2: Gerador de Documentos (PRINCIPAL)

### Como Gerar um Documento:

#### **Passo 1: Selecionar Template**
No dropdown, você verá:
- Confissão de Dívida (21 campos)
- Guia Rápido para Moradores (0 campos)

Selecione **"Confissão de Dívida"**

#### **Passo 2: Carregar Template**
Clique no botão **"Carregar Template"**

Aparecerão 21 campos para preencher:

```
┌─────────────────────────────────────────┐
│ Credor Nome:        [EMPRESA XYZ LTDA  ]│
│ Credor Cnpj:        [12.345.678/0001-90]│
│ Credor Endereco:    [Rua Exemplo, 123  ]│
│ Credor Representante: [João da Silva   ]│
│ Credor Rg:          [12.345.678-9 SSP  ]│
│ Credor Cpf:         [123.456.789-00    ]│
│                                          │
│ Devedor Nome:       [MARIA DOS SANTOS  ]│
│ Devedor Rg:         [98.765.432-1 SSP  ]│
│ Devedor Cpf:        [987.654.321-00    ]│
│ Devedor Endereco:   [Avenida Exemplo   ]│
│                                          │
│ Valor Total:        [R$ 150.000,00     ]│
│ Motivo Divida:      [prestação de serv.]│
│ Num Parcelas:       [12 (doze)         ]│
│ Valor Parcela:      [R$ 12.250,00      ]│
│ Data Primeira Parcela: [15/02/2025     ]│
│                                          │
│ Juros Mora:         [2% ao mês         ]│
│ Multa Atraso:       [2%                ]│
│ Dados Bancarios:    [Banco Exemplo     ]│
│ Foro:               [São Paulo/SP      ]│
│ Cidade:             [São Paulo/SP      ]│
│ Data Assinatura:    [17/10/2025        ]│
└─────────────────────────────────────────┘
```

#### **Passo 3: Preencher os Campos**
- Você pode editar qualquer campo
- Os valores padrão já estão preenchidos como exemplo
- Adapte para seu caso específico

**Exemplos de Preenchimento:**

**DADOS DO CREDOR:**
```
Credor Nome: ESCRITÓRIO ADVOCACIA SILVA & SOUZA
Credor Cnpj: 12.345.678/0001-90
Credor Endereco: Rua das Flores, 500, Sala 101, Centro, São Paulo/SP, CEP 01234-567
Credor Representante: Dr. José Silva
Credor Rg: 12.345.678-9 SSP/SP
Credor Cpf: 123.456.789-00
```

**DADOS DO DEVEDOR:**
```
Devedor Nome: MARIA SANTOS OLIVEIRA
Devedor Rg: 98.765.432-1 SSP/SP
Devedor Cpf: 987.654.321-00
Devedor Endereco: Av. Paulista, 1000, Apto 52, Bela Vista, São Paulo/SP, CEP 01310-100
```

**VALORES:**
```
Valor Total: R$ 50.000,00 (cinquenta mil reais)
Motivo Divida: prestação de serviços jurídicos realizados entre janeiro e junho de 2024
Num Parcelas: 10 (dez)
Valor Parcela: R$ 5.000,00 (cinco mil reais)
Data Primeira Parcela: 15 de março de 2025
```

**CONDIÇÕES:**
```
Juros Mora: 1% ao mês
Multa Atraso: 2%
Dados Bancarios: Banco do Brasil, Agência 1234-5, Conta Corrente 12345-6
Foro: São Paulo/SP
Cidade: São Paulo/SP
Data Assinatura: 26 de outubro de 2025
```

#### **Passo 4: Visualizar o Documento**
Clique em **"Visualizar Documento"**

- O navegador abrirá automaticamente
- Você verá o documento formatado profissionalmente
- Verifique se todos os dados estão corretos

#### **Passo 5: Gerar e Salvar**
Se estiver tudo OK:

1. Clique em **"Gerar e Salvar"**
2. Escolha onde salvar
3. Escolha o formato:
   - `.html` - Documento completo com formatação
   - `.md` - Texto em Markdown (sem estilos)
4. Clique em **"Salvar"**

### ⚠️ Validações Automáticas

O sistema valida automaticamente:

❌ **CPF inválido:**
```
CPF: 12345678900  ← ERRO!
CPF: 123.456.789-00  ← CORRETO!
```

❌ **CNPJ inválido:**
```
CNPJ: 12345678000190  ← ERRO!
CNPJ: 12.345.678/0001-90  ← CORRETO!
```

❌ **Data inválida:**
```
Data: 15-02-2025  ← ERRO!
Data: 15/02/2025  ← CORRETO!
```

Se houver erros, uma mensagem aparecerá:
```
┌─────────────────────────────────┐
│ ❌ Erros de Validação           │
├─────────────────────────────────┤
│ • credor_cpf: Formato de CPF    │
│   inválido (esperado:           │
│   000.000.000-00)               │
│                                 │
│ • data_assinatura: Formato de   │
│   data inválido (esperado:      │
│   DD/MM/AAAA)                   │
└─────────────────────────────────┘
```

---

## 🌐 Visualizando o Guia do Morador

### Como Abrir:

**Opção 1: Pelo Sistema**
1. Vá para **"Gerador de Documentos"**
2. Selecione **"Guia Rápido para Moradores"**
3. Clique em **"Carregar Template"**
4. Clique em **"Visualizar Documento"**

**Opção 2: Diretamente no Navegador**
1. Abra o navegador
2. Pressione `Ctrl + O` (Abrir arquivo)
3. Navegue até: `templates/guia_morador.html`
4. Abra o arquivo

### Usando o Assistente Virtual (Gemini)

⚠️ **IMPORTANTE:** Para usar o assistente com IA, você precisa:

1. Abrir o arquivo `templates/guia_morador.html`
2. Procurar pela linha:
```javascript
const apiKey = "{{GEMINI_API_KEY}}";
```
3. Substituir por sua chave real:
```javascript
const apiKey = "SUA_CHAVE_AQUI";
```

**Como obter a chave do Gemini:**
1. Acesse: https://makersuite.google.com/app/apikey
2. Crie uma chave API
3. Copie e cole no arquivo

**Testando o Assistente:**
```
Pergunta: "Posso ter animais de estimação?"
Resposta: O assistente vai verificar as regras do guia
         e responder com base no conteúdo.
```

---

## 📊 Exemplo Completo de Uso

### Cenário: Gerar Confissão de Dívida Real

**1. Execute:**
```bash
python app_legal.py
```

**2. Vá para:** Aba "📝 Gerador de Documentos"

**3. Selecione:** "Confissão de Dívida (21 campos)"

**4. Clique:** "Carregar Template"

**5. Preencha os dados reais:**
```
CREDOR:
- Nome: MEU ESCRITÓRIO LTDA
- CNPJ: 01.234.567/0001-89
- Endereço: Rua Comercial, 100, São Paulo/SP
- etc...

DEVEDOR:
- Nome: CLIENTE DEVEDOR
- CPF: 111.222.333-44
- etc...

VALORES:
- Total: R$ 30.000,00
- Parcelas: 6
- etc...
```

**6. Clique:** "Visualizar Documento"
- Navegador abre com o documento

**7. Revise tudo**

**8. Clique:** "Gerar e Salvar"
- Escolha: `confissao_divida_cliente.html`

**9. Pronto!** Documento salvo e pronto para impressão/assinatura

---

## 🎨 Personalizando Templates

### Editando um Template Existente:

1. Abra o arquivo: `templates/confissao_divida.html`
2. Procure por `data-field="nome_do_campo"`
3. Edite o conteúdo ou estilos CSS
4. Salve
5. Recarregue o template no sistema

### Criando um Novo Template:

1. Crie um arquivo HTML em `templates/`
2. Adicione `data-field` aos campos variáveis:
```html
<span class="campo-variavel" data-field="nome_cliente">
    João Silva
</span>
```
3. Adicione ao `templates_config.json`:
```json
{
    "id": "meu_template",
    "name": "meu_template.html",
    "title": "Meu Template",
    "category": "Contratos"
}
```
4. Reinicie o sistema

---

## 🐛 Problemas Comuns

### Erro: "No module named 'bs4'"
**Solução:**
```bash
pip install beautifulsoup4 lxml
```

### Erro: "No module named 'docling'"
**Solução:**
```bash
pip install docling
```

### Janela não abre
**Solução:**
```bash
# Verifique se está no diretório correto
pwd

# Execute novamente
python app_legal.py
```

### Campos não aparecem
**Solução:**
1. Verifique se clicou em "Carregar Template"
2. Verifique se selecionou um template no dropdown
3. Verifique se o arquivo HTML tem campos `data-field`

---

## 📱 Atalhos Úteis

| Ação | Atalho |
|------|--------|
| Abrir arquivo | `Ctrl + O` |
| Salvar | `Ctrl + S` |
| Copiar texto | `Ctrl + C` |
| Colar texto | `Ctrl + V` |
| Fechar janela | `Alt + F4` |

---

## ✅ Checklist de Uso Rápido

Para gerar um documento:
- [ ] Abrir `app_legal.py`
- [ ] Ir para aba "Gerador de Documentos"
- [ ] Selecionar template
- [ ] Clicar "Carregar Template"
- [ ] Preencher todos os campos
- [ ] Clicar "Visualizar Documento"
- [ ] Revisar no navegador
- [ ] Clicar "Gerar e Salvar"
- [ ] Escolher local e formato
- [ ] Salvar

---

## 🎯 Próximos Passos

Depois de dominar o básico:
1. Experimente criar seus próprios templates
2. Personalize os estilos CSS
3. Adicione novos tipos de documentos
4. Integre com sistemas de assinatura digital

---

## 💡 Dicas Profissionais

1. **Sempre faça backup** dos templates originais antes de editar
2. **Use o preview** antes de gerar o documento final
3. **Valide os dados** antes de salvar (o sistema ajuda, mas confira!)
4. **Salve em HTML** se quiser manter a formatação completa
5. **Salve em Markdown** se for usar em outros sistemas

---

**Dúvidas?** Consulte o `README_LEGAL.md` para documentação completa!
