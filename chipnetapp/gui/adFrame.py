import time
from myTkinter import myTk, myTtk, mySd, myAskYesNo

tk = myTk
ttk = myTtk
sd = mySd
askyesno = myAskYesNo
# import tkinter as tk
# from tkinter import ttk
# import tkinter.simpledialog as sd
# from tkinter.messagebox import askyesno
from chipnetapp.data import Ad, getMyAccount
from chipnetapp.contract.setters import bidOnAd

adFramebackground = "green"


class adFrame(tk.Frame):
    def __init__(self, parent, ad: Ad, width=210, height=160):
        super().__init__(parent, width=width, height=height)
        self.ad = ad
        self.createWidgets()
        self.layoutWidgets()
        self.pack_propagate(False)
        self.grid_propagate(False)

    def buyThisAd(self):
        print("Bidding on an Ad..")
        noOfHours = sd.askstring("Hours", "How many Hours?")
        if noOfHours != None:
            self.confirmBid(noOfHours)

    def confirmBid(self, noOfHours):
        answer = askyesno(
            title="Confirmation",
            message="Are you sure you want to make Bid on this Ad?",
        )
        if answer:
            bidOnAd(self.ad.index, getMyAccount(), int(noOfHours))
            self.buyButton["text"] = "Bid Submitted"
            time.sleep(1)
        else:
            print("Bid Cancelled")

    def createWidgets(self):
        # create the widgets
        self.title = tk.Label(self, text=self.ad.title, font=("Monospace", 16))
        self.price = tk.Label(
            self, text=f"Price: {int(self.ad.pricePerHour/(10**18))} ETH"
        )
        self.sellerAccount = tk.Label(self, text=self.ad.seller[:10])
        self.buyButton = tk.Button(self, text="Make a Bid", command=self.buyThisAd)
        if not self.ad.active:
            self.buyButton["text"] = "Sold"
            self.buyButton["state"] = "disabled"

    def updateWidget(self, ad):
        # create the widgets
        self.ad = ad
        self.title["text"] = ad.title
        # handle floating point numbers
        self.price["text"] = f"Price: {int(ad.pricePerHour/(10**18))} ETH"
        self.sellerAccount["text"] = ad.seller[:10]
        if not ad.active:
            self.buyButton["text"] = "Sold"
            self.buyButton["state"] = "disabled"
        else:
            self.buyButton["text"] = "Make a Bid"
            self.buyButton["state"] = "normal"

    def layoutWidgets(self):
        # layout the widgets
        self.title.grid(row=0, column=0, sticky="nsew")
        self.title["bg"] = "blue"
        self.price.grid(row=1, column=0, sticky="nsew")
        self.price["bg"] = "yellow"
        self.sellerAccount.grid(row=2, column=0, sticky="nsew")
        self.sellerAccount["bg"] = "pink"
        self.buyButton.grid(row=3, column=0, sticky="nsew")
        self.buyButton["bg"] = "orange"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
