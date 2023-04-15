import time
import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog as sd
from tkinter.messagebox import askyesno
from scripts.data import Ad, myAddress, contractData
from scripts.contract.setters import bidOnAd

adFramebackground = "green"


class adFrame(ttk.Frame):
    def __init__(self, parent, ad: Ad, width=220, height=110):
        super().__init__(
            parent, padding=10, relief="raised", width=width, height=height
        )
        self.ad = ad
        self.createWidgets()
        self.layoutWidgets()
        ttk.Style().configure("AdFrame.TFrame", background=adFramebackground)
        self["style"] = "AdFrame.TFrame"
        self.pack_propagate(False)
        self.grid_propagate(False)

    def buyThisAd(self):
        print("Bidding on an Ad..")
        self.noOfHours = sd.askstring("Hours", "How many Hours?")
        self.confirmBid()

    def confirmBid(self):
        answer = askyesno(
            title="Confirmation",
            message="Are you sure you want to make Bid on this Ad?",
        )
        if answer:
            bidOnAd(self.ad.index, myAddress, int(self.noOfHours))
            self.buyButton["text"] = "Bid Submitted"
            time.sleep(1)
            contractData.updateAllAds()
        else:
            print("Bid Cancelled")

    def createWidgets(self):
        # create the widgets
        self.title = ttk.Label(self, text=self.ad.title)
        self.price = ttk.Label(self, text=f"Price: {int(self.ad.price/(10**18))} ETH")
        self.sellerAddress = ttk.Label(self, text=self.ad.seller)
        isactive = self.ad.isactive
        self.buyButton = tk.Button(self, text="Buy", command=self.buyThisAd)
        if isactive == False:
            self.buyButton["text"] = "Sold"
            self.buyButton["state"] = "disabled"

    def updateWidget(self, ad):
        # create the widgets
        self.title["text"] = ad.title
        # handle floating point numbers
        self.price["text"] = f"Price: {int(ad.price/(10**18))} ETH"
        self.sellerAddress["text"] = ad.seller
        isactive = ad.isactive
        if isactive == False:
            self.buyButton["text"] = "Sold"
            self.buyButton["state"] = "disabled"
        else:
            self.buyButton["text"] = "Buy"
            self.buyButton["state"] = "normal"

    def layoutWidgets(self):
        # layout the widgets
        self.title.pack()
        self.price.pack()
        self.sellerAddress.pack()
        self.buyButton.pack()
