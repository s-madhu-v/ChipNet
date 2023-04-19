import tkinter as tk
from scripts.gui.allConsoles import (
    createAdConsole,
    createBidConsole,
    createApprovedBidConsole,
)


class buyPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.createWidgets()

    def createWidgets(self):
        # create a adConsole
        self.adConsole = createAdConsole(self)
        self.adConsole.grid(row=1, column=0, pady=5, sticky="nsew")
        # create a bidConsole
        self.bidConsole = createBidConsole(self)
        self.bidConsole.grid(row=2, column=0, pady=5, sticky="nsew")
        # create a approvedBidConsole
        self.approvedBidConsole = createApprovedBidConsole(self)
        self.approvedBidConsole.grid(row=3, column=0, pady=5, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

    def refresh(self):
        self.adConsole.updateFramesContainer()
        self.bidConsole.updateFramesContainer()
        self.approvedBidConsole.updateFramesContainer()
