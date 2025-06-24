import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

class ConverterApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("Convertisseur HEIC → Image")
        self.geometry("560x460")
        self.resizable(False, False)

        self.selected_files: list[str] = []
        self.output_format = tk.StringVar(value="jpg")

        self._build_ui()

    def _build_ui(self):
        tk.Label(self, text="Bienvenue", font=("Arial", 18, "bold")).pack(pady=12)
        tk.Label(self, text="Choisissez ce que vous voulez convertir :").pack()

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=8)
        tk.Button(btn_frame, text="Convertir un dossier", width=20, command=self._select_folder).pack(side="left", padx=8)
        tk.Button(btn_frame, text="Convertir des fichiers", width=20, command=self._select_files).pack(side="left", padx=8)

        list_frame = tk.Frame(self)
        list_frame.pack(pady=10, fill="both", expand=True)
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")
        self.listbox = tk.Listbox(list_frame, selectmode=tk.MULTIPLE, width=70, height=12, yscrollcommand=scrollbar.set)
        self.listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.listbox.yview)

        # Drag and drop sur la listbox
        self.listbox.drop_target_register(DND_FILES)
        self.listbox.dnd_bind("<<Drop>>", self._on_drop_files)

        format_frame = tk.Frame(self)
        format_frame.pack(pady=6)
        tk.Label(format_frame, text="Format de sortie :").pack(side="left")
        format_menu = ttk.Combobox(format_frame, textvariable=self.output_format, state="readonly")
        format_menu["values"] = ["jpg", "png", "webp"]
        format_menu.current(0)
        format_menu.pack(side="left", padx=6)

        self.progress = ttk.Progressbar(self, length=480, mode="determinate")
        self.progress.pack(pady=6)

        tk.Button(self, text="Convertir", width=25, command=self._convert_selected).pack(pady=6)

    def _select_folder(self):
        folder = filedialog.askdirectory(title="Sélectionner un dossier contenant des fichiers HEIC")
        if folder:
            self.selected_files = [
                os.path.join(folder, f)
                for f in os.listdir(folder)
                if f.lower().endswith((".heic", ".heif"))
            ]
            self._refresh_listbox()

    def _select_files(self):
        messagebox.showinfo("Info", "Maintenez Ctrl (ou Cmd) pour sélectionner plusieurs fichiers.")
        files = filedialog.askopenfilenames(
            title="Sélectionner des fichiers HEIC",
            filetypes=[("Fichiers HEIC", "*.heic *.heif")],
        )
        if files:
            self.selected_files = list(files)
            self._refresh_listbox()

    def _on_drop_files(self, event):
        paths = self.tk.splitlist(event.data)
        for path in paths:
            if os.path.isfile(path) and path.lower().endswith((".heic", ".heif")):
                if path not in self.selected_files:
                    self.selected_files.append(path)
        self._refresh_listbox()

    def _refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for path in self.selected_files:
            self.listbox.insert(tk.END, os.path.basename(path))

    def _convert_selected(self):
        if not self.selected_files:
            messagebox.showerror("Erreur", "Aucun fichier HEIC sélectionné.")
            return

        idxs = self.listbox.curselection()
        files_to_convert = [self.selected_files[i] for i in idxs] if idxs else self.selected_files

        output_dir = filedialog.askdirectory(title="Sélectionner le dossier de destination")
        if not output_dir:
            return

        fmt = self.output_format.get()
        save_format = fmt.upper()
        if save_format == "JPG":
            save_format = "JPEG"

        total = len(files_to_convert)
        self.progress.configure(maximum=total, value=0)
        self.update_idletasks()

        for count, file_path in enumerate(files_to_convert, start=1):
            try:
                img = Image.open(file_path)
                output_path = os.path.join(
                    output_dir,
                    os.path.splitext(os.path.basename(file_path))[0] + f".{fmt}"
                )
                img.save(output_path, format=save_format, quality=95)
            except Exception as exc:
                messagebox.showerror("Erreur", f"Erreur avec {file_path} :\n{exc}")

            self.progress.configure(value=count)
            self.update_idletasks()

        if messagebox.askyesno("Suppression", "Supprimer les fichiers HEIC convertis ?"):
            for file_path in files_to_convert:
                try:
                    os.remove(file_path)
                except Exception as exc:
                    print(f"Erreur suppression {file_path} : {exc}")

        self.selected_files.clear()
        self._refresh_listbox()
        self.progress.configure(value=0)
        messagebox.showinfo("Terminé", "Conversion terminée !")