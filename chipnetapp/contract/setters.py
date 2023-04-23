from chipnetapp.app import getTheApp
from chipnetapp.contract.getters import getAd
from chipnetapp.service.encrypt import generateKeysIfTheyDontExist, readPublicKey


def postAd(title, priceInETH):
    sellerAccount = getTheApp().myAccount
    deployedChipnet = getTheApp().deployedChipnet
    txn = deployedChipnet.postAd(
        title,
        int(priceInETH) * (10**18),
        {"from": sellerAccount},
    )
    txn.wait(1)
    return txn


def bidOnAd(adIndex, noOfHours=1):
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
