import time
import tkinter as tk
import tkinter.simpledialog as sd
from src.data import Ad
from src.contract.setters import bidOnAd
from src.style import myStyle
from src.service.docker_configurator import show_docker_configurator


class adFrame(tk.LabelFrame):
    def __init__(
        self,
        parent,
        ad: Ad,
        width=myStyle.adFrameWidth,
        height=myStyle.adFrameHeight,
        text="Not assigned",
        font=myStyle.adTitleFont,
    ):
        super().__init__(parent, width=width, height=height, text=ad.title, font=font)
        self.configure(background=myStyle.containerBgColor)
        # self["bg"] = myStyle.adFramebg
        self.ad = ad
        self.createWidgets()
        self.layoutWidgets()
        self.pack_propagate(False)
        self.grid_propagate(False)
    
    def sendBid(self, template):
        bidOnAd(self.ad.index, template)
        self.buyButton["text"] = "Bid Submitted"
        time.sleep(1)

    def buyThisAd(self, event):
        print("attempting to buying this ad...")
        if self.ad.active:
            print("Bidding on an Ad..")
            show_docker_configurator(self.sendBid)
        else:
            print("Already Sold!!!")

    def createWidgets(self):
        # create the widgets
        self.title = tk.Label(
            self, text=self.ad.title, font=myStyle.attributeFont, anchor="w"
        )
        self.power = tk.Label(
            self,
            text=f"Processor :   {self.ad.processingPower}",
            font=myStyle.attributeFont,
            anchor="w",
        )
        self.cores = tk.Label(
            self,
            text=f"Cores         :   {self.ad.coresAllocation}",
            font=myStyle.attributeFont,
            anchor="w",
        )
        self.memory = tk.Label(
            self,
            text=f"Memory    :   {self.ad.memoryAllocation}",
            font=myStyle.attributeFont,
            anchor="w",
        )
        self.storage = tk.Label(
            self,
            text=f"Storage     :   {self.ad.storageAllocation}",
            font=myStyle.attributeFont,
            anchor="w",
        )
        self.price = tk.Label(
            self,
            text=f"Price          :   {int(self.ad.pricePerHour/(10**15))} Finney",
            font=myStyle.attributeFont,
            anchor="w",
        )
        self.sellerAccount = tk.Label(
            self,
            text=f"Seller         :   {self.ad.seller[:8]}..",
            anchor="w",
            font=myStyle.attributeFont,
        )
        self.buyButton = tk.Label(self, text="MAKE A BID", font=myStyle.buyButtonFont)
        self.buyButton.bind("<Button-1>", self.buyThisAd)
        if not self.ad.active:
            self.buyButton["text"] = "Sold"

    def updateWidget(self, ad):
        # create the widgets
        self.ad = ad
        self.title["text"] = ad.title
        self.power["text"] = ad.processingPower
        self.cores["text"] = ad.coresAllocation
        self.memory["text"] = ad.memoryAllocation
        self.storage["text"] = ad.storageAllocation
        # handle floating point numbers
        self.price["text"] = f"Price: {int(ad.pricePerHour/(10**15))} finney"
        self.sellerAccount["text"] = ad.seller[:10]
        if not ad.active:
            self.buyButton["text"] = "Sold"
        else:
            self.buyButton["text"] = "MAKE A BID"

    def layoutWidgets(self):
        # layout the widgets
        self.power.grid(row=0, column=0, sticky="nsew")
        self.power["bg"] = myStyle.adFramePowerColor
        self.cores.grid(row=1, column=0, sticky="nsew")
        self.cores["bg"] = myStyle.adFrameCoresColor
        self.memory.grid(row=2, column=0, sticky="nsew")
        self.memory["bg"] = myStyle.adFrameMemoryColor
        self.storage.grid(row=3, column=0, sticky="nsew")
        self.storage["bg"] = myStyle.adFrameStorageColor
        self.price.grid(row=4, column=0, sticky="nsew")
        self.price["bg"] = myStyle.adFramePriceColor
        self.sellerAccount.grid(row=5, column=0, sticky="nsew")
        self.sellerAccount["bg"] = myStyle.adFrameSellerColor
        self.buyButton.grid(row=6, column=0, sticky="nsew", padx=5)
        self.buyButton["bg"] = myStyle.adFrameBuyButtonColor
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=2)
