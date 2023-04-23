import tkinter as tk
from chipnetapp.app import getTheApp
from chipnetapp.gui.adFrame import adFrame
from chipnetapp.contract.setters import approveBid


class offerFrame(adFrame):
    def __init__(self, parent, bid):
        self.bid = bid
        self.ad = getTheApp().contractData.allAds[bid.adIndex]
        super().__init__(parent, self.ad, width=210, height=160)

    def createWidgets(self):
        super().createWidgets()
        self.hours = tk.Label(self, text=f"Hours: {self.bid.noOfHours}")
        self.approveButton = tk.Button(
            self, text="Approve", command=self.approveBidHandler
        )
        if self.bid.approved:
            self.approveButton["text"] = "Approved"
            self.approveButton["state"] = "disabled"

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

    def approveBidHandler(self):
        approveBid(self.bid.index)

    def updateWidget(self, bid):
        self.bid = bid
        super().updateWidget(getTheApp().contractData.allAds[bid.adIndex])
        if self.bid.approved:
            self.buyButton["text"] = "Approved"
            self.buyButton["state"] = "disabled"
        else:
            self.buyButton["text"] = "Approve"
            self.buyButton["state"] = "normal"
