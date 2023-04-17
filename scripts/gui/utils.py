import tkinter as tk
from tkinter import ttk
from scripts.gui.root import root


def createNewWindow(title="New Window", geometry="200x200+200+200"):
    new_window = tk.Toplevel(root)
    new_window.title(title)
    new_window.geometry(geometry)
    return new_window


def copy_text(event):
    root.clipboard_clear()
    root.clipboard_append(event.widget.cget("text"))
