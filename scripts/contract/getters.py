from scripts.data import deployedChipnet
import os


def getAllAds():
    return deployedChipnet.getAllAds()


def getBidsOf(account):
    return deployedChipnet.getPurchases(account)


def getAd(index):
    return deployedChipnet.ads(index)
