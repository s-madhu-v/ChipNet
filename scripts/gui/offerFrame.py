import tkinter as tk
from scripts.data import contractData
from scripts.gui.adFrame import adFrame


class offerFrame(adFrame):
    def __init__(self, parent, bid):
        self.bid = bid
        self.ad = contractData.allAds[bid.adIndex]
        super().__init__(parent, self.ad, width=210, height=160)

    def createWidgets(self):
        super().createWidgets()
        self.hours = tk.Label(self, text=f"Hours: {self.bid.noOfHours}")
        self.approveButton = tk.Button(self, text="Approve", command=self.approveBid)
        if self.bid.isApproved:
            self.buyButton["text"] = "Approved"
            self.buyButton["state"] = "disabled"

    def layoutWidgets(self):
        self.title.grid(row=0, column=0, sticky="nsew")
        self.title["bg"] = "blue"
        self.price.grid(row=1, column=0, sticky="nsew")
        self.price["bg"] = "yellow"
        self.hours.grid(row=2, column=0, sticky="nsew")
        self.hours["bg"] = "green"
        self.approveButton.grid(row=3, column=0, sticky="nsew")
        self.approveButton["bg"] = "red"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

    def approveBid(self):
        print("fake approving Bid")

    def updateWidget(self, bid):
        super().updateWidget(contractData.allAds[bid.adIndex])
        if self.bid.isApproved:
            self.buyButton["text"] = "Approved"
            self.buyButton["state"] = "disabled"
        else:
            self.buyButton["text"] = "Approved"
            self.buyButton["state"] = "normal"
