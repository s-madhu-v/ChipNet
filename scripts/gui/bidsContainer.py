import tkinter as tk
from tkinter import ttk
from scripts.gui.bidFrame import bidFrame
from scripts.data import contractData
from scripts.gui.Container import Container

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
