import tkinter as tk
from tkinter import ttk
from scripts.data import contractData
from scripts.gui.adFrame import adFrame


class bidFrame(adFrame):
    def __init__(self, parent, bid):
        self.ad = contractData.allAds[bid.adIndex]
        super().__init__(parent, self.ad, width=220, height=170)

    def createWidgets(self):
        super().createWidgets()
        # TODO: update this later to update itself
        self.status = ttk.Label(self, text="Status: Active")
        self.cancelButton = ttk.Button(self, text="Cancel", command=self.cancelBid)

    def layoutWidgets(self):
        super().layoutWidgets()
        self.status.pack()
        self.cancelButton.pack()
        self.buyButton.pack_forget()
        self.sellerAddress.pack_forget()

    def cancelBid(self):
        print("Cancel Bid")

    def updateWidget(self, bid):
        super().updateWidget(contractData.allAds[bid.adIndex])
