"""
Sistema de Clonagem de Formatação de Documentos
Interface com duas colunas: Documento (esquerda) e Template (direita)
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path
import json
import threading
from document_analyzer import DocumentAnalyzer


class DocumentCloneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Clonagem de Documentos")
        self.root.geometry("1600x900")
        self.root.minsize(1400, 700)

        # Analyzer
        self.analyzer = DocumentAnalyzer()
        self.current_analysis = None
        self.current_template = None
        self.selected_field = None

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
            'danger': '#c0392b',
            'selected': '#3498db'
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

    def create_interface(self):
        """Cria interface principal"""
        # Frame principal
        main_frame = ttk.Frame(self.root, style='Main.TFrame', padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        self.create_header(main_frame)

        # Toolbar
        self.create_toolbar(main_frame)

        # Área principal com duas colunas
        content_frame = ttk.Frame(main_frame, style='Main.TFrame')
        content_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Coluna ESQUERDA: Documento
        self.create_document_panel(content_frame)

        # Coluna DIREITA: Template
        self.create_template_panel(content_frame)

        # Status bar
        self.create_status_bar(main_frame)

    def create_header(self, parent):
        """Cria cabeçalho"""
        header_frame = ttk.Frame(parent, style='Main.TFrame')
        header_frame.pack(fill=tk.X, pady=(0, 10))

        title = ttk.Label(header_frame,
                          text="🔄 Sistema de Clonagem de Documentos",
                          style='Header.TLabel')
        title.pack(side=tk.LEFT)

        subtitle = ttk.Label(header_frame,
                             text="Análise, Extração e Replicação de Formatação",
                             style='Info.TLabel')
        subtitle.pack(side=tk.RIGHT, pady=10)

    def create_toolbar(self, parent):
        """Cria barra de ferramentas"""
        toolbar = ttk.Frame(parent, style='Card.TFrame', padding=10)
        toolbar.pack(fill=tk.X, pady=(0, 10))

        # Botões principais
        btn_upload = ttk.Button(toolbar, text="📂 Carregar Documento",
                                 style='Primary.TButton',
                                 command=self.upload_document)
        btn_upload.pack(side=tk.LEFT, padx=5)

        btn_analyze = ttk.Button(toolbar, text="🔍 Analisar",
                                  style='Primary.TButton',
                                  command=self.analyze_document)
        btn_analyze.pack(side=tk.LEFT, padx=5)

        btn_auto_fill = ttk.Button(toolbar, text="⚡ Preencher Auto",
                                     style='Primary.TButton',
                                     command=self.auto_fill)
        btn_auto_fill.pack(side=tk.LEFT, padx=5)

        btn_export = ttk.Button(toolbar, text="💾 Exportar",
                                 style='Primary.TButton',
                                 command=self.export_document)
        btn_export.pack(side=tk.LEFT, padx=5)

        # Info
        self.doc_info_var = tk.StringVar(value="Nenhum documento carregado")
        info_label = ttk.Label(toolbar, textvariable=self.doc_info_var, style='Info.TLabel')
        info_label.pack(side=tk.RIGHT, padx=10)

    def create_document_panel(self, parent):
        """Cria painel do documento (esquerda)"""
        doc_panel = ttk.LabelFrame(parent, text="📄 DOCUMENTO ORIGINAL",
                                    padding=10)
        doc_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))

        # Área de texto do documento
        text_frame = ttk.Frame(doc_panel, style='Card.TFrame')
        text_frame.pack(fill=tk.BOTH, expand=True)

        # Scrolled text para visualizar documento
        self.doc_text = scrolledtext.ScrolledText(
            text_frame,
            wrap=tk.WORD,
            bg=self.colors['bg_light'],
            fg=self.colors['text'],
            font=('Consolas', 10),
            selectbackground=self.colors['selected']
        )
        self.doc_text.pack(fill=tk.BOTH, expand=True)

        # Botão para enviar texto selecionado
        btn_frame = ttk.Frame(doc_panel, style='Card.TFrame')
        btn_frame.pack(fill=tk.X, pady=(10, 0))

        btn_send = ttk.Button(btn_frame,
                               text="➡️ Enviar Seleção para Campo",
                               style='Primary.TButton',
                               command=self.send_selection_to_field)
        btn_send.pack(fill=tk.X)

    def create_template_panel(self, parent):
        """Cria painel do template (direita)"""
        template_panel = ttk.LabelFrame(parent, text="📝 TEMPLATE / EDITOR",
                                         padding=10)
        template_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 0))

        # Canvas com scroll para campos
        canvas_frame = ttk.Frame(template_panel, style='Card.TFrame')
        canvas_frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(canvas_frame, bg=self.colors['bg_medium'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)

        self.fields_frame = ttk.Frame(canvas, style='Card.TFrame')
        self.fields_frame.bind("<Configure>",
                                lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=self.fields_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.template_fields = {}

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
            ('Todos documentos', '*.pdf *.docx *.html *.txt *.md'),
            ('PDF', '*.pdf'),
            ('Word', '*.docx'),
            ('HTML', '*.html'),
            ('Texto', '*.txt *.md'),
            ('Todos arquivos', '*.*')
        )

        filepath = filedialog.askopenfilename(title="Selecionar Documento", filetypes=filetypes)

        if filepath:
            self.load_document(filepath)

    def load_document(self, filepath: str):
        """Carrega documento"""
        self.status_var.set(f"Carregando: {Path(filepath).name}...")
        self.doc_info_var.set(f"📄 {Path(filepath).name}")

        # Carregar em thread
        threading.Thread(target=self._load_document_thread, args=(filepath,), daemon=True).start()

    def _load_document_thread(self, filepath: str):
        """Thread para carregar documento"""
        try:
            # Tentar ler como texto primeiro
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Se for HTML, mostrar como está
                if filepath.endswith('.html'):
                    soup = BeautifulSoup(content, 'html.parser')
                    # Extrair apenas texto visível
                    for script in soup(["script", "style"]):
                        script.decompose()
                    text = soup.get_text()
                    # Limpar espaços extras
                    lines = [line.strip() for line in text.splitlines() if line.strip()]
                    content = '\n'.join(lines)

            except UnicodeDecodeError:
                content = f"Arquivo binário: {Path(filepath).name}\nUse 'Analisar' para processar."

            # Atualizar UI
            self.doc_text.delete(1.0, tk.END)
            self.doc_text.insert(tk.END, content)

            self.current_document_path = filepath
            self.status_var.set(f"Documento carregado: {Path(filepath).name}")

        except Exception as e:
            self.status_var.set(f"Erro ao carregar: {e}")
            messagebox.showerror("Erro", f"Erro ao carregar documento:\n{e}")

    def analyze_document(self):
        """Analisa documento e cria template"""
        if not hasattr(self, 'current_document_path'):
            messagebox.showwarning("Aviso", "Carregue um documento primeiro")
            return

        self.status_var.set("Analisando documento...")

        # Analisar em thread
        threading.Thread(target=self._analyze_thread, daemon=True).start()

    def _analyze_thread(self):
        """Thread para análise"""
        try:
            # Analisar
            analysis = self.analyzer.analyze_document(self.current_document_path)

            if 'error' in analysis:
                self.status_var.set(f"Erro: {analysis['error']}")
                messagebox.showerror("Erro", f"Erro na análise:\n{analysis['error']}")
                return

            self.current_analysis = analysis

            # Criar template
            template = self.analyzer.create_template_from_analysis(analysis)
            self.current_template = template

            # Criar campos
            self.create_template_fields(template)

            self.status_var.set(f"Análise concluída: {len(template['fields'])} campos detectados")

        except Exception as e:
            self.status_var.set(f"Erro na análise: {e}")
            messagebox.showerror("Erro", f"Erro ao analisar:\n{e}")
            import traceback
            traceback.print_exc()

    def create_template_fields(self, template: dict):
        """Cria campos do template na interface"""
        # Limpar campos anteriores
        for widget in self.fields_frame.winfo_children():
            widget.destroy()

        self.template_fields = {}

        # Criar campos
        for i, field in enumerate(template['fields']):
            field_frame = ttk.Frame(self.fields_frame, style='Card.TFrame')
            field_frame.grid(row=i, column=0, sticky=tk.EW, padx=10, pady=5)
            self.fields_frame.columnconfigure(0, weight=1)

            # Label
            label = ttk.Label(field_frame, text=field['label'], style='Info.TLabel')
            label.pack(anchor=tk.W, pady=(0, 5))

            # Entry (com fundo destacado ao clicar)
            if field['type'] in ['paragraph', 'header'] and len(field.get('default', '')) > 100:
                # Text widget para campos longos
                text_widget = tk.Text(
                    field_frame,
                    height=3,
                    bg=self.colors['bg_light'],
                    fg=self.colors['text'],
                    font=('Segoe UI', 10),
                    wrap=tk.WORD
                )
                text_widget.insert('1.0', field.get('default', ''))
                text_widget.pack(fill=tk.X, expand=True)

                # Bind click
                text_widget.bind('<FocusIn>',
                                 lambda e, fid=field['id']: self.select_field(fid))

                self.template_fields[field['id']] = text_widget

            else:
                # Entry widget para campos curtos
                entry_var = tk.StringVar(value=field.get('default', ''))
                entry = ttk.Entry(field_frame, textvariable=entry_var, font=('Segoe UI', 10))
                entry.pack(fill=tk.X, expand=True)

                # Bind click
                entry.bind('<FocusIn>',
                           lambda e, fid=field['id']: self.select_field(fid))

                self.template_fields[field['id']] = entry_var

    def select_field(self, field_id: str):
        """Seleciona campo para receber texto"""
        self.selected_field = field_id
        self.status_var.set(f"Campo selecionado: {field_id}")

    def send_selection_to_field(self):
        """Envia texto selecionado no documento para campo selecionado"""
        if not self.selected_field:
            messagebox.showwarning("Aviso", "Clique em um campo primeiro")
            return

        # Obter texto selecionado
        try:
            selected_text = self.doc_text.get(tk.SEL_FIRST, tk.SEL_LAST)
        except tk.TclError:
            messagebox.showwarning("Aviso", "Selecione texto no documento primeiro")
            return

        # Enviar para campo
        field_widget = self.template_fields.get(self.selected_field)

        if field_widget:
            if isinstance(field_widget, tk.StringVar):
                field_widget.set(selected_text)
            else:  # Text widget
                field_widget.delete('1.0', tk.END)
                field_widget.insert('1.0', selected_text)

            self.status_var.set(f"Texto enviado para: {self.selected_field}")

    def auto_fill(self):
        """Preenche campos automaticamente baseado em padrões"""
        if not self.current_template:
            messagebox.showwarning("Aviso", "Analise um documento primeiro")
            return

        messagebox.showinfo("Info", "Preenchimento automático em desenvolvimento")
        # TODO: Implementar regex e ML para preenchimento automático

    def export_document(self):
        """Exporta documento com template preenchido"""
        if not self.current_template:
            messagebox.showwarning("Aviso", "Analise um documento primeiro")
            return

        # Coletar dados dos campos
        data = {}
        for field_id, widget in self.template_fields.items():
            if isinstance(widget, tk.StringVar):
                data[field_id] = widget.get()
            else:  # Text widget
                data[field_id] = widget.get('1.0', tk.END).strip()

        # Escolher onde salvar
        filepath = filedialog.asksaveasfilename(
            defaultextension=".html",
            filetypes=[('HTML', '*.html'), ('JSON', '*.json'), ('Markdown', '*.md')]
        )

        if not filepath:
            return

        # Exportar baseado no formato
        ext = Path(filepath).suffix.lower()

        try:
            if ext == '.json':
                # Exportar como JSON
                export_data = {
                    'template': self.current_template,
                    'data': data
                }
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(export_data, f, indent=4, ensure_ascii=False)

            elif ext == '.md':
                # Exportar como Markdown
                lines = []
                for field in self.current_template['fields']:
                    value = data.get(field['id'], '')
                    if field['type'] == 'header':
                        level = '#' * field.get('level', 1)
                        lines.append(f"{level} {value}\n")
                    else:
                        lines.append(f"{value}\n")

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(lines))

            else:
                # Exportar como HTML (reconstruir com formatação)
                messagebox.showinfo("Info", "Exportação HTML com formatação em desenvolvimento")
                return

            self.status_var.set(f"Exportado: {Path(filepath).name}")
            messagebox.showinfo("Sucesso", f"Documento exportado:\n{filepath}")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar:\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DocumentCloneApp(root)
    root.mainloop()
