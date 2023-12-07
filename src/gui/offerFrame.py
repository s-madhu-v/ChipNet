import tkinter as tk
from src.app import getTheApp
from src.gui.adFrame import adFrame
from src.contract.setters import approveBid
from src.style import myStyle


class offerFrame(adFrame):
    def __init__(self, parent, bid):
        self.bid = bid
        self.ad = getTheApp().contractData.allAds[bid.adIndex]
        self.totalPrice = self.bid.noOfHours * self.ad.pricePerHour
        super().__init__(
            parent,
            self.ad,
            width=myStyle.offerFrameWidth,
            height=myStyle.offerFrameHeight,
        )

    def createWidgets(self):
        super().createWidgets()
        self.hours = tk.Label(
            self,
            text=f"Hours            :   {self.bid.noOfHours}",
            font=myStyle.attributeFont,
            anchor="w",
        )
        self.totalPriceLabel = tk.Label(
            self,
            text=f"Total Price   :   {(self.totalPrice)/(10**15)} Finney",
            font=myStyle.attributeFont,
            anchor="w",
        )
        self.approveButton = tk.Button(
            self, text="Approve", command=self.approveBidHandler
        )
        if self.bid.approved:
            self.approveButton["text"] = "Approved"
            self.approveButton["state"] = "disabled"

    def layoutWidgets(self):
        self.hours.grid(row=0, column=0, sticky="nsew")
        self.hours["bg"] = myStyle.offerHoursColor
        self.totalPriceLabel.grid(row=1, column=0, sticky="nsew")
        self.totalPriceLabel["bg"] = myStyle.offerTotalPriceColor
        self.approveButton.grid(row=2, column=0, sticky="nsew")
        self.approveButton.configure(bg=myStyle.offerApproveButtonColor)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

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
