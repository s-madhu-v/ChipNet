from chipnetapp.data import chipnetEvents
from chipnetapp.events.sellerEvents import handleBidApprovedEvent


def listen():
    # chipnetEvents.subscribe("newBid", handleNewBidEvent)
    chipnetEvents.subscribe("bidApproved", handleBidApprovedEvent)
