from scripts.data import deployedChipnet
from scripts.contract.getters import getAd
from scripts.service.encrypt import generateKeysIfTheyDontExist, readPublicKey
from scripts.data import myAccount


def postAd(title, priceInETH, sellerAccount):
    txn = deployedChipnet.postAd(
        title,
        int(priceInETH) * (10**18),
        {"from": sellerAccount},
    )
    txn.wait(1)
    return txn


def bidOnAd(adIndex, buyerAccount, noOfHours=1):
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


def approveBid(bidIndex, sellerAccount):
    txn = deployedChipnet.approveBid(bidIndex, {"from": sellerAccount})
    txn.wait(1)
    return txn
