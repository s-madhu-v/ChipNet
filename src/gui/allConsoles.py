from src.gui.allContainers import (
    createAdsContainer,
    createBidsContainer,
    createApprovedBidsContainer,
    createYourAdsContainer,
    createBidsOnYourAdsContainer,
    createYourServicesContainer,
)
from src.gui.Console import Console
from src.style import myStyle


# Ads Console
def createAdConsole(parent):
    return Console(
        parent, createAdsContainer, "Marketplace", height=myStyle.adsConsoleHeight
    )


# Bids Console
def createBidConsole(parent):
    return Console(
        parent, createBidsContainer, "Your Bids", height=myStyle.bidsConsoleHeight
    )


# Approved Bids Console
def createApprovedBidConsole(parent):
    return Console(
        parent,
        createApprovedBidsContainer,
        "Approved Bids",
        height=myStyle.approvedBidsConsoleHeight,
    )


# create a yourAdsConsole
def createYourAdsConsole(parent):
    return Console(
        parent, createYourAdsContainer, "Your Ads", height=myStyle.yourAdsConsoleHeight
    )


# bidsOnYourAds Console
def createBidsOnYourAdsConsole(parent):
    return Console(
        parent,
        createBidsOnYourAdsContainer,
        "Bids On Your Ads",
        height=myStyle.bidsOnYourAdsConsoleHeight,
    )


# yourServices Console
def createYourServicesConsole(parent):
    return Console(
        parent,
        createYourServicesContainer,
        "Your Services",
        height=myStyle.servicesConsoleHeight,
    )
