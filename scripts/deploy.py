from brownie import accounts, ChipNet

accounts.add("0x5c878d522611affa2bb2cc7c3a72d1b1a38fee335b0be0772ec14c824bb32016")
myAccount = accounts[0]


def main():
    chipNet = ChipNet.deploy({"from": myAccount})
    return chipNet.address
