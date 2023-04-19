from scripts.gui.adFrame import adFrame
from scripts.gui.bidFrame import bidFrame
from scripts.gui.approvedBidFrame import approvedBidFrame
from scripts.gui.offerFrame import offerFrame
from scripts.gui.serviceFrame import serviceFrame
from scripts.gui.Container import Container
from scripts.data import contractData


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
        height=130,
        dataFunc=GUIAllBids,
        frameClass=bidFrame,
        widgetDataFunc=bidWidgetDataUpdateFunc,
    )
    return container


# Approved Bids Container
def GUIAllApprovedBids():
    return contractData.yourOrders


def approvedBidWidgetDataUpdateFunc(approvedBidWidget, approvedBid):
    approvedBidWidget.updateWidget(approvedBid)


def createApprovedBidsContainer(parent):
    container = Container(
        parent,
        width=770,
        height=130,
        dataFunc=GUIAllApprovedBids,
        frameClass=approvedBidFrame,
        widgetDataFunc=approvedBidWidgetDataUpdateFunc,
    )
    return container


# Ads Container


def GUIYourAds():
    return contractData.yourAds


def createYourAdsContainer(parent):
    container = Container(
        parent,
        width=770,
        height=130,
        dataFunc=GUIYourAds,
        frameClass=adFrame,
        widgetDataFunc=AdWidgetDataUpdateFunc,
    )
    return container


# bidsOnYourAds Container
def GUIBidsOnYourAds():
    return contractData.bidsOnYourAds


def createBidsOnYourAdsContainer(parent):
    container = Container(
        parent,
        width=770,
        height=130,
        dataFunc=GUIBidsOnYourAds,
        frameClass=offerFrame,
        widgetDataFunc=bidWidgetDataUpdateFunc,
    )
    return container


# yourServices Container
def GUIYourServices():
    return contractData.yourServices


def offerWidgetDataUpdateFunc(offerWidget, bid):
    print("Called the offerWidgetDataUpdateFunc")
    offerWidget.updateWidget(bid)


def createYourServicesContainer(parent):
    container = Container(
        parent,
        width=770,
        height=130,
        dataFunc=GUIYourServices,
        frameClass=serviceFrame,
        widgetDataFunc=offerWidgetDataUpdateFunc,
    )
    return container
