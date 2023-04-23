import tkinter as tk
from brownie import Contract, network
from chipnetapp.data import Data
from chipnetapp.gui.gui import appGui
from chipnetapp.eventHandlers import handleBidApprovedEvent
from chipnetapp.contract.setters import postAd
from chipnetapp.contract.getters import getAllAds
from random import randint


class App:
    def __init__(self, contractAddress, networkName, root) -> None:
        self.contractAddress = contractAddress
        self.currentNetwork = networkName
        self.root = root
        self.deployedChipnet = None
        self.myAccount = None
        self.chipnetEvents = None
        self.gui = None

    def setMyAccount(self, account):
        self.myAccount = account

    def setChipnetEvents(self):
        self.chipnetEvents = network.contract.ContractEvents(self.deployedChipnet)

    def switchToNetwork(self, networkName):
        self.currentNetwork = networkName
        if network.is_connected():
            network.disconnect()
        network.connect(self.currentNetwork)
        self.deployedChipnet = Contract(self.contractAddress)
        self.setMyAccount(network.accounts[0])  # temporary. Change this to no account.
        self.setChipnetEvents()
        print(f"ACTIVE NETWORKS: {network.show_active()}")

    def listen(self):
        self.chipnetEvents.subscribe("bidApproved", handleBidApprovedEvent)

    def populateAds(self):
        if len(getAllAds()) == 1:
            print("Populating Ads")
            for i in range(10):
                postAd(f"Ad {i}", randint(1, 10))

    def showGUI(self):
        self.gui = appGui(self)
        self.root.mainloop()

    def setupApp(self):
        self.switchToNetwork(self.currentNetwork)
        self.contractData = Data(self)
        self.listen()
        self.populateAds()  # TODO: deal with this later
        self.showGUI()
