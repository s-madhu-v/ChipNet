from myTkinter import myTk, myTtk
tk = myTk
ttk = myTtk
#import tkinter as tk
#from tkinter import ttk
from chipnetapp.gui.adCreator import adCreator


class advertise(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=860, height=170, relief="raised")
        self.createWidgets()
        ttk.Style().configure("advertise.TFrame", background="red")
        self["style"] = "advertise.TFrame"

    def createWidgets(self):
        self.adCreator = adCreator(self)
        self.adCreator.pack()
