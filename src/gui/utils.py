import tkinter as tk
from src.app import getTheApp


def createNewWindow(title="New Window", geometry="200x200+200+200"):
    new_window = tk.Toplevel(getTheApp().root)
    new_window.title(title)
    new_window.geometry(geometry)
    return new_window


def copy_text(event):
    getTheApp().root.clipboard_clear()
    getTheApp().root.clipboard_append(event.widget.cget("text"))
