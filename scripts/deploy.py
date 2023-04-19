from brownie import accounts, ChipNet

myAccount = accounts[0]


def main():
    chipNet = ChipNet.deploy({"from": myAccount})
    return chipNet.address
