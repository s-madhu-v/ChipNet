from brownie import accounts, ChipNet, web3
import time
import os


# write a function to post an ad
def postAd(title, priceInETH, account, contractAddress=os.getenv("CONTRACT_ADDRESS")):
    chipNet = ChipNet.at(contractAddress)
    txn = chipNet.postAd(
        title,
        int(priceInETH) * (10**18),
        {"from": account},
    )
    txn.wait(1)


# write a function to buy an ad
def buyAd(adIndex, buyerAccount):
    contractAddress = os.getenv("CONTRACT_ADDRESS")
    chipNet = ChipNet.at(contractAddress)
    ad = chipNet.ads(adIndex)
    print(chipNet.getAllAds())
    print(f"\n\n\nBuying the ad: {ad}, with adIndex: {adIndex}\n\n\n")
    txn = chipNet.purchaseAd(adIndex, {"from": buyerAccount, "value": ad["price"]})
    txn.wait(1)


def main():
    postAd()
    buyAd()
