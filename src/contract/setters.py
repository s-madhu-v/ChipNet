import psutil
from src.app import getTheApp
from src.contract.getters import getAd
from src.service.encrypt import generateKeysIfTheyDontExist, readPublicKey


def postAd(
    title, coresAllocation, memoryAllocation, storageAllocation, pricePerHour
):  # change the variable name to just price
    sellerAccount = getTheApp().myAccount
    deployedChipnet = getTheApp().deployedChipnet
    txn = deployedChipnet.postAd(
        title,
        f"{(psutil.cpu_freq().max)/1000} GHz",
        coresAllocation,
        memoryAllocation,
        storageAllocation,
        pricePerHour,
        {"from": sellerAccount},
    )
    txn.wait(1)
    return txn


def bidOnAd(adIndex, template, noOfHours=1):
    buyerAccount = getTheApp().myAccount
    deployedChipnet = getTheApp().deployedChipnet
    print(f"Bidding on an Ad: {adIndex}, with noOfHours: {noOfHours}")
    generateKeysIfTheyDontExist()
    ad = getAd(adIndex)
    print(f"\n\n\nBuying the ad: {ad}, with adIndex: {adIndex}\n\n\n")
    txn = deployedChipnet.bidOnAd(
        adIndex,
        noOfHours,
        readPublicKey().export_key().decode("utf-8"),
        template,
        {"from": buyerAccount, "value": ad["pricePerHour"] * noOfHours},
    )
    txn.wait(1)
    return txn


def approveBid(bidIndex):
    sellerAccount = getTheApp().myAccount
    deployedChipnet = getTheApp().deployedChipnet
    txn = deployedChipnet.approveBid(bidIndex, {"from": sellerAccount})
    txn.wait(1)
    return txn


def cancelBid(bidIndex):
    buyerAccount = getTheApp().myAccount
    deployedChipnet = getTheApp().deployedChipnet
    txn = deployedChipnet.cancelBid(bidIndex, {"from": buyerAccount})
    txn.wait(1)
    return txn
