from chipnetapp.contract.getters import isYourAd
from chipnetapp.service.serviceWorker import newService
from chipnetapp.data import contractData
import time
import threading


def handleBidApprovedEvent(event):
    bidIndex = event.args["bidIndex"]
    adIndex = contractData.allBids[bidIndex].adIndex
    if isYourAd(adIndex):
        while True:
            contractData.updateAll()
            if len(contractData.allServices) >= event.args["serviceIndex"]:
                break
            else:
                print("Waiting for contractData to be updated")
                time.sleep(3)
        print("A bid is approved")
        print(f"\nEvent triggered with arguments: {event.args}\n")
        serviceIndex = event.args["serviceIndex"]

        def threadFunction():
            print("Thread started")
            newService(serviceIndex)

        # Create a new thread and start it
        thread = threading.Thread(target=threadFunction)
        thread.start()
