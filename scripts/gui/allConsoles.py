import tkinter as tk
from tkinter import ttk
from scripts.gui.allContainers import (
    createAdsContainer,
    createBidsContainer,
    createApprovedBidsContainer,
)
from scripts.gui.Console import Console

# Ads Console

adConsolebackground = "blue"


def createAdConsole(parent):
    return Console(parent, createAdsContainer)


# Bids Console
bidConsolebackground = "pink"


def createBidConsole(parent):
    return Console(parent, createBidsContainer)


# Approved Bids Console
approvedBidConsolebackground = "white"


def createApprovedBidConsole(parent):
    return Console(parent, createApprovedBidsContainer)
