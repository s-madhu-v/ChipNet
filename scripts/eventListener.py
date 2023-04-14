from brownie import accounts, ChipNet, web3, network
import time
import os
from scripts.data import deployedChipnet, sellAccount, buyAccount
from scripts.service.run import run
from scripts.service.serviceWorker import runService
from scripts.contract.setters import approveBid
import threading

def handleNewBid(event):
    print(f"\n\n\n\nEvent triggered with arguments: {event.args}\n\n\n\n")
    approveBid(event.args["bidIndex"], sellAccount)
    print("\n\n\n\n***Bid Approved***\n\n\n\n")

serviceIndex = 0

def threadFunction():
    print("Thread started")
    runService(serviceIndex)

def handleBidApproved(event):
    print(f"\n\n\n\nEvent triggered with arguments: {event.args}\n\n\n\n")
    global serviceIndex
    serviceIndex = event.args["serviceIndex"]
    # Create a new thread and start it
    thread = threading.Thread(target=threadFunction)
    thread.start()

chipnetEvents = network.contract.ContractEvents(deployedChipnet)


chipnetEvents.subscribe("newBid", handleNewBid)
chipnetEvents.subscribe("bidApproved", handleBidApproved)

print("\nEvent Listerer Started:\n")
while True:
    time.sleep(1)
