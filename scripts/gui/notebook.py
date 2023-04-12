import tkinter as tk
from tkinter import ttk


def createNotebook(root):
    # create a notebook
    notebook = ttk.Notebook(root)

    # create tabs and add them to the notebook
    marketplace_tab = ttk.Frame(notebook)
    notebook.add(marketplace_tab, text="Marketplace")

    advertise_tab = ttk.Frame(notebook)
    notebook.add(advertise_tab, text="Advertise")
    advertise_label = tk.Label(advertise_tab, text="Advertise")
    advertise_label.pack()

    purchases_tab = ttk.Frame(notebook)
    notebook.add(purchases_tab, text="Purchases")
    purchases_label = tk.Label(purchases_tab, text="Purchases")
    purchases_label.pack()

    account_tab = ttk.Frame(notebook)
    notebook.add(account_tab, text="Account")
    account_label = tk.Label(account_tab, text="Account")
    account_label.pack()

    # pack the notebook
    notebook.pack()
    return notebook, marketplace_tab, advertise_tab, purchases_tab, account_tab
