# Docling - Conversor de Documentos (Tkinter)

![Docling](DOCLING.png)

Esta aplicação Tkinter permite converter documentos para formato Markdown ou JSON utilizando a biblioteca `docling`.

## Funcionalidades

- Converter documentos PDF, DOCX, TXT, MD, HTML e RTF para Markdown ou JSON.
- Mostrar a informação do documento convertido na interface.
- Salvar o documento convertido em um arquivo.

## Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/ma-serra/Docling---Conversor-de-Documentos-Tkinter-.git
cd Docling---Conversor-de-Documentos-Tkinter-
```

### 2. Crie um ambiente virtual (recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install docling Pillow
```

## Como Executar

Execute o arquivo principal:
```bash
python app_tkinter.py
```

## Como Usar

1. Execute o arquivo `app_tkinter.py`
2. Clique em "Procurar" para selecionar o arquivo que deseja converter
3. Selecione o formato de saída (Markdown ou JSON)
4. Clique em "Converter Documento" para iniciar a conversão
5. Após a conversão, clique em "Salvar Documento Convertido" para salvar o resultado

## Empacotar como Executável

Para criar um executável (.exe no Windows):

```bash
# Instale o PyInstaller
pip install pyinstaller

# Crie o executável
pyinstaller --onefile --windowed --add-data "DOCLING.png:." app_tkinter.py
```

O executável será criado na pasta `dist/`.

## Dependências

- Python 3.8+
- docling
- Pillow
- tkinter (incluído no Python)
