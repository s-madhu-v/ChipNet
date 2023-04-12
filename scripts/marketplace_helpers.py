from brownie import accounts, ChipNet, web3
import time
import os


def main():
    myAddress = accounts[0]
    myAccount = accounts.at(myAddress)
    chipNet = ChipNet.deploy({"from": myAccount})
    return chipNet.address


# write a function to get all the ads
def getAds():
    contractAddress = os.getenv("CONTRACT_ADDRESS")
    chipNet = ChipNet.at(contractAddress)
    return chipNet.getAllAds()


def getAd(index):
    contractAddress = os.getenv("CONTRACT_ADDRESS")
    chipNet = ChipNet.at(contractAddress)
    return chipNet.getAd(index)
