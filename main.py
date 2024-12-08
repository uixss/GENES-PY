import os
import shutil
import subprocess
import re
import customtkinter as ctk
from tkinter import filedialog, messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title(".")
root.geometry("400x200")
root.resizable(False, False)

py_file_path = ""
icon_file_path = ""
def select_py_file():
    global py_file_path
    py_file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if py_file_path:
        py_file_entry.delete(0, "end")
        py_file_entry.insert(0, py_file_path)

def select_icon_file():
    global icon_file_path
    icon_file_path = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
    if icon_file_path:
        icon_file_entry.delete(0, "end")
        icon_file_entry.insert(0, icon_file_path)


def extract_imports(py_file):
    import_lines = []
    in_multiline_comment = False
    in_js_block = False
    with open(py_file, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            if line.startswith(('"""', "'''")):
                in_multiline_comment = not in_multiline_comment
                continue

            if line.startswith(("js_template =", "js_template = r")):
                in_js_block = True
                continue

            if in_js_block:
                if line.endswith('"""') or line.endswith("'''"):
                    in_js_block = False
                continue

            if in_multiline_comment:
                continue

            if re.match(r'^\s*(import|from)\s+[a-zA-Z0-9_.]+', line):
                import_lines.append(line)

    return import_lines


def generate_and_build():
    global py_file_path
    if not py_file_path:
        messagebox.showerror("Error", "Debe seleccionar un archivo .py")
        return
    imports = extract_imports(py_file_path)

    py_basename = os.path.basename(py_file_path)
    pyx_file = py_basename.replace(".py", ".pyx")
    
    with open(py_file_path, "r", encoding="utf-8") as f:
        content = f.read()
    with open(pyx_file, "w", encoding="utf-8") as f:
        f.write(content)

    # Crear setup.py
    setup_code = f"""
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("{pyx_file}")
)
"""
    with open("setup.py", "w", encoding="utf-8") as f:
        f.write(setup_code)
    try:
        subprocess.run(["python", "setup.py", "build_ext", "--inplace"], check=True)
        messagebox.showinfo("Éxito", f"Archivo {pyx_file} compilado correctamente.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error durante la compilación del archivo .pyx:\n{e}")
        return
    imports_code = "\n".join(imports)
    main_code = f"""
{imports_code}

import importlib
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

module_name = "{os.path.splitext(pyx_file)[0]}"
module = importlib.import_module(module_name)

if __name__ == "__main__":
    if hasattr(module, "gui_main"):
        module.gui_main()
    else:
        print(f"El módulo {{module_name}} no contiene la función 'gui_main'.")
"""
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(main_code)

    messagebox.showinfo("Éxito", "Archivos .pyx y main.py generados correctamente.")
    build_exe()

def build_exe():
    if not os.path.exists("main.py"):
        messagebox.showerror("Error", "Debe generar primero el archivo main.py")
        return

    command = ["python", "-m", "PyInstaller", "--onefile"]
    if icon_file_path:
        command.extend(["--icon", icon_file_path])
    command.extend(["--add-binary", "script.cp312-win_amd64.pyd;.", "main.py"])

    try:
        subprocess.run(command, check=True)

        exe_name = "main.exe"
        dist_path = os.path.join(os.getcwd(), "dist", exe_name)
        if os.path.exists(dist_path):
            shutil.move(dist_path, os.getcwd())
        cleanup_generated_files()

        messagebox.showinfo("Éxito", "Ejecutable creado y archivos temporales eliminados correctamente.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error durante la creación del ejecutable:\n{e}")

def cleanup_generated_files():
    folders = ["build", "dist"]
    files = ["main.spec", "setup.py"]

    for folder in folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)

    for file in files:
        if os.path.exists(file):
            os.remove(file)

ctk.CTkLabel(root, text="Archivo .py", bg_color="#262626").grid(row=0, column=0, padx=10, pady=10, sticky="e")
py_file_entry = ctk.CTkEntry(root, width=50)
py_file_entry.grid(row=0, column=1, padx=10, pady=10)
ctk.CTkButton(root, text="...", command=select_py_file).grid(row=0, column=2, padx=10, pady=10)

ctk.CTkLabel(root, text=".ico", bg_color="#262626").grid(row=1, column=0, padx=10, pady=10, sticky="e")
icon_file_entry = ctk.CTkEntry(root, width=50) 
icon_file_entry.grid(row=1, column=1, padx=10, pady=10)
ctk.CTkButton(root, text="...", command=select_icon_file).grid(row=1, column=2, padx=10, pady=10)
ctk.CTkButton(root, text="RUN", command=generate_and_build).grid(row=2, column=1, pady=20)

root.mainloop()
