import tkinter as tk
from src.gui.allConsoles import (
    createYourAdsConsole,
    createBidsOnYourAdsConsole,
    createYourServicesConsole,
)
from src.gui.adCreator import adCreator
from src.app import getTheApp


def createNewWindow():
    new_window = tk.Toplevel(getTheApp().root)
    new_window.title("New Window")
    new_window.geometry("200x200+200+200")
    adCreatorFrame = adCreator(new_window)
    adCreatorFrame.grid(row=0, column=0, sticky="nsew")


class postAdBtn(tk.Button):
    def __init__(self, parent):
        super().__init__(parent)
        self.createWidgets()

    def createWidgets(self):
        self["text"] = "Post Ad"
        self["command"] = createNewWindow
        self.grid(row=0, column=0, padx=5, pady=5)

    def postAd(self):
        print("postAd")


class sellPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.createWidgets()

    def createWidgets(self):
        # create a postAdBtn
        self.postAdBtn = postAdBtn(self)
        self.postAdBtn.grid(row=0, column=0, padx=5, pady=5)
        # create a yourAdsConsole
        self.yourAdsConsole = createYourAdsConsole(self)
        self.yourAdsConsole.grid(row=1, column=0, pady=5, sticky="nsew")
        # create a bidsOnYourAdsConsole
        self.bidsOnYourAdsConsole = createBidsOnYourAdsConsole(self)
        self.bidsOnYourAdsConsole.grid(row=2, column=0, pady=5, sticky="nsew")
        # create a yourServicesConsole
        self.yourServicesConsole = createYourServicesConsole(self)
        self.yourServicesConsole.grid(row=3, column=0, pady=5, sticky="nsew")
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
