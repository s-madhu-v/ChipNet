import time
import threading
from src.app import getTheApp
from src.contract.getters import isYourAd
from src.service.serviceWorker import newService


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
            newService(serviceIndex, adIndex)

        # Create a new thread and start it
        thread = threading.Thread(target=threadFunction)
        thread.start()
