import time
import threading
from chipnetapp.app import getTheApp
from chipnetapp.contract.getters import isYourAd
from chipnetapp.service.serviceWorker import newService


def handleBidApprovedEvent(event):
    bidIndex = event.args["bidIndex"]
    adIndex = getTheApp().contractData.allBids[bidIndex].adIndex
    if isYourAd(adIndex):
        while True:
            getTheApp().contractData.updateAll()
            if len(getTheApp().contractData.allServices) >= event.args["serviceIndex"]:
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
