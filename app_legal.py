"""
Docling Legal - Sistema Integrado de Documentos Jurídicos
Versão expandida com Templates e Diagnóstico Condominial
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import json
import threading
import os
import webbrowser
from pathlib import Path
from docling.document_converter import DocumentConverter
from template_manager import TemplateManager


class DoclingLegalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Docling Legal - Sistema de Documentos Jurídicos")
        self.root.geometry("1400x850")
        self.root.minsize(1200, 700)

        # Inicializa componentes
        self.converter = DocumentConverter()
        self.template_manager = TemplateManager()

        # Configurar tema
        self.configure_theme()

        # Criar interface principal com tabs
        self.create_main_interface()

    def configure_theme(self):
        """Configura tema monocromático moderno"""
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

        # Estilos principais
        self.style.configure('Main.TFrame', background=self.colors['bg_dark'])
        self.style.configure('Card.TFrame', background=self.colors['bg_medium'])
        self.style.configure('Header.TLabel',
                             background=self.colors['bg_dark'],
                             foreground=self.colors['text'],
                             font=('Segoe UI', 20, 'bold'))
        self.style.configure('Info.TLabel',
                             background=self.colors['bg_medium'],
                             foreground=self.colors['text_dim'],
                             font=('Segoe UI', 9))
        self.style.configure('Primary.TButton',
                             background=self.colors['accent'],
                             foreground=self.colors['text'],
                             font=('Segoe UI', 10),
                             padding=8)
        self.style.map('Primary.TButton',
                       background=[('active', self.colors['accent_hover'])])

        # Estilo para Notebook (Tabs)
        self.style.configure('TNotebook', background=self.colors['bg_dark'], borderwidth=0)
        self.style.configure('TNotebook.Tab',
                             background=self.colors['bg_medium'],
                             foreground=self.colors['text'],
                             padding=[20, 10],
                             font=('Segoe UI', 10))
        self.style.map('TNotebook.Tab',
                       background=[('selected', self.colors['bg_light'])],
                       foreground=[('selected', self.colors['text'])])

    def create_main_interface(self):
        """Cria interface principal com sistema de tabs"""
        main_frame = ttk.Frame(self.root, style='Main.TFrame', padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        header_frame = ttk.Frame(main_frame, style='Main.TFrame')
        header_frame.pack(fill=tk.X, pady=(0, 20))

        title = ttk.Label(header_frame, text="Docling Legal", style='Header.TLabel')
        title.pack(side=tk.LEFT)

        subtitle = ttk.Label(header_frame,
                             text="Sistema Integrado de Documentos Jurídicos",
                             style='Info.TLabel')
        subtitle.pack(side=tk.RIGHT, pady=10)

        # Notebook (Tabs)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Tab 1: Conversor de Documentos
        self.create_converter_tab()

        # Tab 2: Gerador de Templates
        self.create_template_tab()

        # Tab 3: Diagnóstico Jurídico (futuro)
        self.create_diagnostic_tab()

    def create_converter_tab(self):
        """Cria aba de conversão de documentos (funcionalidade original)"""
        converter_frame = ttk.Frame(self.notebook, style='Main.TFrame', padding=20)
        self.notebook.add(converter_frame, text="📄 Conversor de Documentos")

        # Info
        info_label = ttk.Label(converter_frame,
                                text="Converta documentos PDF, DOCX, TXT, MD, HTML, RTF para Markdown ou JSON",
                                style='Info.TLabel')
        info_label.pack(pady=(0, 20))

        # Content frame com duas colunas
        content_frame = ttk.Frame(converter_frame, style='Main.TFrame')
        content_frame.pack(fill=tk.BOTH, expand=True)

        # Painel de controles
        control_panel = ttk.LabelFrame(content_frame, text="Controles", padding=15)
        control_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        # Seleção de arquivo
        file_frame = ttk.Frame(control_panel, style='Card.TFrame')
        file_frame.pack(fill=tk.X, pady=(0, 15))

        self.conv_file_path = tk.StringVar()
        self.conv_file_entry = ttk.Entry(file_frame, textvariable=self.conv_file_path, width=40)
        self.conv_file_entry.pack(side=tk.LEFT, padx=(0, 10))

        browse_btn = ttk.Button(file_frame, text="Browse", style='Primary.TButton',
                                command=self.browse_converter_file)
        browse_btn.pack(side=tk.LEFT)

        # Formato de saída
        options_frame = ttk.LabelFrame(control_panel, text="Formato de Saída", padding=10)
        options_frame.pack(fill=tk.X, pady=(0, 15))

        self.conv_output_format = tk.StringVar(value="markdown")
        ttk.Radiobutton(options_frame, text="Markdown", variable=self.conv_output_format,
                        value="markdown").pack(anchor=tk.W, padx=10, pady=5)
        ttk.Radiobutton(options_frame, text="JSON", variable=self.conv_output_format,
                        value="json").pack(anchor=tk.W, padx=10, pady=5)

        # Progresso
        progress_frame = ttk.Frame(control_panel, style='Card.TFrame')
        progress_frame.pack(fill=tk.X, pady=(0, 15))

        self.conv_progress = ttk.Progressbar(progress_frame, orient=tk.HORIZONTAL, mode='determinate')
        self.conv_progress.pack(fill=tk.X, pady=(0, 5))

        self.conv_status_var = tk.StringVar(value="Pronto para converter")
        status_label = ttk.Label(progress_frame, textvariable=self.conv_status_var, style='Info.TLabel')
        status_label.pack(fill=tk.X)

        # Botões
        convert_btn = ttk.Button(control_panel, text="Converter Documento",
                                 style='Primary.TButton', command=self.start_conversion)
        convert_btn.pack(fill=tk.X, pady=(0, 10))

        save_btn = ttk.Button(control_panel, text="Salvar Documento Convertido",
                              style='Primary.TButton', command=self.save_converted_document)
        save_btn.pack(fill=tk.X)

        # Painel de resultados
        results_panel = ttk.LabelFrame(content_frame, text="Resultado", padding=15)
        results_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.conv_output_text = scrolledtext.ScrolledText(results_panel, wrap=tk.WORD,
                                                           bg=self.colors['bg_light'],
                                                           fg=self.colors['text'],
                                                           font=('Consolas', 10))
        self.conv_output_text.pack(fill=tk.BOTH, expand=True)

    def create_template_tab(self):
        """Cria aba de geração de documentos a partir de templates"""
        template_frame = ttk.Frame(self.notebook, style='Main.TFrame', padding=20)
        self.notebook.add(template_frame, text="📝 Gerador de Documentos")

        # Painel superior: Seleção de template
        selection_frame = ttk.LabelFrame(template_frame, text="Selecionar Template", padding=15)
        selection_frame.pack(fill=tk.X, pady=(0, 20))

        # Lista de templates
        templates = self.template_manager.get_available_templates()

        self.template_var = tk.StringVar()
        template_combo = ttk.Combobox(selection_frame, textvariable=self.template_var, state='readonly', width=50)
        template_combo['values'] = [f"{t['title']} ({t['field_count']} campos)" for t in templates]
        template_combo.pack(side=tk.LEFT, padx=(0, 10))

        load_btn = ttk.Button(selection_frame, text="Carregar Template", style='Primary.TButton',
                              command=self.load_template_fields)
        load_btn.pack(side=tk.LEFT)

        # Painel de preenchimento
        fill_frame = ttk.LabelFrame(template_frame, text="Preencher Campos", padding=15)
        fill_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))

        # Canvas com scrollbar para campos
        canvas = tk.Canvas(fill_frame, bg=self.colors['bg_medium'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(fill_frame, orient="vertical", command=canvas.yview)
        self.fields_frame = ttk.Frame(canvas, style='Card.TFrame')

        self.fields_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.fields_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Painel de ações
        actions_frame = ttk.Frame(template_frame, style='Main.TFrame')
        actions_frame.pack(fill=tk.X)

        preview_btn = ttk.Button(actions_frame, text="Visualizar Documento",
                                 style='Primary.TButton', command=self.preview_document)
        preview_btn.pack(side=tk.LEFT, padx=5)

        generate_btn = ttk.Button(actions_frame, text="Gerar e Salvar",
                                  style='Primary.TButton', command=self.generate_document)
        generate_btn.pack(side=tk.LEFT, padx=5)

        # Armazena referências dos templates e campos
        self.templates_list = templates
        self.current_fields = {}

    def create_diagnostic_tab(self):
        """Cria aba de diagnóstico jurídico condominial (futuro)"""
        diagnostic_frame = ttk.Frame(self.notebook, style='Main.TFrame', padding=20)
        self.notebook.add(diagnostic_frame, text="⚖️ Diagnóstico Jurídico")

        # Placeholder para funcionalidade futura
        info_text = """
        SISTEMA DE DIAGNÓSTICO JURÍDICO CONDOMINIAL

        Esta funcionalidade permitirá:

        ✓ Análise automática de convenções condominiais
        ✓ Identificação de não conformidades legais
        ✓ Geração de relatórios de conformidade
        ✓ Sugestões de adequação normativa

        Base Legal:
        • Lei 4.591/64 (Condomínios)
        • Código Civil art. 1.331+
        • Jurisprudência STJ

        Status: Em desenvolvimento
        """

        placeholder_label = ttk.Label(diagnostic_frame, text=info_text,
                                      style='Info.TLabel', justify=tk.LEFT)
        placeholder_label.pack(pady=50)

    # ========================
    # FUNÇÕES DO CONVERSOR
    # ========================

    def browse_converter_file(self):
        """Abre diálogo para selecionar arquivo"""
        filetypes = (
            ('PDF files', '*.pdf'),
            ('Word files', '*.docx'),
            ('All files', '*.*')
        )
        filename = filedialog.askopenfilename(title="Selecionar Documento", filetypes=filetypes)
        if filename:
            self.conv_file_path.set(filename)

    def start_conversion(self):
        """Inicia conversão de documento"""
        if not self.conv_file_path.get():
            messagebox.showerror("Erro", "Selecione um arquivo para converter")
            return
        threading.Thread(target=self.convert_document, daemon=True).start()

    def convert_document(self):
        """Converte documento usando Docling"""
        try:
            self.update_conv_progress(0, "Iniciando conversão...")
            result = self.converter.convert(self.conv_file_path.get())

            # Escolhe formato de saída
            if self.conv_output_format.get() == "markdown":
                converted_text = result.document.export_to_markdown()
            else:
                converted_text = result.document.export_to_json()

            self.update_conv_progress(100, "Conversão concluída")
            self.display_conversion_result(converted_text)

        except Exception as e:
            self.update_conv_progress(0, "Erro na conversão")
            messagebox.showerror("Erro de Conversão", str(e))

    def update_conv_progress(self, value, status):
        """Atualiza barra de progresso"""
        self.conv_progress['value'] = value
        self.conv_status_var.set(status)

    def display_conversion_result(self, text):
        """Exibe resultado da conversão"""
        self.conv_output_text.delete(1.0, tk.END)
        self.conv_output_text.insert(tk.END, text)

    def save_converted_document(self):
        """Salva documento convertido"""
        content = self.conv_output_text.get(1.0, tk.END)
        if not content.strip():
            messagebox.showwarning("Aviso", "Nenhum documento para salvar")
            return

        ext = ".md" if self.conv_output_format.get() == "markdown" else ".json"
        filetypes = [('Markdown file', '*.md')] if ext == ".md" else [('JSON file', '*.json')]

        filepath = filedialog.asksaveasfilename(defaultextension=ext, filetypes=filetypes)

        if filepath:
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    if ext == ".json":
                        json_data = json.loads(content)
                        json.dump(json_data, f, ensure_ascii=False, indent=4)
                    else:
                        f.write(content)
                messagebox.showinfo("Sucesso", "Documento salvo com sucesso")
            except Exception as e:
                messagebox.showerror("Erro ao Salvar", str(e))

    # ========================
    # FUNÇÕES DO GERADOR DE TEMPLATES
    # ========================

    def load_template_fields(self):
        """Carrega campos do template selecionado"""
        selection = self.template_var.get()
        if not selection:
            messagebox.showwarning("Aviso", "Selecione um template")
            return

        # Encontra template selecionado
        template_title = selection.split(" (")[0]
        template = next((t for t in self.templates_list if t['title'] == template_title), None)

        if not template:
            messagebox.showerror("Erro", "Template não encontrado")
            return

        # Limpa campos anteriores
        for widget in self.fields_frame.winfo_children():
            widget.destroy()

        self.current_fields = {}

        # Cria campos de entrada
        for i, field in enumerate(template['fields']):
            field_frame = ttk.Frame(self.fields_frame, style='Card.TFrame')
            field_frame.grid(row=i, column=0, sticky=tk.EW, padx=10, pady=5)
            self.fields_frame.columnconfigure(0, weight=1)

            # Label
            label = ttk.Label(field_frame, text=f"{field['label']}:", style='Info.TLabel', width=25)
            label.pack(side=tk.LEFT, padx=(0, 10))

            # Entry
            if field['type'] == 'textarea':
                entry = tk.Text(field_frame, height=3, width=50, bg=self.colors['bg_light'],
                                fg=self.colors['text'])
                entry.insert('1.0', field['default'])
                entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            else:
                entry_var = tk.StringVar(value=field['default'])
                entry = ttk.Entry(field_frame, textvariable=entry_var, width=50)
                entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

            self.current_fields[field['name']] = (entry, field['type'])

        messagebox.showinfo("Sucesso", f"Template '{template_title}' carregado com {len(template['fields'])} campos")

    def get_field_values(self) -> dict:
        """Obtém valores preenchidos dos campos"""
        values = {}
        for field_name, (widget, field_type) in self.current_fields.items():
            if field_type == 'textarea':
                values[field_name] = widget.get('1.0', tk.END).strip()
            else:
                values[field_name] = widget.get().strip()
        return values

    def preview_document(self):
        """Visualiza documento em navegador"""
        if not self.current_fields:
            messagebox.showwarning("Aviso", "Carregue um template primeiro")
            return

        # Obtém template selecionado
        selection = self.template_var.get()
        template_title = selection.split(" (")[0]
        template = next((t for t in self.templates_list if t['title'] == template_title), None)

        if not template:
            return

        # Obtém valores e gera documento
        values = self.get_field_values()

        # Valida dados
        errors = self.template_manager.validate_data(template['name'], values)
        if errors:
            error_msg = "Erros de validação:\n\n"
            for field, msgs in errors.items():
                error_msg += f"• {field}: {', '.join(msgs)}\n"
            messagebox.showerror("Erro de Validação", error_msg)
            return

        try:
            filled_html = self.template_manager.fill_template(template['name'], values)

            # Salva temporariamente
            temp_file = Path("temp_preview.html")
            self.template_manager.save_filled_template(filled_html, str(temp_file))

            # Abre no navegador
            webbrowser.open(str(temp_file.absolute()))

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar preview: {e}")

    def generate_document(self):
        """Gera e salva documento final"""
        if not self.current_fields:
            messagebox.showwarning("Aviso", "Carregue um template primeiro")
            return

        # Obtém template selecionado
        selection = self.template_var.get()
        template_title = selection.split(" (")[0]
        template = next((t for t in self.templates_list if t['title'] == template_title), None)

        if not template:
            return

        # Obtém valores
        values = self.get_field_values()

        # Valida dados
        errors = self.template_manager.validate_data(template['name'], values)
        if errors:
            error_msg = "Erros de validação:\n\n"
            for field, msgs in errors.items():
                error_msg += f"• {field}: {', '.join(msgs)}\n"
            messagebox.showerror("Erro de Validação", error_msg)
            return

        # Pergunta onde salvar
        filepath = filedialog.asksaveasfilename(
            defaultextension=".html",
            filetypes=[
                ('HTML files', '*.html'),
                ('Markdown files', '*.md'),
                ('All files', '*.*')
            ]
        )

        if not filepath:
            return

        try:
            filled_html = self.template_manager.fill_template(template['name'], values)

            # Se for markdown, converte
            if filepath.endswith('.md'):
                content = self.template_manager.export_to_markdown(filled_html)
            else:
                content = filled_html

            # Salva arquivo
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            messagebox.showinfo("Sucesso", f"Documento gerado com sucesso:\n{filepath}")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar documento: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DoclingLegalApp(root)
    root.mainloop()
