from brownie import accounts, ChipNet

accounts.add("a2ace2fbda7b6a4b3830fbd21737a803b2bc570115f4ade13f092242cdd5abda")
myAccount = accounts[0]


def main():
    chipNet = ChipNet.deploy({"from": myAccount})
    return chipNet.address
