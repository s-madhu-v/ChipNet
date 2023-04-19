from scripts.gui.allContainers import (
    createAdsContainer,
    createBidsContainer,
    createApprovedBidsContainer,
    createYourAdsContainer,
)
from scripts.gui.Console import Console


# Ads Console
def createAdConsole(parent):
    return Console(parent, createAdsContainer, "Marketplace")


# Bids Console
def createBidConsole(parent):
    return Console(parent, createBidsContainer, "Your Bids")


# Approved Bids Console
def createApprovedBidConsole(parent):
    return Console(parent, createApprovedBidsContainer, "Approved Bids")


# create a yourAdsConsole
def createYourAdsConsole(parent):
    return Console(parent, createYourAdsContainer, "Your Ads")
