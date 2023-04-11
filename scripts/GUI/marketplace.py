import tkinter as tk
from tkinter import ttk


class adLabel(tk.Frame):
    def __init__(self, ad, master=None):
        super().__init__(master)
        self.titleLabel = tk.Label(self, text=f"Title: {ad[0]}")
        self.titleLabel.pack()
        self.priceLabel = tk.Label(self, text=f"Price: {ad[1]}")
        self.priceLabel.pack()
