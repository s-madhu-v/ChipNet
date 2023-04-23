from chipnetapp.gui.adFrame import adFrame
from chipnetapp.gui.bidFrame import bidFrame
from chipnetapp.gui.approvedBidFrame import approvedBidFrame
from chipnetapp.gui.offerFrame import offerFrame
from chipnetapp.gui.serviceFrame import serviceFrame
from chipnetapp.gui.Container import Container
from chipnetapp.app import getTheApp


# Ads Container
adsContainerbackground = "blue"


def GUIAllAds():
    return getTheApp().contractData.allAds


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
    return getTheApp().contractData.yourBids


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
    return getTheApp().contractData.yourOrders


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
    return getTheApp().contractData.yourAds


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
