from myTkinter import myTk, myTtk
tk = myTk
#ttk = myTtk
#import tkinter as tk


# create a home page
class homePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.createWidgets()

    def createWidgets(self):
        self.label = tk.Label(self, text="Home Page")
        self.label.pack()
