from scripts.contract.setters import postAd
from brownie import accounts


def populateAds():
    postAd("Malin Akerman", 14, accounts[3])
    postAd("Alice Eve", 4, accounts[4])
    postAd("Megan Boone", 5, accounts[2])
    postAd("Sonali Bindre", 8, accounts[1])
    postAd("Kajal Agarwal", 2, accounts[5])
    postAd("Melissa Benoist", 3, accounts[6])
    postAd("Amy Adams", 12, accounts[7])
    postAd("Kate Beckinsale", 9, accounts[8])
    postAd("Brie Larson", 7, accounts[9])
    postAd("Cameron Diaz", 6, accounts[0])
    postAd("Scarlett Johansson", 1, accounts[1])
    postAd("Jennifer Lawrence", 11, accounts[2])
    postAd("Emma Stone", 10, accounts[3])
    postAd("Emma Watson", 13, accounts[4])
    postAd("Jennifer Aniston", 15, accounts[5])
    postAd("Jennifer Lopez", 16, accounts[6])
    postAd("Katherine Heigl", 18, accounts[8])
    postAd("Kristen Stewart", 19, accounts[9])
    postAd("Mila Kunis", 20, accounts[0])
    postAd("Natalie Portman", 21, accounts[1])
    postAd("Nicole Kidman", 22, accounts[2])
    postAd("Rachel McAdams", 23, accounts[3])
