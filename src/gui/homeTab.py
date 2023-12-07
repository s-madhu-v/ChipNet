import tkinter as tk
from src.style import myStyle


# create a home page
class homePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self["bg"] = "#FEE8B0"
        self.createWidgets()

    def createWidgets(self):
        self.label = tk.Label(self, text="ChipNet", font=myStyle.homePageFont)
        self.label["bg"] = "#FEE8B0"
        self.madeBy = tk.Label(self, text="Made by:", font=("American Typewriter", 50))
        self.madeBy["bg"] = "#FEE8B0"
        self.madhu = tk.Label(self, text="» Madhu", font=("American Typewriter", 40))
        self.madhu["bg"] = "#FEE8B0"
        self.label.pack()
        self.madeBy.pack()
        self.madhu.pack()
