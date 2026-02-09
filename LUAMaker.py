import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import sys, os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def generate_lua():
    name = name_entry.get().strip()
    model_path = model_entry.get().strip()
    arms_path = arms_entry.get().strip()

    if not name or not model_path or not arms_path:
        messagebox.showerror("Error", "All fields are required.")
        return

    if not model_path.endswith(".mdl"):
        model_path += ".mdl"

    if not arms_path.endswith(".mdl"):
        arms_path += ".mdl"

    lua_code = f'''player_manager.AddValidModel( "{name}", "{model_path}" )
player_manager.AddValidHands( "{name} Arms", "{arms_path}", 0, "00000000" )
'''

    file_path = filedialog.asksaveasfilename(
        defaultextension=".lua",
        filetypes=[("Lua Files", "*.lua")],
        initialfile=f"{name.lower()}_playermodel.lua"
    )

    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(lua_code)
        messagebox.showinfo("Success", "Playermodel LUA file created!")

root = tb.Window(themename="darkly")
root.title("GMod Playermodel Generator")
root.geometry("560x460")
root.resizable(False, False)

root.iconbitmap(resource_path("icon.ico"))

frame = tb.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

title = tb.Label(
    frame,
    text="Garry's Mod LUA Playermodel Generator",
    font=("Segoe UI", 16, "bold"),
    bootstyle="info"
)
title.pack(pady=(0, 20))

def labeled_entry(parent, label_text):
    lbl = tb.Label(parent, text=label_text, font=("Segoe UI", 11))
    lbl.pack(anchor="w", pady=(5, 0))
    entry = tb.Entry(parent, font=("Segoe UI", 11))
    entry.pack(fill="x", pady=5)
    return entry

name_entry = labeled_entry(frame, "Playermodel Name")
model_entry = labeled_entry(frame, "Main Model Path (models/... .mdl)")
arms_entry = labeled_entry(frame, "Arms Model Path (models/arms/... .mdl)")

generate_btn = tb.Button(
    frame,
    text="Generate LUA File",
    bootstyle="success",
    command=generate_lua,
    width=25,
)
generate_btn.pack(pady=25)

root.mainloop()
