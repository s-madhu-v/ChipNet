import tkinter as tk
from tkinter import ttk
from scripts.contract.setters import postAd
from scripts.data import myAddress

adCreatorbackground = "red"


class adCreator(ttk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            width=860,
            height=170,
            relief="raised",
        )
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()
        ttk.Style().configure("createAd.TFrame", background=adCreatorbackground)
        self["style"] = "createAd.TFrame"

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
        postAd(title, price, myAddress)
