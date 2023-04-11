from brownie import accounts, ChipNet, web3
import time
import os


def myFunc():
    print("My Func")


# write a function to post an ad
def postAd(name, priceInETH, account):
    contractAddress = os.getenv("CONTRACT_ADDRESS")
    chipNet = ChipNet.at(contractAddress)
    txn = chipNet.postAd(
        name,
        priceInETH * (10**18),
        {"from": account},
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
