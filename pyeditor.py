import tkinter as tk
from tkinter import filedialog
import socket
import time


class Menubar:
    def __init__(self, parent):
        font_specs = ("ubuntu", 14)
        menubar = tk.Menu(parent.root, font=font_specs)
        parent.root.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_specs)
        file_dropdown.add_command(
            label="New File", accelerator="Ctrl+N", command=parent.new_file
        )
        file_dropdown.add_command(
            label="Open File", accelerator="Ctrl+O", command=parent.open_file
        )
        file_dropdown.add_command(
            label="Save", accelerator="Ctrl+S", command=parent.save
        )
        file_dropdown.add_command(
            label="Save As", accelerator="Ctrl+Shift+S", command=parent.save_as
        )
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit", command=parent.root.destroy)

        menubar.add_cascade(label="File", menu=file_dropdown)


class PyText:
    def __init__(self, root):
        root.title("Untitled - PyText")
        root.geometry("1200x700")

        font_specs = ("ubuntu", 18)

        self.root = root
        self.filename = None

        self.textarea = tk.Text(root, font=font_specs)
        self.scroll = tk.Scrollbar(root, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = Menubar(self)

    def set_window_title(self, name=None):
        if name:
            self.root.title(name + " - PyText")
        else:
            self.root.title("Untitled - PyText")

    def new_file(self, *arg):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()

    def open_file(self, *arg):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[
                ("ALL Files", "*.*"),
                ("Text Files", "*.txt"),
                ("Python Scripts", "*.py"),
                ("Markdown", "*.md"),
                ("Javascript", "*.js"),
                ("HTML", "*.html"),
                ("CSS", "*.css"),
            ],
        )
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)

    def save(self, *arg):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
            except Exception as e:
                print(e)
        else:
            self.save_as()

    def save_as(self, *arg):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt", defaultextension=".txt"
            )
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
        except Exception as e:
            print(e)

    def bind_shortcuts(self):
        self.textarea.bind("<Control-n>", self.new_file)
        self.textarea.bind("<Control-s>", self.save)
        self.textarea.bind("<Control-o>", self.open_file)
        self.textarea.bind("<Control-S>", self.save_as)

