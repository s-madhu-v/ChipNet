from brownie import accounts, ChipNet, web3
import time
import os


def main():
    myAddress = accounts[0]
    myAccount = accounts.at(myAddress)
    chipNet = ChipNet.deploy({"from": myAccount})
    return chipNet.address
