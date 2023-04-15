import tkinter as tk
from tkinter import ttk
from scripts.gui.bidFrame import bidFrame
from scripts.data import contractData

bidsContainerbackground = "yellow"


class bidsContainer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=770, height=200, relief="raised", padding=10)
        self.ContainerSize = 3
        self.nofBids = min(self.ContainerSize, len(contractData.yourBids))
        self.startBidIndex = 0
        self.bidWidgets = []
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()
        ttk.Style().configure(
            "bidsContainer.TFrame", background=bidsContainerbackground
        )
        self["style"] = "bidsContainer.TFrame"
        self.startBidIndx = 0  # remove this later; indentaion issues?
        print(f"\n\n=====Remove Me. I am annoying=====\n\n")  # this too

    def createWidgets(self):
        contractData.updateAll()
        for i in range(self.nofBids):
            bid = contractData.yourBids[self.startBidIndex + i]
            widget = bidFrame(self, bid)
            self.bidWidgets.append(widget)
            widget.pack(side="left", padx=10)

    def handleNoOfBidsChange(self):
        self.nofBids = min(self.ContainerSize, len(contractData.yourBids))
        if self.nofBids < len(self.bidWidgets):
            for i in range(self.nofBids, len(self.bidWidgets)):
                self.bidWidgets[i].destroy()
            self.bidWidgets = self.bidWidgets[: self.nofBids]
        elif self.nofBids > len(self.bidWidgets):
            for i in range(len(self.bidWidgets), self.nofBids):
                bid = contractData.yourBids[self.startBidIndex + i]
                widget = bidFrame(self, bid)
                self.bidWidgets.append(widget)
                widget.pack(side="left", padx=10)

    def moveBidsContainer(self):
        self.handleNoOfBidsChange()
        for i in range(self.nofBids):
            bid = contractData.yourBids[self.startBidIndex + i]
            self.bidWidgets[i].ad = contractData.allAds[bid.adIndex]
            self.bidWidgets[i].title["text"] = self.bidWidgets[i].ad.title
            self.bidWidgets[i].price[
                "text"
            ] = f"Price: {int(self.bidWidgets[i].ad.price/(10**18))} ETH"
            self.bidWidgets[i].sellerAddress["text"] = self.bidWidgets[i].ad.seller
            isactive = self.bidWidgets[i].ad.isactive

    def updateBidWidgets(self):
        contractData.updateAll()
        self.moveBidsContainer()
