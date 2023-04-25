from src.app import getTheApp
from src.gui.adFrame import adFrame
from src.gui.bidFrame import bidFrame
from src.gui.Container import Container
from src.gui.offerFrame import offerFrame
from src.gui.serviceFrame import serviceFrame
from src.gui.approvedBidFrame import approvedBidFrame
from src.gui.yourAdsFrame import yourAdsFrame
from src.style import myStyle


# Ads Container
def GUIAllAds():
    return getTheApp().contractData.allAds


def AdWidgetDataUpdateFunc(adWidget, ad):
    adWidget.updateWidget(ad)


def createAdsContainer(parent):
    container = Container(
        parent,
        width=myStyle.adsContainerWidth,
        height=myStyle.adsContainerHeight,
        dataFunc=GUIAllAds,
        frameClass=adFrame,
        widgetDataFunc=AdWidgetDataUpdateFunc,
    )
    return container


# Bids Container
def GUIAllBids():
    return getTheApp().contractData.yourBids


def bidWidgetDataUpdateFunc(bidWidget, bid):
    bidWidget.updateWidget(bid)


def createBidsContainer(parent):
    container = Container(
        parent,
        width=myStyle.bidsContainerWidth,
        height=myStyle.bidsContainerHeight,
        dataFunc=GUIAllBids,
        frameClass=bidFrame,
        widgetDataFunc=bidWidgetDataUpdateFunc,
    )
    return container


# Approved Bids Container
def GUIAllApprovedBids():
    return getTheApp().contractData.yourOrders


def approvedBidWidgetDataUpdateFunc(approvedBidWidget, approvedBid):
    approvedBidWidget.updateWidget(approvedBid)


def createApprovedBidsContainer(parent):
    container = Container(
        parent,
        width=myStyle.approvedBidsContainerWidth,
        height=myStyle.approvedBidsContainerHeight,
        dataFunc=GUIAllApprovedBids,
        frameClass=approvedBidFrame,
        widgetDataFunc=approvedBidWidgetDataUpdateFunc,
    )
    return container


# Ads Container


def GUIYourAds():
    return getTheApp().contractData.yourAds


def createYourAdsContainer(parent):
    container = Container(
        parent,
        width=myStyle.yourAdsContainerWidth,
        height=myStyle.yourAdsContainerHeight,
        dataFunc=GUIYourAds,
        frameClass=yourAdsFrame,
        widgetDataFunc=AdWidgetDataUpdateFunc,
    )
    return container


# bidsOnYourAds Container
def GUIBidsOnYourAds():
    return getTheApp().contractData.bidsOnYourAds


def createBidsOnYourAdsContainer(parent):
    container = Container(
        parent,
        width=myStyle.bidsOnYourAdsContainerWidth,
        height=myStyle.bidsOnYourAdsContainerHeight,
        dataFunc=GUIBidsOnYourAds,
        frameClass=offerFrame,
        widgetDataFunc=bidWidgetDataUpdateFunc,
    )
    return container


# yourServices Container
def GUIYourServices():
    return getTheApp().contractData.yourServices


def offerWidgetDataUpdateFunc(offerWidget, bid):
    print("Called the offerWidgetDataUpdateFunc")
    offerWidget.updateWidget(bid)


def createYourServicesContainer(parent):
    container = Container(
        parent,
        width=myStyle.servicesContainerWidth,
        height=myStyle.servicesContainerHeight,
        dataFunc=GUIYourServices,
        frameClass=serviceFrame,
        widgetDataFunc=offerWidgetDataUpdateFunc,
    )
    return container
