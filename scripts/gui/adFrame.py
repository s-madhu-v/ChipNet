import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog as sd
from scripts.data import Ad, myAddress, contractData
from scripts.contract.setters import bidOnAd
from scripts.service.run import fakeRun

adFramebackground = "green"


class adFrame(ttk.Frame):
    def __init__(self, parent, ad: Ad):
        super().__init__(
            parent,
            padding=10,
            relief="raised",
            width=220,
            height=110,
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
        noOfHours = sd.askstring("noOfHours", "How many Hours?")
        bidOnAd(self.ad.index, myAddress, int(noOfHours))
        self.buyButton["text"] = "Bought!!!"
        contractData.updateAll()

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

    def layoutWidgets(self):
        # layout the widgets
        self.title.pack()
        self.price.pack()
        self.sellerAddress.pack()
        self.buyButton.pack()
