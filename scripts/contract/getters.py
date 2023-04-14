from scripts.data import deployedChipnet


def getAllAds():
    return deployedChipnet.getAllAds()


def getBidsOf(account):
    return deployedChipnet.getPurchases(account)


def getAd(index):
    return deployedChipnet.getAd(index)
