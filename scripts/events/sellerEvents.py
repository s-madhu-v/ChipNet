from scripts.contract.getters import isYourAd
from scripts.service.serviceWorker import newService
import threading


def handleNewBidEvent(event):
    if isYourAd(event.args["adIndex"]):
        print("There's a new bid on your ad")
        print(f"\nEvent triggered with arguments: {event.args}\n")
        # approveBid(event.args["bidIndex"], myAccount)


def handleBidApprovedEvent(event):
    print("A bid is approved")
    print(f"\nEvent triggered with arguments: {event.args}\n")
    serviceIndex = event.args["serviceIndex"]

    def threadFunction():
        print("Thread started")
        newService(serviceIndex)

    # Create a new thread and start it
    thread = threading.Thread(target=threadFunction)
    thread.start()
