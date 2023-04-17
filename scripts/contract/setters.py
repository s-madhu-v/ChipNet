from scripts.data import deployedChipnet
from scripts.contract.getters import getAd
from scripts.service.encrypt import generateKeysIfTheyDontExist, readPublicKey
from scripts.data import buyAccount, sellAccount


def postAd(title, priceInETH, sellerAccount):
    txn = deployedChipnet.postAd(
        title,
        int(priceInETH) * (10**18),
        {"from": sellerAccount},
    )
    txn.wait(1)
    return txn


def bidOnAd(
    adIndex, buyerAccount, noOfHours=1
):  # change the buyAccount to buyerAccount
    print(f"Bidding on an Ad: {adIndex}, with noOfHours: {noOfHours}")
    generateKeysIfTheyDontExist()
    ad = getAd(adIndex)
    print(f"\n\n\nBuying the ad: {ad}, with adIndex: {adIndex}\n\n\n")
    txn = deployedChipnet.bidOnAd(
        adIndex,
        noOfHours,
        readPublicKey().export_key().decode("utf-8"),
        {"from": buyAccount, "value": ad["pricePerHour"] * noOfHours},
    )
    txn.wait(1)
    return txn


def approveBid(bidIndex, sellerAccount):  # change the sellAccount to sellerAccount
    txn = deployedChipnet.approveBid(bidIndex, {"from": sellAccount})
    txn.wait(1)
    return txn
