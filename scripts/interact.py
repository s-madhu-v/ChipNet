from brownie import accounts, ChipNet, web3
import time
import os


# write a setTimeout function for python
def setTimeout(func, delay):
    while True:
        func()
        time.sleep(delay)


# write a function that listens for AdPurchased events polling every 5 seconds
def listenForAdPurchasedEvents():
    # write code to get the contract address from the environment variable
    contractAddress = os.getenv("CONTRACT_ADDRESS")
    # write code to get the contract instance
    chipNet = ChipNet.at(contractAddress)
    # write code to create an event filter for the AdPurchased event
    adPurchasedFilter = chipNet.events.AdPurchased.createFilter(fromBlock="latest")
    # write code to listen for the AdPurchased event
    adPurchasedEvents = adPurchasedFilter.get_new_entries()
    # write code to print the event
    print("AdPurchased events: ")
    print(adPurchasedEvents)


def main():
    contractAddress = os.getenv("CONTRACT_ADDRESS")
    chipNet = ChipNet.at(contractAddress)
    buyerAccount = accounts[1]
    sellerAccount = accounts[2]
    # post an advertisement
    txn = chipNet.postAd(
        "My Ad",
        "I am selling 1000 chips for 1 ETH",
        2 * (10**18),
        {"from": sellerAccount},
    )
    txn.wait(1)
    # print the number of ads
    print(f"Number of ads: {chipNet.getAdsCount()}")
    # print the latest ad
    print(f"Latest ad: {chipNet.getAd(chipNet.getAdsCount() - 1)}")
    # print the balance of both buyer and seller
    print(f"Buyer balance: {web3.fromWei(buyerAccount.balance(), 'ether')} ETH")
    print(f"Seller balance: {web3.fromWei(sellerAccount.balance(), 'ether')} ETH")
    # buy the latest ad from buyerAccount and print the balance of both buyer and seller
    txn = chipNet.buy(
        chipNet.getAdsCount() - 1, {"from": buyerAccount, "value": 2 * (10**18)}
    )
    txn.wait(1)
    print(f"Buyer balance: {web3.fromWei(buyerAccount.balance(), 'ether')} ETH")
    print(f"Seller balance: {web3.fromWei(sellerAccount.balance(), 'ether')} ETH")
    # write an event filter to listen for the AdPosted event
    adPurchasedFilter = chipNet.events.AdPurchased.createFilter(fromBlock="latest")
    # listen for the AdPosted event and print the event
    adPurchasedEvents = adPurchasedFilter.get_new_entries()
    print("AdPurchase events: ")
    print(txn.events)
    print("Listening for AdPurchased events...")
    setTimeout(listenForAdPurchasedEvents, 3)
