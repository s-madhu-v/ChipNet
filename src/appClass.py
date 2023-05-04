import tkinter as tk
from brownie import Contract, network, Wei, accounts, project
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
        self.p = project.load("", name="ChipNet")
        self.p.load_config()
        self.root = root
        self.deployedChipnet = None
        self.myAccount = None
        self.chipnetEvents = None
        self.gui = None
        #accounts.add("a2ace2fbda7b6a4b3830fbd21737a803b2bc570115f4ade13f092242cdd5abda")
        accounts.add("65374019dc6a5281a58e6aef720927eeed63b564932245cc8b4f47f965921876")

    def setMyAccount(self, account):
        self.myAccount = account

    def setChipnetEvents(self):
        self.chipnetEvents = network.contract.ContractEvents(self.deployedChipnet)

    def switchToNetwork(self, networkName):
        self.setMyAccount(network.accounts[0])  # temporary. Change this to no account.
        self.currentNetwork = networkName
        if network.is_connected():
            network.disconnect()
        network.connect(self.currentNetwork)
        self.deployedChipnet = self.p.ChipNet.at(self.contractAddress)
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
        # self.populateAds()  # TODO: deal with this later
        self.showGUI()
