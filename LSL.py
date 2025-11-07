import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import win32con
import win32ui
import win32gui
import json

CONFIG_FILE = "config.json"
icon_images = {}

def load_last_folder():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            return config.get("last_folder", "")
    return ""

def save_last_folder(folder):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"last_folder": folder}, f)

def find_exe_files(directory):
    exe_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_lower = file.lower()
            if (file_lower.endswith("01_x64.exe") and
                file.startswith("GSA") and
                "INS" not in file and
                "DZV" not in file):
                exe_files.append(os.path.join(root, file))
    return exe_files

def launch_exe(path):
    try:
        subprocess.Popen(path)
    except Exception as e:
        messagebox.showerror("Chyba", f"Nelze spustit soubor:\n{e}")

def extract_icon(exe_path):
    try:
        large, small = win32gui.ExtractIconEx(exe_path, 0)
        hicon = large[0] if large else (small[0] if small else None)
        if not hicon:
            return None

        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, 32, 32)
        hdc = hdc.CreateCompatibleDC()
        hdc.SelectObject(hbmp)
        win32gui.DrawIconEx(hdc.GetHandleOutput(), 0, 0, hicon, 32, 32, 0, None, win32con.DI_NORMAL)

        bmpinfo = hbmp.GetInfo()
        bmpstr = hbmp.GetBitmapBits(True)

        img = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
        img = img.resize((20, 20), Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except:
        return None

def load_exe_files(folder):
    for item in tree.get_children():
        tree.delete(item)
    files = find_exe_files(folder)
    if not files:
        messagebox.showinfo("Info", "Nenalezeny žádné odpovídající .exe soubory.")
    for f in files:
        display_name = os.path.basename(f).replace("_x64", "")
        icon = extract_icon(f)
        if icon:
            icon_images[f] = icon
            tree.insert("", "end", text=display_name, image=icon, values=(f,))
        else:
            tree.insert("", "end", text=display_name, values=(f,))

def browse_and_list():
    folder = filedialog.askdirectory(title="Vyber složku")
    if folder:
        save_last_folder(folder)
        load_exe_files(folder)

def on_double_click(event):
    item = tree.selection()
    if item:
        path = tree.item(item, "values")[0]
        launch_exe(path)

# GUI setup
root = tk.Tk()
root.title("Spouštěč EXE souborů s ikonami (GSA_01_x64.exe)")
root.geometry("900x600")
root.minsize(600, 400)
root.resizable(True, True)

browse_btn = tk.Button(root, text="Vybrat složku", command=browse_and_list)
browse_btn.pack(pady=10)

tree = ttk.Treeview(root)
tree["columns"] = ("path",)
tree.column("#0", width=600)
tree.column("path", width=0, stretch=False)
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
tree.bind("<Double-1>", on_double_click)

last_folder = load_last_folder()
if last_folder and os.path.exists(last_folder):
    load_exe_files(last_folder)

root.mainloop()