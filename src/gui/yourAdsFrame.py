import time
import tkinter as tk
import tkinter.simpledialog as sd
from tkinter.messagebox import askyesno
from src.data import Ad
from src.contract.setters import bidOnAd
from src.style import myStyle


class yourAdsFrame(tk.LabelFrame):
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
        self.ad = ad
        self.createWidgets()
        self.layoutWidgets()
        self.pack_propagate(False)
        self.grid_propagate(False)

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
        self.status = tk.Label(
            self,
            text="Status       :   Not Sold",
            font=myStyle.attributeFont,
            anchor="w",
        )
        if not self.ad.active:
            self.status["text"] = "Status       :   Sold"

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
            self.status["text"] = "Status       :   Sold"
        else:
            self.status["text"] = "Status       :   Not Sold"

    def layoutWidgets(self):
        # layout the widgets
        # self.title.grid(row=0, column=0, sticky="nsew")
        # self.title["bg"] = myStyle.adFrameTitleColor
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
        self.status.grid(row=6, column=0, sticky="nsew")
        self.status["bg"] = myStyle.adFramePriceColor  # same as price color
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=2)
