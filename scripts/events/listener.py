from scripts.data import chipnetEvents
from scripts.events.sellerEvents import handleBidApprovedEvent


def listen():
    # chipnetEvents.subscribe("newBid", handleNewBidEvent)
    chipnetEvents.subscribe("bidApproved", handleBidApprovedEvent)
