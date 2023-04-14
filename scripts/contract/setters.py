from scripts.data import deployedChipnet
from scripts.contract.getters import getAd


def bidOnAd(adIndex, buyerAccount, noOfHours=1):
    ad = getAd(adIndex)
    print(f"\n\n\nBuying the ad: {ad}, with adIndex: {adIndex}\n\n\n")
    txn = deployedChipnet.bidOnAd(
        adIndex, noOfHours, {"from": buyerAccount, "value": ad["price"]}
    )
    txn.wait(1)


def postAd(title, priceInETH, sellerAccount):
    txn = deployedChipnet.postAd(
        title,
        int(priceInETH) * (10**18),
        {"from": sellerAccount},
    )
    txn.wait(1)
