from brownie import ChipNet, accounts
import os

contractAddress = os.getenv("CONTRACT_ADDRESS")
deployedChipnet = ChipNet.at(contractAddress)
myAddress = accounts[0]
myAccount = accounts.at(myAddress)
sellAccount = accounts[8]
buyAccount = accounts[9]


class Ad:
    def __init__(self, index, title, price, seller, isactive) -> None:
        self.index = index
        self.title = title
        self.price = price
        self.seller = seller
        self.isactive = isactive


class Bid:
    def __init__(self, index, adIndex, noOfHours, isApproved, isactive) -> None:
        self.index = index
        self.adIndex = adIndex
        self.noOfHours = noOfHours
        self.isApproved = isApproved
        self.isactive = isactive


class service:
    def __init__(
        self,
        index,
        adIndex,
        bidIndex,
        accessLink,
        password,
        SOSTimestamp,
        EOSTimestamp,
        isactive,
    ) -> None:
        self.index = index
        self.adIndex = adIndex
        self.bidIndex = bidIndex
        self.accessLink = accessLink
        self.password = password
        self.SOSTimestamp = SOSTimestamp
        self.EOSTimestamp = EOSTimestamp
        self.isactive = isactive


# convert ad array to Ad objects
def convertAds(ads):
    adObjects = []
    for ad in ads:
        adObjects.append(Ad(ad[0], ad[1], ad[2], ad[3], ad[4]))
    return adObjects


# convert bid array to Bid objects
def convertBids(bids):
    bidObjects = []
    for bid in bids:
        bidObjects.append(Bid(bid[0], bid[1], bid[4], bid[6], bid[7]))
    return bidObjects


def convertServices(services):
    serviceObjects = []
    for service in services:
        serviceObjects.append(
            service(
                service[0],
                service[1],
                service[2],
                service[3],
                service[4],
                service[5],
                service[6],
                service[7],
            )
        )
    return serviceObjects


class Data:
    def __init__(self) -> None:
        self.allAds = []
        self.allBids = []
        self.allServices = []
        self.yourAds = []
        self.yourBids = []
        self.approvedBids = []
        self.updateAll()

    def updateAllAds(self):
        self.allAds = convertAds(deployedChipnet.getAllAds())

    # def updateAllBids(self):
    #     self.allBids = convertBids(deployedChipnet.getAllBids())

    # def updateAllServices(self):
    #     self.allServices = convertServices(deployedChipnet.getAllServices())

    def updateYourAds(self, account):
        self.yourAds = convertAds(deployedChipnet.getAdsOf(account))

    def updateYourBids(self, account):
        self.yourBids = convertBids(deployedChipnet.getBidsOf(account))

    def updateApprovedBids(self, account):
        self.updateYourBids(account)
        self.approvedBids = []
        for bid in self.yourBids:
            if bid.isApproved:
                self.approvedBids.append(bid)

    def updateUserSpecificData(self, account=buyAccount):
        self.updateYourAds(account)
        self.updateYourBids(account)
        self.updateApprovedBids(account)

    def updateAll(self):
        self.updateAllAds()
        # self.updateAllBids()
        # self.updateAllServices()
        self.updateUserSpecificData()


contractData = Data()
