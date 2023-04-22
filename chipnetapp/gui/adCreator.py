from myTkinter import myTk, myTtk
tk = myTk
ttk = myTtk
#import tkinter as tk
#from tkinter import ttk
from chipnetapp.contract.setters import postAd
from chipnetapp.data import myAccount


class adCreator(ttk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            width=200,
            height=200,
            relief="raised",
        )
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()

    def createWidgets(self):
        # create the widgets
        self.titleLabel = ttk.Label(self, text="Title")
        self.titleEntry = ttk.Entry(self)
        self.priceLabel = ttk.Label(self, text="Price")
        self.priceEntry = ttk.Entry(self)
        self.createButton = ttk.Button(self, text="Create")

        # layout the widgets
        self.titleLabel.pack()
        self.titleEntry.pack()
        self.priceLabel.pack()
        self.priceEntry.pack()
        self.createButton.pack()
        self.createButton["command"] = self.createAd

    def createAd(self):
        title = self.titleEntry.get()
        price = self.priceEntry.get()
        postAd(title, price, myAccount)
