from brownie import ChipNet, accounts
import os

contractAddress = os.getenv("CONTRACT_ADDRESS")
deployedChipnet = ChipNet.at(contractAddress)


class Ad:
    def __init__(self, index, title, price, seller, isactive) -> None:
        self.index = index
        self.title = title
        self.price = price
        self.seller = seller
        self.isactive = isactive


# convert ad array to Ad objects
def convertAds(ads):
    adObjects = []
    for ad in ads:
        adObjects.append(Ad(ad[0], ad[1], ad[2], ad[3], ad[4]))
    return adObjects


class Data:
    def __init__(self) -> None:
        self.ads = []

    def updateAds(self):
        self.ads = convertAds(deployedChipnet.getAllAds())

    def updateAll(self):
        self.updateAds()


contractData = Data()
myAddress = accounts[0]
myAccount = accounts.at(myAddress)
sellAccount = accounts[8]
buyAccount = accounts[9]
