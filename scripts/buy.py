from brownie import accounts, ChipNet, web3
from random import randint
import time
import os


# write a function to post an ad
def postAd(name, priceInEth, sellerAccount=accounts[randint(0, 9)]):
    contractAddress = os.getenv("CONTRACT_ADDRESS")
    chipNet = ChipNet.at(contractAddress)
    txn = chipNet.postAd(
        name,
        priceInEth * (10**18),
        {"from": sellerAccount},
    )
    txn.wait(1)


# write a function to buy an ad
def buyAd():
    contractAddress = os.getenv("CONTRACT_ADDRESS")
    chipNet = ChipNet.at(contractAddress)
    buyerAccount = accounts[1]
    sellerAccount = accounts[2]
    txn = chipNet.purchaseAd(
        chipNet.getAdsCount() - 1, {"from": buyerAccount, "value": 2 * (10**18)}
    )
    txn.wait(1)
    print(f"Buyer balance: {web3.fromWei(buyerAccount.balance(), 'ether')} ETH")
    print(f"Seller balance: {web3.fromWei(sellerAccount.balance(), 'ether')} ETH")


def main():
    print("Entered Main")
    postAd()
    print("Posted Ad")
    buyAd()
    print("Bought Ad")
