import tkinter as tk
from src.app import getTheApp
from src.gui.adFrame import adFrame
from src.contract.setters import cancelBid
from src.style import myStyle


class bidFrame(adFrame):
    def __init__(self, parent, bid):
        self.bid = bid
        self.ad = getTheApp().contractData.allAds[bid.adIndex]
        self.totalPrice = self.bid.noOfHours * self.ad.pricePerHour
        super().__init__(
            parent, self.ad, width=myStyle.bidFrameWidth, height=myStyle.bidFrameHeight
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
        # TODO: update this later to update itself
        self.status = tk.Label(
            self,
            text="Status           :   Active",
            font=myStyle.attributeFont,
            anchor="w",
        )
        self.cancelButton = tk.Button(
            self, text="Cancel", command=self.cancelBid, bg="red"
        )

    def layoutWidgets(self):
        # self.title.grid(row=0, column=0, sticky="nsew")
        # self.title["bg"] = myStyle.bidTitleColor
        # self.price.grid(row=1, column=0, sticky="nsew")
        # self.price["bg"] = myStyle.bidPriceColor
        self.hours.grid(row=0, column=0, sticky="nsew")
        self.hours["bg"] = myStyle.bidHoursColor
        self.totalPriceLabel.grid(row=1, column=0, sticky="nsew")
        self.totalPriceLabel["bg"] = myStyle.bidTotalPriceColor
        self.status.grid(row=2, column=0, sticky="nsew")
        self.status["bg"] = myStyle.bidStatusColor
        self.cancelButton.grid(row=3, column=0, sticky="nsew")
        self.cancelButton["bg"] = myStyle.bidCancelButtonColor
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

    def cancelBid(self):
        print("Cancelling Bid")
        cancelBid(self.bid.index)

    def updateWidget(self, bid):
        self.bid = bid
        super().updateWidget(getTheApp().contractData.allAds[bid.adIndex])
        # update status here...
