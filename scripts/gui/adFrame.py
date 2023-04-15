import time
import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog as sd
from tkinter.messagebox import askyesno
from scripts.data import Ad, myAddress, contractData
from scripts.contract.setters import bidOnAd

adFramebackground = "green"


class adFrame(tk.Frame):
    def __init__(self, parent, ad: Ad, width=200, height=100):
        super().__init__(parent, width=width, height=height)
        self.ad = ad
        self.createWidgets()
        self.layoutWidgets()
        self.pack_propagate(False)
        self.grid_propagate(False)

    def buyThisAd(self):
        print("Bidding on an Ad..")
        self.noOfHours = sd.askstring("Hours", "How many Hours?")
        if self.noOfHours != None:
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
        self.title = tk.Label(self, text=self.ad.title, font=("Monospace", 16))
        self.price = tk.Label(self, text=f"Price: {int(self.ad.price/(10**18))} ETH")
        self.sellerAddress = tk.Label(self, text=self.ad.seller[:10])
        isactive = self.ad.isactive
        self.buyButton = tk.Button(self, text="Make a Bid", command=self.buyThisAd)
        if isactive == False:
            self.buyButton["text"] = "Sold"
            self.buyButton["state"] = "disabled"

    def updateWidget(self, ad):
        # create the widgets
        self.title["text"] = ad.title
        # handle floating point numbers
        self.price["text"] = f"Price: {int(ad.price/(10**18))} ETH"
        self.sellerAddress["text"] = ad.seller[:10]
        isactive = ad.isactive
        if isactive == False:
            self.buyButton["text"] = "Sold"
            self.buyButton["state"] = "disabled"
        else:
            self.buyButton["text"] = "Buy"
            self.buyButton["state"] = "normal"

    def layoutWidgets(self):
        # layout the widgets
        self.title.grid(row=0, column=0, sticky="nsew")
        self.title["bg"] = "blue"
        self.price.grid(row=1, column=0, sticky="nsew")
        self.price["bg"] = "yellow"
        self.sellerAddress.grid(row=2, column=0, sticky="nsew")
        self.sellerAddress["bg"] = "pink"
        self.buyButton.grid(row=3, column=0, sticky="nsew")
        self.buyButton["bg"] = "orange"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
