from chipnetapp.app import getTheApp


def getAllAds():
    return getTheApp().deployedChipnet.getAllAds()


def getBidsOf(account):
    return getTheApp().deployedChipnet.getPurchases(account)


def getAd(index):
    return getTheApp().deployedChipnet.getAd(index)


def isYourAd(adIndex):
    return (
        getTheApp().contractData.allAds[adIndex].seller == getTheApp().myAccount.address
    )


# A function to get the no of hours from the service index
def getNoOfHours(serviceIndex):
    try:
        bid = getTheApp().contractData.allBids[
            getTheApp().contractData.allServices[serviceIndex].bidIndex
        ]
        return bid.noOfHours
    except:
        getTheApp().contractData.updateAll()
        bid = getTheApp().contractData.allBids[
            getTheApp().contractData.allServices[serviceIndex].bidIndex
        ]
        return bid.noOfHours
