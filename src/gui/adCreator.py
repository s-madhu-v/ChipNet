import tkinter as tk
from tkinter import ttk
from brownie import Wei
from src.contract.setters import postAd


class adCreator(ttk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            width=400,
            height=400,
            relief="raised",
        )
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()

    def createWidgets(self):
        # create the widgets
        self.titleLabel = tk.Label(self, text="Title")
        self.titleEntry = tk.Entry(self)
        self.coresLabel = tk.Label(self, text="Cores")
        self.coresEntry = tk.Entry(self)
        self.memoryLabel = tk.Label(self, text="Memory")
        self.memoryEntry = tk.Entry(self)
        self.storageLabel = tk.Label(self, text="Storage")
        self.storageEntry = tk.Entry(self)
        self.priceLabel = tk.Label(self, text="PricePerHour")
        self.priceEntry = tk.Entry(self)
        self.createButton = tk.Button(self, text="Create")

        # layout the widgets
        self.titleLabel.pack()
        self.titleEntry.pack()
        self.coresLabel.pack()
        self.coresEntry.pack()
        self.memoryLabel.pack()
        self.memoryEntry.pack()
        self.storageLabel.pack()
        self.storageEntry.pack()
        self.priceLabel.pack()
        self.priceEntry.pack()
        self.createButton.pack()
        self.createButton["command"] = self.createAd

    def createAd(self):
        title = self.titleEntry.get()
        price = self.priceEntry.get()
        cores = self.coresEntry.get()
        memory = self.memoryEntry.get()
        storage = self.storageEntry.get()
        if price.isdigit():
            price += " finney"
        postAd(title, cores, memory, storage, Wei(price.lower()))
