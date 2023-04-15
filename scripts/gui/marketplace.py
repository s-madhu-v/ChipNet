import tkinter as tk
from tkinter import ttk
from scripts.gui.adConsole import createAdConsole
from scripts.gui.bidConsole import bidConsole


class marketplace(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=860, height=170, relief="raised")
        self.createWidgets()
        ttk.Style().configure("marketplace.TFrame", background="red")
        self["style"] = "marketplaceView.TFrame"

    def createWidgets(self):
        self.adConsole = createAdConsole(self)
        self.adConsole.pack()
        updateButton = ttk.Button(self, text="Update")
        updateButton["command"] = lambda: self.adConsole.updateFramesContainer()
        updateButton.pack()
        # create a bidConsole
        self.bidConsole = bidConsole(self)
        self.bidConsole.pack()
        updateButton = ttk.Button(self, text="Update")
        updateButton["command"] = lambda: self.bidConsole.updateBidsContainer()
        updateButton.pack()
