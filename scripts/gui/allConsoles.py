import tkinter as tk
from tkinter import ttk
from scripts.gui.allContainers import createAdsContainer, createBidsContainer
from scripts.gui.Console import Console

# Ads Console

adConsolebackground = "red"


def createAdConsole(parent):
    return Console(parent, createAdsContainer)


# Bids Console
bidConsolebackground = "red"


def createBidConsole(parent):
    return Console(parent, createBidsContainer)
