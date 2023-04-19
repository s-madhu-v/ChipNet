from scripts.data import chipnetEvents
from scripts.events.sellerEvents import handleNewBidEvent, handleBidApprovedEvent

chipnetEvents.subscribe("newBid", handleNewBidEvent)
chipnetEvents.subscribe("bidApproved", handleBidApprovedEvent)
