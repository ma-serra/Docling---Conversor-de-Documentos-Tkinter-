# Docling Legal - Sistema Integrado de Documentos Jurídicos

![Docling](DOCLING.png)

Sistema completo para conversão, geração e análise de documentos jurídicos, desenvolvido com **Tkinter** e **Docling**.

## Funcionalidades

### 1. Conversor de Documentos
- Converte PDF, DOCX, TXT, MD, HTML, RTF para Markdown ou JSON
- Interface intuitiva com visualização em tempo real
- Exportação de documentos convertidos

### 2. Gerador de Documentos Jurídicos
- Sistema de templates HTML profissionais
- Preenchimento automático de campos variáveis
- Validação de dados (CPF, CNPJ, datas, emails)
- Exportação para HTML e Markdown
- Visualização em navegador antes de salvar

### 3. Diagnóstico Jurídico Condominial (Em Desenvolvimento)
- Análise automática de convenções e regimentos
- Identificação de não conformidades
- Geração de relatórios técnicos
- Base legal: Lei 4.591/64, CC art. 1.331+

## Templates Disponíveis

### Confissão de Dívida
Template profissional de confissão de dívida com:
- Qualificação completa das partes
- Discriminação de valores
- Cronograma de pagamento
- Cláusulas legais padronizadas

**Campos:** 15+ campos variáveis
**Base Legal:** CC Lei 10.406/2002, CPC Lei 13.105/2015

### Guia do Morador
Guia interativo com regras condominiais:
- Interface moderna e responsiva
- Seções organizadas por categoria
- Assistente virtual com IA (Gemini)
- Extração automática de contexto

**Campos:** Editáveis via HTML
**Base Legal:** Lei 4.591/1964, CC art. 1.331+

## Instalação

### Requisitos
- Python 3.8+
- Tkinter (geralmente incluído no Python)

### Passo 1: Clonar o repositório
```bash
git clone https://github.com/seu-usuario/Docling-Legal.git
cd Docling-Legal
```

### Passo 2: Instalar dependências
```bash
pip install -r requirements.txt
```

### Passo 3: Executar a aplicação

**Versão Completa (Recomendada):**
```bash
python app_legal.py
```

**Versão Original (Apenas Conversor):**
```bash
python app_tkinter.py
```

## Uso

### Conversor de Documentos

1. Acesse a aba **"📄 Conversor de Documentos"**
2. Clique em **"Browse"** e selecione o arquivo
3. Escolha o formato de saída (Markdown ou JSON)
4. Clique em **"Converter Documento"**
5. Salve o resultado usando **"Salvar Documento Convertido"**

### Gerador de Documentos

1. Acesse a aba **"📝 Gerador de Documentos"**
2. Selecione um template no dropdown
3. Clique em **"Carregar Template"**
4. Preencha todos os campos obrigatórios
5. Clique em **"Visualizar Documento"** para preview no navegador
6. Clique em **"Gerar e Salvar"** para salvar o documento final

### Validações Automáticas

O sistema valida automaticamente:
- **CPF:** formato 000.000.000-00
- **CNPJ:** formato 00.000.000/0000-00
- **Datas:** formato DD/MM/AAAA
- **Emails:** formato padrão
- **Campos obrigatórios:** não podem estar vazios

## Estrutura do Projeto

```
Docling-Legal/
├── app_tkinter.py              # App original (conversor)
├── app_legal.py                # App completo com todas funcionalidades
├── template_manager.py         # Gerenciador de templates
├── requirements.txt            # Dependências Python
├── README.md                   # Documentação original
├── README_LEGAL.md            # Documentação completa (este arquivo)
│
├── templates/                  # Templates de documentos
│   ├── confissao_divida.html  # Template de confissão de dívida
│   ├── guia_morador.html      # Guia interativo do morador
│   └── templates_config.json  # Configuração dos templates
│
└── DOCLING.png                # Logo do projeto
```

## Criando Novos Templates

### Passo 1: Criar arquivo HTML

Crie um arquivo HTML com estrutura padrão e adicione `data-field` aos campos variáveis:

```html
<span class="campo-variavel" data-field="nome_cliente">João Silva</span>
<span class="campo-variavel" data-field="cpf_cliente">000.000.000-00</span>
```

### Passo 2: Adicionar ao templates_config.json

```json
{
    "id": "meu_template",
    "name": "meu_template.html",
    "title": "Meu Template",
    "category": "Contratos",
    "description": "Descrição do template",
    "icon": "📄",
    "tags": ["contrato", "custom"],
    "base_legal": "Lei aplicável"
}
```

### Passo 3: Reiniciar a aplicação

O novo template aparecerá automaticamente na lista.

## API do Template Manager

### Carregar templates
```python
from template_manager import TemplateManager

manager = TemplateManager()
templates = manager.get_available_templates()
```

### Preencher template
```python
data = {
    "nome_cliente": "João Silva",
    "cpf_cliente": "123.456.789-00"
}

filled_html = manager.fill_template("meu_template.html", data)
manager.save_filled_template(filled_html, "output.html")
```

### Validar dados
```python
errors = manager.validate_data("meu_template.html", data)
if errors:
    print("Erros encontrados:", errors)
```

### Exportar para Markdown
```python
markdown = manager.export_to_markdown(filled_html)
```

## Exportação para PDF (Opcional)

Para habilitar exportação para PDF:

1. Descomente no `requirements.txt`:
```
weasyprint
```

2. Instale:
```bash
pip install weasyprint
```

3. Use no código:
```python
from template_manager import html_to_pdf

html_to_pdf(filled_html, "output.pdf")
```

## Tecnologias Utilizadas

- **Python 3.8+**
- **Tkinter** - Interface gráfica
- **Docling** - Conversão de documentos
- **BeautifulSoup4** - Parsing e manipulação de HTML
- **lxml** - Parser XML/HTML
- **WeasyPrint** (opcional) - Exportação para PDF

## Roadmap

### Em Desenvolvimento
- [x] Sistema de templates com campos variáveis
- [x] Validação automática de dados
- [x] Exportação HTML e Markdown
- [ ] Exportação para PDF integrada
- [ ] Mais templates jurídicos

### Planejado
- [ ] Diagnóstico Jurídico Condominial completo
- [ ] Integração com APIs de IA (GPT/Gemini)
- [ ] Base de dados de jurisprudência
- [ ] Sistema de versionamento de documentos
- [ ] Assinatura digital

## Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Avisos Legais

Este software é fornecido "como está", sem garantias de qualquer tipo. Os templates fornecidos são exemplos e devem ser revisados por profissionais qualificados antes de uso em contextos reais.

**Importante:** Este sistema não substitui assessoria jurídica profissional. Sempre consulte um advogado antes de utilizar documentos gerados por este sistema.

## Suporte

- Reporte bugs: [GitHub Issues](https://github.com/seu-usuario/Docling-Legal/issues)
- Documentação: Este README
- Email: seu-email@exemplo.com

## Autores

- Desenvolvimento inicial baseado no projeto Docling Converter
- Expansão para sistema jurídico: 2025

---

**Docling Legal** - Automatizando o direito, um documento por vez.
