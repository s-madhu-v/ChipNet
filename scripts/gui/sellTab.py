import tkinter as tk
from scripts.gui.allConsoles import createYourAdsConsole
from scripts.gui.adCreator import adCreator
from scripts.gui.root import root


def createNewWindow():
    new_window = tk.Toplevel(root)
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
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.refresh()

    def refresh(self):
        print("refreshing")
        self.yourAdsConsole.updateFramesContainer()