from brownie import accounts, ChipNet

# from scripts.contract.setters import postAd
# from scripts.data import myAccount


def main():
    myAddress = accounts[0]
    myAccount = accounts.at(myAddress)
    chipNet = ChipNet.deploy({"from": myAccount})
    # populateAds(chipNet.address)
    return chipNet.address
