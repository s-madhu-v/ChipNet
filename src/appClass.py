import tkinter as tk
from brownie import Contract, network, Wei, accounts, ChipNet
from src.data import Data
from src.gui.gui import appGui
from src.eventHandlers import handleBidApprovedEvent
from src.contract.setters import postAd
from src.contract.getters import getAllAds
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
        self.deployedChipnet = ChipNet.at(self.contractAddress)
        self.setMyAccount(network.accounts[-1])  # temporary. Change this to no account.
        self.setChipnetEvents()
        print(f"ACTIVE NETWORKS: {network.show_active()}")

    def listen(self):
        self.chipnetEvents.subscribe("bidApproved", handleBidApprovedEvent)

    def populateAds(self):
        if len(getAllAds()) <= 1:
            print("Populating Ads")
            for i in range(10):
                postAd(f"Ad {i}", 1, "1g", "5g", Wei(f"{randint(4, 24)} finney"))

    def showGUI(self):
        self.gui = appGui(self)
        self.root.bind("<Escape>", self.gui.showRefreshTab)
        self.root.mainloop()

    def setupApp(self):
        self.switchToNetwork(self.currentNetwork)
        self.contractData = Data(self)
        self.listen()
        self.populateAds()  # TODO: deal with this later
        self.showGUI()
