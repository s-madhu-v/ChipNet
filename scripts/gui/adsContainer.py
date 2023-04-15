import tkinter as tk
from tkinter import ttk
from scripts.gui.adFrame import adFrame
from scripts.gui.Container import Container
from scripts.data import contractData


adsContainerbackground = "blue"


def GUIAllAds():
    return contractData.allAds


def AdWidgetDataUpdateFunc(adWidget, ad):
    adWidget.updateWidget(ad)


def createAdsContainer(parent):
    container = Container(
        parent,
        width=770,
        height=130,
        dataFunc=GUIAllAds,
        updateFunc=contractData.updateAllAds,
        frameClass=adFrame,
        widgetDataFunc=AdWidgetDataUpdateFunc,
    )
    return container


"""
class adsContainer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=770, height=130, relief="raised", padding=10)
        self.ContainerSize = 3
        self.nofAds = min(self.ContainerSize, len(contractData.allAds))
        self.startAdIndex = 0
        self.adWidgets = []
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()
        ttk.Style().configure("adsContainer.TFrame", background=adsContainerbackground)
        self["style"] = "adsContainer.TFrame"
        self.startAdIndx = 0  # remove this later; indentaion issues?
        print(f"\n\n====={self.nofAds}=====\n\n")  # this too

    def createWidgets(self):
        contractData.updateAllAds()
        for i in range(self.nofAds):
            widget = adFrame(self, contractData.allAds[self.startAdIndex + i])
            self.adWidgets.append(widget)
            widget.pack(side="left", padx=10)

    def handleNoOfAdsChange(self):
        self.nofAds = min(self.ContainerSize, len(contractData.allAds))
        if self.nofAds < len(self.adWidgets):
            for i in range(self.nofAds, len(self.adWidgets)):
                self.adWidgets[i].destroy()
            self.adWidgets = self.adWidgets[: self.nofAds]
        elif self.nofAds > len(self.adWidgets):
            for i in range(len(self.adWidgets), self.nofAds):
                widget = adFrame(self, contractData.allAds[self.startAdIndex + i])
                self.adWidgets.append(widget)
                widget.pack(side="left", padx=10)

    def moveAdContainer(self):
        self.handleNoOfAdsChange()
        for i in range(self.nofAds):
            self.adWidgets[i].ad = contractData.allAds[self.startAdIndex + i]
            self.adWidgets[i].title["text"] = self.adWidgets[i].ad.title
            self.adWidgets[i].price[
                "text"
            ] = f"Price: {int(self.adWidgets[i].ad.price/(10**18))} ETH"
            self.adWidgets[i].sellerAddress["text"] = self.adWidgets[i].ad.seller
            isactive = self.adWidgets[i].ad.isactive
            if isactive == False:
                self.adWidgets[i].buyButton["text"] = "Sold"
                self.adWidgets[i].buyButton["state"] = "disabled"
            else:
                self.adWidgets[i].buyButton["text"] = "Buy"
                self.adWidgets[i].buyButton["state"] = "normal"

    def updateAdWidgets(self):
        contractData.updateAllAds()
        self.moveAdContainer()
"""
