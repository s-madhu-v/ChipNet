from chipnetapp.data import deployedChipnet, myAccount, contractData


def getAllAds():
    return deployedChipnet.getAllAds()


def getBidsOf(account):
    return deployedChipnet.getPurchases(account)


def getAd(index):
    return deployedChipnet.getAd(index)


def isYourAd(adIndex, account=myAccount):
    return contractData.allAds[adIndex].seller == account.address


# write a function to get the no of hours from the service index
def getNoOfHours(serviceIndex):
    try:
        bid = contractData.allBids[contractData.allServices[serviceIndex].bidIndex]
        return bid.noOfHours
    except:
        contractData.updateAll()
        bid = contractData.allBids[contractData.allServices[serviceIndex].bidIndex]
        return bid.noOfHours
