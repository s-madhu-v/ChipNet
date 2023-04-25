import tkinter as tk
from src.gui.allConsoles import (
    createYourAdsConsole,
    createBidsOnYourAdsConsole,
    createYourServicesConsole,
)
from src.gui.adCreator import adCreator
from src.app import getTheApp
from src.style import myStyle


class sellPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self["bg"] = myStyle.sellPageColor
        self.createWidgets()

    def createWidgets(self):
        # create a postAdBtn
        # self.postAdBtn = postAdBtn(self)
        # self.postAdBtn.grid(row=0, column=0)
        # create a yourAdsConsole
        self.yourAdsConsole = createYourAdsConsole(self)
        self.yourAdsConsole.grid(row=1, column=0, sticky="nsew")
        # create a bidsOnYourAdsConsole
        self.bidsOnYourAdsConsole = createBidsOnYourAdsConsole(self)
        self.bidsOnYourAdsConsole.grid(row=2, column=0, sticky="nsew")
        # create a yourServicesConsole
        self.yourServicesConsole = createYourServicesConsole(self)
        self.yourServicesConsole.grid(row=3, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

    def refresh(self):
        print("refreshing")
        self.yourAdsConsole.updateFramesContainer()
        self.bidsOnYourAdsConsole.updateFramesContainer()
        self.yourServicesConsole.updateFramesContainer()
