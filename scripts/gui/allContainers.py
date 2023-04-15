import tkinter as tk
from tkinter import ttk
from scripts.gui.adFrame import adFrame
from scripts.gui.Container import Container
from scripts.data import contractData
from scripts.gui.bidFrame import bidFrame


# Ads Container
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


# Bids Container
bidsContainerbackground = "yellow"


def GUIAllBids():
    return contractData.yourBids


def bidWidgetDataUpdateFunc(bidWidget, bid):
    bidWidget.updateWidget(bid)


def createBidsContainer(parent):
    container = Container(
        parent,
        width=770,
        height=200,
        dataFunc=GUIAllBids,
        updateFunc=contractData.updateYourBids,
        frameClass=bidFrame,
        widgetDataFunc=bidWidgetDataUpdateFunc,
    )
    return container
