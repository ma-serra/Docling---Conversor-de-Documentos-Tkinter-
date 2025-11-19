# Docling Document Converter - Guia Completo

![Docling](DOCLING.png)

## Descrição

Aplicação desktop moderna desenvolvida em Python com interface Tkinter para converter documentos PDF, DOCX, TXT, MD, HTML e RTF para formatos Markdown ou JSON utilizando a poderosa biblioteca `docling`.

## Características

- Interface gráfica moderna com tema escuro
- Conversão de múltiplos formatos de documento
- Suporte para exportação em Markdown e JSON
- Visualização de metadata do documento
- Barra de progresso para acompanhamento
- Design responsivo e intuitivo

## Requisitos

- Python 3.11 ou superior
- Sistema operacional: Windows, Linux ou macOS

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/Docling---Conversor-de-Documentos-Tkinter-.git
cd Docling---Conversor-de-Documentos-Tkinter-
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

Principais dependências:
- `docling` - Biblioteca para conversão de documentos
- `tkinter` - Interface gráfica (geralmente já vem com Python)
- `PyInstaller` - Para criar executáveis (opcional)

## Como Usar

### Executar a Aplicação

```bash
python app_tkinter.py
```

### Passos no Aplicativo

1. **Selecionar Arquivo**: Clique no botão "Browse" para escolher o documento que deseja converter
2. **Escolher Formato**: Selecione entre "Markdown" ou "JSON" como formato de saída
3. **Converter**: Clique em "Convert Document" para iniciar a conversão
4. **Visualizar**: O documento convertido aparecerá no painel de resultados
5. **Salvar**: Use o botão "Save Converted Document" para salvar o arquivo convertido

## Formatos Suportados

### Entrada (Input)
- PDF (.pdf)
- Word (.docx)
- Texto (.txt)
- Markdown (.md)
- HTML (.html)
- Rich Text Format (.rtf)

### Saída (Output)
- Markdown (.md)
- JSON (.json)

## Criar Executável

Para criar um arquivo executável independente que pode ser distribuído:

### Método 1: Script Automatizado (Recomendado)

```bash
python build_app.py
```

### Método 2: PyInstaller Manual

```bash
pyinstaller --name DoclingConverter --onefile --windowed --clean --noconfirm app_tkinter.py
```

O executável será criado na pasta `dist/`:
- **Windows**: `dist/DoclingConverter.exe`
- **Linux/Mac**: `dist/DoclingConverter`

## Estrutura do Projeto

```
Docling---Conversor-de-Documentos-Tkinter-/
│
├── app_tkinter.py              # Aplicação principal
├── build_app.py                # Script de build
├── requirements.txt            # Dependências Python
├── INSTRUCOES_BUILD.md         # Instruções de build
├── README.md                   # Documentação original
├── README_COMPLETO.md          # Este arquivo
├── DOCLING.png                 # Logo do aplicativo
│
└── dist/                       # Pasta gerada com executável (após build)
    └── DoclingConverter        # Executável final
```

## Tecnologias Utilizadas

- **Python 3.11** - Linguagem de programação
- **Tkinter** - Framework para interface gráfica
- **Docling** - Motor de conversão de documentos
- **PyInstaller** - Empacotamento de executáveis

## Características Técnicas

### Interface
- Tema escuro moderno
- Painel duplo (controles + resultados)
- Barra de progresso animada
- Visualização de metadata

### Performance
- Conversão em thread separada (não trava a interface)
- Progress feedback em tempo real
- Tratamento de erros robusto

## Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'docling'"
Solução: Instale as dependências com `pip install -r requirements.txt`

### Erro: "tkinter is not available"
Solução (Ubuntu/Debian):
```bash
sudo apt-get install python3-tk
```

Solução (macOS):
```bash
brew install python-tk
```

### Executável não abre no Windows
- Verifique se o antivírus não está bloqueando
- Execute como administrador
- Reconstrua o executável no Windows

### Conversão falha para arquivos grandes
- A conversão de PDFs muito grandes pode demorar
- Aguarde o processo concluir
- Verifique a memória disponível no sistema

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## Suporte

Para reportar bugs ou solicitar features, abra uma issue no GitHub.

## Autor

Desenvolvido com ❤️ utilizando Python e Docling

## Changelog

### v1.0.0 (2025)
- Lançamento inicial
- Interface Tkinter moderna
- Suporte para PDF, DOCX, TXT, MD, HTML, RTF
- Exportação para Markdown e JSON
- Sistema de empacotamento com PyInstaller

---

**Docling Document Converter** - Transformando seus documentos de forma simples e elegante
