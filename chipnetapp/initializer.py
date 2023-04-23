from brownie import Contract


class app:
    def __init__(
        self,
    ) -> None:
        self.myAccount = None
        self.currentNetwork = None
        self.deployedChipnet = None
        self.chipnetEvents = None
        self.mutex = None
        self.contractData = None

    #        self.availableNetworks = ["localGanache", "globalGanache"] if you want to use, restart the app

    def getDeployedChipnet(self):
        return self.deployedChipnet

    def getMyAccount(self):
        return self.myAccount

    def setMyAccount(self, account):
        self.myAccount = account

    def getCurrentNetwork(self):
        return self.currentNetwork
