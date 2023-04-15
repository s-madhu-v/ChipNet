import tkinter as tk
from tkinter import ttk
from scripts.gui.allConsoles import (
    createAdConsole,
    createBidConsole,
    createApprovedBidConsole,
)


class marketplace(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=860, height=170, relief="raised")
        self.createWidgets()
        ttk.Style().configure("marketplace.TFrame", background="red")
        self["style"] = "marketplaceView.TFrame"

    def createWidgets(self):
        # create a adConsole
        self.adConsole = createAdConsole(self)
        self.adConsole.pack()
        updateButton = ttk.Button(self, text="Update")
        updateButton["command"] = lambda: self.adConsole.updateFramesContainer()
        updateButton.pack()
        # create a bidConsole
        self.bidConsole = createBidConsole(self)
        self.bidConsole.pack()
        updateButton = ttk.Button(self, text="Update")
        updateButton["command"] = lambda: self.bidConsole.updateFramesContainer()
        updateButton.pack()
        # create a approvedBidConsole
        self.approvedBidConsole = createApprovedBidConsole(self)
        self.approvedBidConsole.pack()
        updateButton = ttk.Button(self, text="Update")
        updateButton[
            "command"
        ] = lambda: self.approvedBidConsole.updateFramesContainer()
        updateButton.pack()
