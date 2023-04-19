import tkinter as tk
from scripts.data import contractData
from scripts.gui.adFrame import adFrame
from scripts.contract.setters import cancelBid


class bidFrame(adFrame):
    def __init__(self, parent, bid):
        self.bid = bid
        self.ad = contractData.allAds[bid.adIndex]
        super().__init__(parent, self.ad, width=210, height=160)

    def createWidgets(self):
        super().createWidgets()
        # TODO: update this later to update itself
        self.status = tk.Label(self, text="Status: Active")
        self.cancelButton = tk.Button(self, text="Cancel", command=self.cancelBid)

    def layoutWidgets(self):
        self.title.grid(row=0, column=0, sticky="nsew")
        self.title["bg"] = "blue"
        self.price.grid(row=1, column=0, sticky="nsew")
        self.price["bg"] = "yellow"
        self.status.grid(row=2, column=0, sticky="nsew")
        self.status["bg"] = "green"
        self.cancelButton.grid(row=3, column=0, sticky="nsew")
        self.cancelButton["bg"] = "red"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

    def cancelBid(self):
        print("Cancel Bid")
        cancelBid(self.bid.index)

    def updateWidget(self, bid):
        self.bid = bid
        super().updateWidget(contractData.allAds[bid.adIndex])
        # update status here...
