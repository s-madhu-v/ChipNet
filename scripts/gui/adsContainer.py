import tkinter as tk
from tkinter import ttk
from scripts.gui.adFrame import adFrame
from scripts.data import contractData


adsContainerbackground = "blue"


class adsContainer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=770, height=130, relief="raised", padding=10)
        self.nofAds = 3
        self.startAdIndex = 0
        self.adWidgets = []
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()
        ttk.Style().configure("adsContainer.TFrame", background=adsContainerbackground)
        self["style"] = "adsContainer.TFrame"
        self.startAdIndx = 0  # remove this later; indentaion issues?
        print(f"\n\n====={self.nofAds}=====\n\n")  # this too

    def createWidgets(self):
        contractData.updateAds()
        for i in range(self.nofAds):
            widget = adFrame(self, contractData.ads[self.startAdIndex + i])
            self.adWidgets.append(widget)
            widget.pack(side="left", padx=10)

    def moveAdContainer(self):
        for i in range(self.nofAds):
            self.adWidgets[i].ad = contractData.ads[self.startAdIndex + i]
            self.adWidgets[i].title["text"] = self.adWidgets[i].ad.title
            self.adWidgets[i].price[
                "text"
            ] = f"Price: {int(self.adWidgets[i].ad.price/(10**18))} ETH"
            self.adWidgets[i].sellerAddress["text"] = self.adWidgets[i].ad.seller
            isactive = self.adWidgets[i].ad.isactive
            if isactive == False:
                self.adWidgets[i].buyButton["text"] = "Sold"
                self.adWidgets[i].buyButton["state"] = "disabled"
            else:
                self.adWidgets[i].buyButton["text"] = "Buy"
                self.adWidgets[i].buyButton["state"] = "normal"

    def updateAdWidgets(self):
        contractData.updateAds()
        self.moveAdContainer()
