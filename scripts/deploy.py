from brownie import accounts, ChipNet, web3
from scripts.buy import postAd
import time
import os


def populateAds(contractAddress):
    postAd("Malin Akerman", 14, accounts[3], contractAddress)
    postAd("Alice Eve", 4, accounts[4], contractAddress)
    postAd("Megan Boone", 5, accounts[2], contractAddress)
    postAd("Sonali Bindre", 8, accounts[1], contractAddress)
    postAd("Kajal Agarwal", 2, accounts[5], contractAddress)
    postAd("Melissa Benoist", 3, accounts[6], contractAddress)
    postAd("Amy Adams", 12, accounts[7], contractAddress)
    postAd("Kate Beckinsale", 9, accounts[8], contractAddress)
    postAd("Brie Larson", 7, accounts[9], contractAddress)
    postAd("Cameron Diaz", 6, accounts[0], contractAddress)
    postAd("Scarlett Johansson", 1, accounts[1], contractAddress)
    postAd("Jennifer Lawrence", 11, accounts[2], contractAddress)
    postAd("Emma Stone", 10, accounts[3], contractAddress)
    postAd("Emma Watson", 13, accounts[4], contractAddress)
    postAd("Jennifer Aniston", 15, accounts[5], contractAddress)
    postAd("Jennifer Lopez", 16, accounts[6], contractAddress)
    postAd("Katherine Heigl", 18, accounts[8], contractAddress)
    postAd("Kristen Stewart", 19, accounts[9], contractAddress)
    postAd("Mila Kunis", 20, accounts[0], contractAddress)
    postAd("Natalie Portman", 21, accounts[1], contractAddress)
    postAd("Nicole Kidman", 22, accounts[2], contractAddress)
    postAd("Rachel McAdams", 23, accounts[3], contractAddress)


def main():
    myAddress = accounts[0]
    myAccount = accounts.at(myAddress)
    chipNet = ChipNet.deploy({"from": myAccount})
    populateAds(chipNet.address)
    return chipNet.address
