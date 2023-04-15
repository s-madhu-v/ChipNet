import tkinter as tk
from tkinter import ttk
from scripts.gui.bidsContainer import bidsContainer
from scripts.data import contractData

bidConsolebackground = "red"


class bidConsole(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=860, height=200, relief="raised")
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()
        self.createLayout()
        ttk.Style().configure("bidConsole.TFrame", background=bidConsolebackground)
        self["style"] = "bidConsole.TFrame"

    def createWidgets(self):
        # create the widgets
        self.leftButton = tk.Button(self, text="<", width=1, height=9)
        self.leftButton["command"] = lambda: self.leftButtonHandler()
        self.bidsContainer = bidsContainer(self)
        self.rightButton = tk.Button(self, text=">", width=1, height=9)
        self.rightButton["command"] = lambda: self.rightButtonHandler()

    def createLayout(self):
        # layout the widgets
        self.leftButton.pack(side="left")
        self.bidsContainer.pack(side="left")
        self.rightButton.pack(side="left")

    def leftButtonHandler(self):
        if self.bidsContainer.startBidIndex > 0:
            self.bidsContainer.startBidIndex -= 1
            self.bidsContainer.moveBidsContainer()

    def rightButtonHandler(self):
        if (
            self.bidsContainer.startBidIndex
            < len(contractData.yourBids) - self.bidsContainer.nofBids
        ):
            self.bidsContainer.startBidIndex += 1
            self.bidsContainer.moveBidsContainer()

    def updateBidsContainer(self):
        self.bidsContainer.updateBidWidgets()
