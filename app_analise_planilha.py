"""
Interface de Análise e Conversão para Planilha
Sistema completo com preview de dados tabulares
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import threading
from document_to_spreadsheet import DocumentToSpreadsheetConverter
import pandas as pd


class SpreadsheetAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📊 Análise e Conversão para Planilha")
        self.root.geometry("1600x900")
        self.root.minsize(1400, 700)

        # Converter
        self.converter = DocumentToSpreadsheetConverter()
        self.current_dataframes = []
        self.current_file = None

        # Configurar tema
        self.configure_theme()

        # Criar interface
        self.create_interface()

    def configure_theme(self):
        """Configura tema visual"""
        self.colors = {
            'bg_dark': '#1e1e1e',
            'bg_medium': '#252526',
            'bg_light': '#333333',
            'accent': '#0d7377',
            'accent_hover': '#0f8589',
            'text': '#ffffff',
            'text_dim': '#cccccc',
            'border': '#404040',
            'success': '#27ae60',
            'warning': '#f39c12',
            'danger': '#c0392b'
        }

        self.root.configure(bg=self.colors['bg_dark'])
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Estilos
        self.style.configure('Main.TFrame', background=self.colors['bg_dark'])
        self.style.configure('Card.TFrame', background=self.colors['bg_medium'])
        self.style.configure('Header.TLabel',
                             background=self.colors['bg_dark'],
                             foreground=self.colors['text'],
                             font=('Segoe UI', 18, 'bold'))
        self.style.configure('Info.TLabel',
                             background=self.colors['bg_medium'],
                             foreground=self.colors['text_dim'],
                             font=('Segoe UI', 9))
        self.style.configure('Primary.TButton',
                             background=self.colors['accent'],
                             foreground=self.colors['text'],
                             font=('Segoe UI', 10),
                             padding=8)

        # Treeview
        self.style.configure('Treeview',
                             background=self.colors['bg_light'],
                             foreground=self.colors['text'],
                             fieldbackground=self.colors['bg_light'],
                             borderwidth=0)
        self.style.configure('Treeview.Heading',
                             background=self.colors['bg_medium'],
                             foreground=self.colors['text'],
                             font=('Segoe UI', 10, 'bold'))

    def create_interface(self):
        """Cria interface principal"""
        # Frame principal
        main_frame = ttk.Frame(self.root, style='Main.TFrame', padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        self.create_header(main_frame)

        # Toolbar
        self.create_toolbar(main_frame)

        # Área de análise
        analysis_frame = ttk.LabelFrame(main_frame, text="📋 ANÁLISE DO DOCUMENTO", padding=10)
        analysis_frame.pack(fill=tk.X, pady=10)
        self.create_analysis_panel(analysis_frame)

        # Área de preview (Tabela)
        preview_frame = ttk.LabelFrame(main_frame, text="👁️ PREVIEW DOS DADOS", padding=10)
        preview_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        self.create_preview_panel(preview_frame)

        # Status bar
        self.create_status_bar(main_frame)

    def create_header(self, parent):
        """Cria cabeçalho"""
        header_frame = ttk.Frame(parent, style='Main.TFrame')
        header_frame.pack(fill=tk.X, pady=(0, 10))

        title = ttk.Label(header_frame,
                          text="📊 Análise e Conversão para Planilha",
                          style='Header.TLabel')
        title.pack(side=tk.LEFT)

        subtitle = ttk.Label(header_frame,
                             text="Extração Automática de Dados Tabulares",
                             style='Info.TLabel')
        subtitle.pack(side=tk.RIGHT, pady=10)

    def create_toolbar(self, parent):
        """Cria barra de ferramentas"""
        toolbar = ttk.Frame(parent, style='Card.TFrame', padding=10)
        toolbar.pack(fill=tk.X, pady=(0, 10))

        # Botões
        btn_upload = ttk.Button(toolbar, text="📂 Carregar Documento",
                                 style='Primary.TButton',
                                 command=self.upload_document)
        btn_upload.pack(side=tk.LEFT, padx=5)

        btn_analyze = ttk.Button(toolbar, text="🔍 Analisar",
                                  style='Primary.TButton',
                                  command=self.analyze_document)
        btn_analyze.pack(side=tk.LEFT, padx=5)

        btn_export_excel = ttk.Button(toolbar, text="📗 Exportar Excel",
                                        style='Primary.TButton',
                                        command=self.export_excel)
        btn_export_excel.pack(side=tk.LEFT, padx=5)

        btn_export_csv = ttk.Button(toolbar, text="📄 Exportar CSV",
                                      style='Primary.TButton',
                                      command=self.export_csv)
        btn_export_csv.pack(side=tk.LEFT, padx=5)

        # Info do arquivo
        self.file_info_var = tk.StringVar(value="Nenhum arquivo carregado")
        info_label = ttk.Label(toolbar, textvariable=self.file_info_var, style='Info.TLabel')
        info_label.pack(side=tk.RIGHT, padx=10)

    def create_analysis_panel(self, parent):
        """Cria painel de análise"""
        # Grid de informações
        info_frame = ttk.Frame(parent, style='Card.TFrame')
        info_frame.pack(fill=tk.X)

        # Labels de informação
        self.info_labels = {}

        info_items = [
            ('tables', 'Tabelas Encontradas:', '0'),
            ('fields', 'Campos Detectados:', '0'),
            ('rows', 'Total de Linhas:', '0'),
            ('columns', 'Total de Colunas:', '0')
        ]

        for i, (key, label, default) in enumerate(info_items):
            # Label
            lbl = ttk.Label(info_frame, text=label, style='Info.TLabel')
            lbl.grid(row=0, column=i*2, padx=10, pady=5, sticky=tk.W)

            # Value
            value_var = tk.StringVar(value=default)
            value_lbl = ttk.Label(info_frame, textvariable=value_var,
                                   font=('Segoe UI', 12, 'bold'),
                                   foreground=self.colors['success'])
            value_lbl.grid(row=0, column=i*2+1, padx=5, pady=5, sticky=tk.W)

            self.info_labels[key] = value_var

    def create_preview_panel(self, parent):
        """Cria painel de preview com Treeview"""
        # Notebook para múltiplas tabelas
        self.preview_notebook = ttk.Notebook(parent)
        self.preview_notebook.pack(fill=tk.BOTH, expand=True)

        # Label de ajuda inicial
        self.help_label = ttk.Label(parent,
                                      text="Carregue e analise um documento para ver o preview dos dados",
                                      style='Info.TLabel')
        self.help_label.pack(pady=50)

    def create_status_bar(self, parent):
        """Cria barra de status"""
        status_frame = ttk.Frame(parent, style='Card.TFrame')
        status_frame.pack(fill=tk.X, pady=(10, 0))

        self.status_var = tk.StringVar(value="Pronto")
        status_label = ttk.Label(status_frame, textvariable=self.status_var, style='Info.TLabel')
        status_label.pack(side=tk.LEFT, padx=10, pady=5)

    def upload_document(self):
        """Upload de documento"""
        filetypes = (
            ('Todos suportados', '*.pdf *.docx *.html *.txt *.md'),
            ('PDF', '*.pdf'),
            ('Word', '*.docx'),
            ('HTML', '*.html'),
            ('Texto', '*.txt *.md'),
            ('Todos', '*.*')
        )

        filepath = filedialog.askopenfilename(title="Selecionar Documento", filetypes=filetypes)

        if filepath:
            self.current_file = filepath
            self.file_info_var.set(f"📄 {Path(filepath).name}")
            self.status_var.set(f"Arquivo carregado: {Path(filepath).name}")

    def analyze_document(self):
        """Analisa documento e extrai dados"""
        if not self.current_file:
            messagebox.showwarning("Aviso", "Carregue um documento primeiro")
            return

        self.status_var.set("Analisando documento...")

        # Analisar em thread
        threading.Thread(target=self._analyze_thread, daemon=True).start()

    def _analyze_thread(self):
        """Thread de análise"""
        try:
            # Extrair dados
            extracted = self.converter.extract_data_from_document(self.current_file)

            if 'error' in extracted:
                self.status_var.set(f"Erro: {extracted['error']}")
                messagebox.showerror("Erro", f"Erro na análise:\n{extracted['error']}")
                return

            # Converter para DataFrames
            dfs = self.converter.convert_to_dataframe(extracted)

            self.current_dataframes = dfs

            # Atualizar informações
            self.update_analysis_info(extracted, dfs)

            # Mostrar preview
            self.show_preview(dfs)

            self.status_var.set(f"Análise concluída: {len(dfs)} tabela(s) encontrada(s)")

        except Exception as e:
            self.status_var.set(f"Erro: {e}")
            messagebox.showerror("Erro", f"Erro ao analisar:\n{e}")
            import traceback
            traceback.print_exc()

    def update_analysis_info(self, extracted: dict, dataframes: list):
        """Atualiza informações da análise"""
        tables_count = len(extracted.get('tables', []))
        fields_count = len(extracted.get('fields', []))

        total_rows = sum(len(df) for df in dataframes)
        total_cols = sum(len(df.columns) for df in dataframes)

        self.info_labels['tables'].set(str(tables_count))
        self.info_labels['fields'].set(str(fields_count))
        self.info_labels['rows'].set(str(total_rows))
        self.info_labels['columns'].set(str(total_cols))

    def show_preview(self, dataframes: list):
        """Mostra preview dos DataFrames em Treeview"""
        # Limpar notebook
        for tab in self.preview_notebook.tabs():
            self.preview_notebook.forget(tab)

        # Esconder label de ajuda
        self.help_label.pack_forget()

        # Criar aba para cada DataFrame
        for i, df in enumerate(dataframes):
            # Frame para a aba
            tab_frame = ttk.Frame(self.preview_notebook, style='Card.TFrame')

            # Nome da aba
            tab_name = getattr(df, 'name', f'Tabela {i+1}')

            # Criar Treeview
            self.create_treeview_for_dataframe(tab_frame, df)

            # Adicionar aba
            self.preview_notebook.add(tab_frame, text=tab_name)

    def create_treeview_for_dataframe(self, parent, df: pd.DataFrame):
        """Cria Treeview para visualizar DataFrame"""
        # Frame container
        container = ttk.Frame(parent, style='Card.TFrame')
        container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Info da tabela
        info_frame = ttk.Frame(container, style='Card.TFrame')
        info_frame.pack(fill=tk.X, pady=(0, 5))

        info_text = f"📊 {len(df)} linhas × {len(df.columns)} colunas"
        ttk.Label(info_frame, text=info_text, style='Info.TLabel').pack(side=tk.LEFT, padx=5)

        # Treeview com scrollbars
        tree_frame = ttk.Frame(container)
        tree_frame.pack(fill=tk.BOTH, expand=True)

        # Scrollbars
        vsb = ttk.Scrollbar(tree_frame, orient="vertical")
        vsb.pack(side=tk.RIGHT, fill=tk.Y)

        hsb = ttk.Scrollbar(tree_frame, orient="horizontal")
        hsb.pack(side=tk.BOTTOM, fill=tk.X)

        # Treeview
        columns = list(df.columns)

        tree = ttk.Treeview(tree_frame,
                            columns=columns,
                            show='headings',
                            yscrollcommand=vsb.set,
                            xscrollcommand=hsb.set)

        vsb.config(command=tree.yview)
        hsb.config(command=tree.xview)

        # Configurar colunas
        for col in columns:
            tree.heading(col, text=col)
            # Ajustar largura baseado no conteúdo
            max_width = max(
                len(str(col)) * 10,
                max([len(str(val)) for val in df[col][:100]], default=0) * 8
            )
            tree.column(col, width=min(max_width, 300))

        # Inserir dados (limitado a 1000 linhas para performance)
        max_rows = min(len(df), 1000)

        for idx in range(max_rows):
            row = df.iloc[idx]
            values = [str(val) for val in row]
            tree.insert('', tk.END, values=values)

        tree.pack(fill=tk.BOTH, expand=True)

        # Aviso se limitado
        if len(df) > 1000:
            warning_lbl = ttk.Label(container,
                                     text=f"⚠️ Mostrando primeiras 1000 linhas de {len(df)} (todas serão exportadas)",
                                     foreground=self.colors['warning'])
            warning_lbl.pack(pady=5)

    def export_excel(self):
        """Exporta para Excel"""
        if not self.current_dataframes:
            messagebox.showwarning("Aviso", "Analise um documento primeiro")
            return

        filepath = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[('Excel', '*.xlsx')],
            initialfile="documento_convertido.xlsx"
        )

        if not filepath:
            return

        try:
            self.status_var.set("Exportando para Excel...")

            self.converter.export_to_excel(self.current_dataframes, filepath)

            self.status_var.set(f"Exportado: {Path(filepath).name}")
            messagebox.showinfo("Sucesso", f"Planilha Excel criada:\n{filepath}")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar:\n{e}")
            self.status_var.set("Erro na exportação")

    def export_csv(self):
        """Exporta para CSV"""
        if not self.current_dataframes:
            messagebox.showwarning("Aviso", "Analise um documento primeiro")
            return

        output_dir = filedialog.askdirectory(title="Escolher pasta para salvar CSVs")

        if not output_dir:
            return

        try:
            self.status_var.set("Exportando para CSV...")

            files = self.converter.export_to_csv(self.current_dataframes, output_dir)

            self.status_var.set(f"Exportados: {len(files)} arquivo(s) CSV")
            messagebox.showinfo("Sucesso",
                                 f"{len(files)} arquivo(s) CSV criado(s) em:\n{output_dir}")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar:\n{e}")
            self.status_var.set("Erro na exportação")


if __name__ == "__main__":
    root = tk.Tk()
    app = SpreadsheetAnalysisApp(root)
    root.mainloop()
