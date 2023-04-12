import tkinter as tk
from tkinter import ttk
from scripts.gui.adConsole import adConsole


class marketplace(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=860, height=170, relief="raised")
        self.createWidgets()
        ttk.Style().configure("marketplace.TFrame", background="red")
        self["style"] = "marketplaceView.TFrame"

    def createWidgets(self):
        self.adConsole = adConsole(self)
        self.adConsole.pack()
        updateButton = ttk.Button(self, text="Update")
        updateButton["command"] = lambda: self.adConsole.updateAdsContainer()
        updateButton.pack()
