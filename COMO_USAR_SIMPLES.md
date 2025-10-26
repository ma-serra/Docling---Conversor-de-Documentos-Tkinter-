# 🚀 COMO USAR - SUPER SIMPLES

## ✅ O Sistema FUNCIONA - Testado e Aprovado

---

## 3 FORMAS DE USAR

### 1️⃣ FORMA MAIS RÁPIDA (1 comando)

Gera documento já pronto com dados de exemplo:

```bash
python gerar_rapido.py
```

**Resultado:**
- Cria `output_examples/confissao_divida_gerada.html`
- Documento pronto para abrir no navegador
- Dados já preenchidos (você pode editar no código)

---

### 2️⃣ FORMA INTERATIVA (Terminal)

Preenche campos um por um no terminal:

```bash
python gerar_documento.py
```

**Como funciona:**
1. Escolhe o template
2. Preenche cada campo
3. Gera o documento

---

### 3️⃣ FORMA GRÁFICA (Interface)

Abre janela com formulário:

```bash
python app_legal.py
```

**Requer:** Interface gráfica (Windows/Mac/Linux com GUI)

---

## 🎯 TESTE AGORA

**Cole isto no terminal:**

```bash
# Testar se funciona
python gerar_rapido.py

# Ver o resultado
ls -lh output_examples/confissao_divida_gerada.html
```

**Deve aparecer:**
```
✅ DOCUMENTO GERADO COM SUCESSO!
📄 output_examples/confissao_divida_gerada.html
```

---

## 📝 PERSONALIZAR SEUS DADOS

### Editar gerar_rapido.py

Abra o arquivo `gerar_rapido.py` e edite os dados:

```python
dados = {
    "credor_nome": "SEU NOME AQUI",
    "credor_cnpj": "00.000.000/0001-00",
    # ... edite o que quiser
}
```

Salve e execute de novo:
```bash
python gerar_rapido.py
```

---

## 🌐 VER O DOCUMENTO

**Abrir no navegador:**

```bash
# Mac/Linux
open output_examples/confissao_divida_gerada.html

# Windows
start output_examples/confissao_divida_gerada.html

# Ou clique duas vezes no arquivo
```

---

## ✅ PRONTO!

**3 scripts criados:**
- `gerar_rapido.py` ← Mais rápido
- `gerar_documento.py` ← Interativo
- `app_legal.py` ← Interface gráfica

**Todos funcionam!** Escolha o que preferir.

---

## 🔧 Problemas?

**Erro "No module":**
```bash
pip install beautifulsoup4 lxml
```

**Não tem Python:**
```bash
# Baixe em: https://www.python.org/downloads/
```

**Não acha os arquivos:**
```bash
# Liste:
ls *.py

# Deve mostrar:
# gerar_rapido.py
# gerar_documento.py
# app_legal.py
```

---

## 📊 COMPARAÇÃO

| Script | Velocidade | Facilidade | Interface |
|--------|------------|------------|-----------|
| `gerar_rapido.py` | ⚡⚡⚡ | ⭐⭐⭐ | Terminal |
| `gerar_documento.py` | ⚡⚡ | ⭐⭐ | Terminal |
| `app_legal.py` | ⚡ | ⭐⭐⭐ | Janela |

---

**🎉 Sistema 100% funcional - Escolha sua forma preferida!**
