import tkinter as tk
from tkinter import ttk
from scripts.gui.allConsoles import (
    createAdConsole,
    createBidConsole,
    createApprovedBidConsole,
)


class TabFrame(tk.Frame):
    def __init__(self, parent, tabNames):
        super().__init__(parent, width=1000, height=40)
        self["bg"] = "red"
        self.grid_propagate(False)
        self.tabNames = tabNames
        self.createWidgets()

    def createWidgets(self):
        for i in range(len(self.tabNames)):
            self.tab = tk.Label(self, text=self.tabNames[i], font=("Arial", 16))
            self.tab["bg"] = "green"
            self.tab.grid(row=0, column=i, sticky="nsew")
            self.columnconfigure(i, weight=1)
        self.rowconfigure(0, weight=1)


tabs = ["Buy", "Sell", "My Services", "My Account", "Refresh"]


class marketplace(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.createWidgets()

    def createWidgets(self):
        self.TabFrame = TabFrame(self, tabs)
        self.TabFrame.grid(row=0, column=0, sticky="nsew")

        # create a adConsole
        self.adConsole = createAdConsole(self)
        self.adConsole.grid(row=1, column=0, pady=5, sticky="nsew")
        self.bidConsole = createBidConsole(self)
        self.bidConsole.grid(row=2, column=0, pady=5, sticky="nsew")
        self.approvedBidConsole = createApprovedBidConsole(self)
        self.approvedBidConsole.grid(row=3, column=0, pady=5, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
