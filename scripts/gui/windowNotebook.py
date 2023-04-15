import tkinter as tk
from tkinter import ttk
from scripts.gui.marketplace import marketplace
from scripts.gui.advertise import advertise


class windowNotebook(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        self.createWidgets()

    def createWidgets(self):
        # create tabs and add them to the notebook
        self.marketplace = marketplace(self)
        self.add(self.marketplace, text="Marketplace")

        self.advertise = advertise(self)
        self.add(self.advertise, text="Advertise")

        self.services_tab = ttk.Frame(self)
        self.add(self.services_tab, text="Services")
        self.services_label = tk.Label(self.services_tab, text="Your Services")
        self.services_label.pack()

        self.account_tab = ttk.Frame(self)
        self.add(self.account_tab, text="Account")
        self.account_label = tk.Label(self.account_tab, text="Account")
        self.account_label.pack()
