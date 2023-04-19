from brownie import ChipNet, accounts, network
import os
import threading

contractAddress = os.getenv("CONTRACT_ADDRESS")
deployedChipnet = ChipNet.at(contractAddress)
chipnetEvents = network.contract.ContractEvents(deployedChipnet)
myAccount = accounts[0]
mutex = threading.Lock()


class Ad:
    def __init__(self, index, title, price, seller, active) -> None:
        self.index = index
        self.title = title
        self.pricePerHour = price
        self.seller = seller
        self.active = active


class Bid:
    def __init__(
        self,
        index,
        adIndex,
        serviceIndex,
        bidder,
        noOfHours,
        publicKey,
        approved,
        active,
    ) -> None:
        self.index = index
        self.adIndex = adIndex
        self.serviceIndex = serviceIndex
        self.bidder = bidder
        self.noOfHours = noOfHours
        self.publicKey = publicKey
        self.approved = approved
        self.active = active


class Service:
    def __init__(
        self,
        index,
        adIndex,
        bidIndex,
        serviceIndex,
        accessLink,
        password,
        SOSTimestamp,
        EOSTimestamp,
        isactive,
    ) -> None:
        self.index = index
        self.adIndex = adIndex
        self.bidIndex = bidIndex
        self.serviceIndex = serviceIndex
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
        bidObjects.append(
            Bid(
                bid[0],
                bid[1],
                bid[2],
                bid[3],
                bid[4],
                bid[5],
                bid[6],
                bid[7],
            )
        )
    return bidObjects


def convertServices(services):
    serviceObjects = []
    for service in services:
        serviceObjects.append(
            Service(
                service[0],
                service[1],
                service[2],
                service[3],
                service[4],
                service[5],
                service[6],
                service[7],
                service[8],
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
        self.yourOrders = []
        self.bidsOnYourAds = []
        self.updateAll()

    def updateAllAds(self):
        self.allAds = convertAds(deployedChipnet.getAllAds())

    def updateAllBids(self):
        self.allBids = convertBids(deployedChipnet.getAllBids())

    def updateAllServices(self):
        self.allServices = convertServices(deployedChipnet.getAllServices())

    def updateYourAds(self, account=myAccount):
        self.yourAds = []
        for ad in self.allAds:
            if ad.seller == account.address:
                self.yourAds.append(ad)

    def updateYourBids(self, account=myAccount):
        self.yourBids = []
        for bid in self.allBids:
            if bid.bidder == account.address:
                self.yourBids.append(bid)

    def updateYourOrders(self, account=myAccount):
        self.yourOrders = []
        for service in self.allServices:
            if self.allBids[service.bidIndex].bidder == account.address:
                self.yourOrders.append(service)

    def updateBidsOnYourAds(self, account=myAccount):
        self.bidsOnYourAds = []
        for bid in self.allBids:
            if (self.allAds[bid.adIndex]).seller == account.address:
                self.bidsOnYourAds.append(bid)

    def updateUserSpecificData(self, account=myAccount):
        self.updateYourAds(account)
        self.updateYourBids(account)
        self.updateYourOrders(account)
        self.updateBidsOnYourAds(account)

    def updateAll(self):
        mutex.acquire()
        self.updateAllAds()
        self.updateAllBids()
        self.updateAllServices()
        self.updateUserSpecificData()
        mutex.release()


contractData = Data()


def setInterval(func, sec):
    def func_wrapper():
        setInterval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def updater():
    contractData.updateAll()
    print("Updated All")


# update data every 10 seconds
setInterval(updater, 10)
