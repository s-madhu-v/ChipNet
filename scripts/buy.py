import brownie
from brownie import accounts, ChipNet, web3
import time
import os


# write a function to post an ad
def postAd():
    contractAddress = os.getenv("CONTRACT_ADDRESS")
    chipNet = ChipNet.at(contractAddress)
    sellerAccount = accounts[2]
    txn = chipNet.postAd(
        "My Ad",
        "I am selling 1000 chips for 1 ETH",
        2 * (10**18),
        {"from": sellerAccount},
    )
    txn.wait(1)
    print(f"Number of ads: {chipNet.getAdsCount()}")
    print(f"Latest ad: {chipNet.getAd(chipNet.getAdsCount() - 1)}")


# write a function to buy an ad
def buyAd():
    contractAddress = os.getenv("CONTRACT_ADDRESS")
    chipNet = ChipNet.at(contractAddress)
    buyerAccount = accounts[1]
    sellerAccount = accounts[2]
    txn = chipNet.buy(
        chipNet.getAdsCount() - 1, {"from": buyerAccount, "value": 2 * (10**18)}
    )
    txn.wait(1)
    print(f"Buyer balance: {web3.fromWei(buyerAccount.balance(), 'ether')} ETH")
    print(f"Seller balance: {web3.fromWei(sellerAccount.balance(), 'ether')} ETH")


def handle_event(event):
    print(f"\n\n\n\nEvent {event.name} triggered with arguments: {event.args}\n\n\n\n")


contractAddr = os.getenv("CONTRACT_ADDRESS")
contract = ChipNet.at(contractAddr)
x = brownie.network.contract.ContractEvents(contract)
x.subscribe("AdPurchased", handle_event)


def main():
    contractAddress = os.getenv("CONTRACT_ADDRESS")
    chipNet = ChipNet.at(contractAddress)
    print("Entered Main")
    postAd()
    print("Posted Ad")
    buyAd()
    print("Bought Ad")
