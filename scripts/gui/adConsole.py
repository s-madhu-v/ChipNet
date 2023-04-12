import tkinter as tk
from tkinter import ttk
from scripts.gui.adsContainer import adsContainer
from scripts.data import contractData

adConsolebackground = "red"


class adConsole(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=860, height=170, relief="raised")
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()
        self.createLayout()
        ttk.Style().configure("adConsole.TFrame", background=adConsolebackground)
        self["style"] = "adConsole.TFrame"

    def createWidgets(self):
        # create the widgets
        self.leftButton = tk.Button(self, text="<", width=1, height=9)
        self.leftButton["command"] = lambda: self.leftButtonHandler()
        self.adsContainer = adsContainer(self)
        self.rightButton = tk.Button(self, text=">", width=1, height=9)
        self.rightButton["command"] = lambda: self.rightButtonHandler()

    def createLayout(self):
        # layout the widgets
        self.leftButton.pack(side="left")
        self.adsContainer.pack(side="left")
        self.rightButton.pack(side="left")

    def leftButtonHandler(self):
        if self.adsContainer.startAdIndex > 0:
            self.adsContainer.startAdIndex -= 1
            self.adsContainer.moveAdContainer()

    def rightButtonHandler(self):
        if (
            self.adsContainer.startAdIndex
            < len(contractData.ads) - self.adsContainer.nofAds
        ):
            self.adsContainer.startAdIndex += 1
            self.adsContainer.moveAdContainer()

    def updateAdsContainer(self):
        self.adsContainer.updateAdWidgets()
