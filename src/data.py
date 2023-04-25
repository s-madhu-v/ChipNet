import threading


def setInterval(func, sec):
    def func_wrapper():
        setInterval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


class Ad:
    def __init__(
        self,
        index,
        title,
        processingPower,
        coresAllocation,
        memoryAllocation,
        storageAllocation,
        price,
        seller,
        active,
    ) -> None:
        self.index = index
        self.title = title
        self.processingPower = processingPower
        self.coresAllocation = coresAllocation
        self.memoryAllocation = memoryAllocation
        self.storageAllocation = storageAllocation
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
        active,
    ) -> None:
        self.index = index
        self.adIndex = adIndex
        self.bidIndex = bidIndex
        self.serviceIndex = serviceIndex
        self.accessLink = accessLink
        self.password = password
        self.SOSTimestamp = SOSTimestamp
        self.EOSTimestamp = EOSTimestamp
        self.active = active


# convert ad array to Ad objects
def convertAds(ads):
    adObjects = []
    for ad in ads:
        adObjects.append(
            Ad(ad[0], ad[1], ad[2], ad[3], ad[4], ad[5], ad[6], ad[7], ad[8])
        )
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
    def __init__(self, app) -> None:
        self.app = app
        self.allAds = []
        self.allBids = []
        self.allServices = []
        self.yourAds = []
        self.yourBids = []
        self.yourOrders = []
        self.bidsOnYourAds = []
        self.yourServices = []
        self.changeMetric = [
            len(self.allAds),
            len(self.allBids),
            len(self.allServices),
        ]  # add more metrics here
        self.mutex = threading.Lock()
        setInterval(self.updater, 5)

    def isRefreshNeeded(self):
        return self.changeMetric != [
            len(self.allAds),
            len(self.allBids),
            len(self.allServices),
        ]

    def updateChangeMetric(self):
        self.changeMetric = [
            len(self.allAds),
            len(self.allBids),
            len(self.allServices),
        ]

    def updateAllAds(self):
        self.allAds = convertAds(self.app.deployedChipnet.getAllAds())

    def updateAllBids(self):
        self.allBids = convertBids(self.app.deployedChipnet.getAllBids())

    def updateAllServices(self):
        self.allServices = convertServices(self.app.deployedChipnet.getAllServices())

    def updateYourAds(self, account=None):
        if not account:
            account = self.app.myAccount
        self.yourAds = []
        for ad in self.allAds:
            if ad.seller == account.address:
                self.yourAds.append(ad)

    def updateYourBids(self, account=None):
        if not account:
            account = self.app.myAccount
        self.yourBids = []
        for bid in self.allBids:
            if bid.bidder == account.address:
                self.yourBids.append(bid)

    def updateYourOrders(self, account=None):
        if not account:
            account = self.app.myAccount
        self.yourOrders = []
        for service in self.allServices:
            if self.allBids[service.bidIndex].bidder == account.address:
                self.yourOrders.append(service)

    def updateBidsOnYourAds(self, account=None):
        if not account:
            account = self.app.myAccount
        self.bidsOnYourAds = []
        for bid in self.allBids:
            if (self.allAds[bid.adIndex]).seller == account.address:
                self.bidsOnYourAds.append(bid)

    def updateYourServices(self, account=None):
        if not account:
            account = self.app.myAccount
        self.yourServices = []
        for service in self.allServices:
            if self.allAds[service.adIndex].seller == account.address:
                self.yourServices.append(service)

    def updateUserSpecificData(self):
        self.updateYourAds()
        self.updateYourBids()
        self.updateYourOrders()
        self.updateBidsOnYourAds()
        self.updateYourServices()

    def updateAll(self):
        self.mutex.acquire()
        self.updateAllAds()
        self.updateAllBids()
        self.updateAllServices()
        self.updateUserSpecificData()
        self.mutex.release()

    def updater(self):
        self.updateAll()
        print("Thread: Updated All")
