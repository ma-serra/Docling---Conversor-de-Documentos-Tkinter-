# Instruções para Empacotar o Aplicativo

## Pré-requisitos

1. Python 3.11 ou superior instalado
2. Todas as dependências instaladas

## Passo 1: Instalar Dependências

```bash
pip install -r requirements.txt
pip install pyinstaller
```

## Passo 2: Criar Executável

### Opção 1: Usar o script automatizado (Recomendado)

```bash
python build_app.py
```

### Opção 2: Usar PyInstaller diretamente

```bash
pyinstaller --name DoclingConverter --onefile --windowed --clean --noconfirm app_tkinter.py
```

## Passo 3: Localizar o Executável

Após o build, o executável estará localizado em:
- `dist/DoclingConverter` (Linux/Mac)
- `dist/DoclingConverter.exe` (Windows)

## Opções do PyInstaller Explicadas

- `--onefile`: Cria um único arquivo executável (mais fácil de distribuir)
- `--windowed`: Não mostra a janela do console (apenas a GUI)
- `--clean`: Limpa o cache antes de buildar
- `--noconfirm`: Sobrescreve arquivos existentes sem perguntar

## Testando o Executável

1. Navegue até a pasta `dist/`
2. Execute o arquivo `DoclingConverter` (ou `DoclingConverter.exe` no Windows)
3. A interface gráfica deverá abrir automaticamente

## Distribuição

Você pode distribuir o executável criado (`dist/DoclingConverter`) para qualquer pessoa!
O arquivo é standalone e não requer Python instalado para funcionar.

## Troubleshooting

### Erro: "Failed to execute script"
- Verifique se todas as dependências estão instaladas
- Tente rebuildar com `--onedir` em vez de `--onefile`

### Executável muito grande
- O executável pode ficar grande (100-500MB) devido às bibliotecas incluídas
- Isso é normal para aplicações Python empacotadas

### Erro ao abrir PDFs
- Certifique-se de que os arquivos PDF não estão corrompidos
- Verifique se você tem permissões de leitura no arquivo
