import tkinter as tk
from src.style import myStyle


# create a home page
class homePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self["bg"] = myStyle.homePageColor
        self.createWidgets()

    def createWidgets(self):
        self.label = tk.Label(self, text="Home Page")
        self.label.pack()