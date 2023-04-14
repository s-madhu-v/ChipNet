from scripts.contract.setters import postAd
from brownie import accounts
from scripts.data import sellAccount


def populateAds():
    postAd("Malin Akerman", 14, sellAccount)
    postAd("Alice Eve", 4, sellAccount)
    postAd("Megan Boone", 5, sellAccount)
    postAd("Sonali Bindre", 8, sellAccount)
    postAd("Kajal Agarwal", 2, sellAccount)
    postAd("Melissa Benoist", 3, sellAccount)
    postAd("Amy Adams", 12, sellAccount)
    postAd("Kate Beckinsale", 9, sellAccount)
    postAd("Brie Larson", 7, sellAccount)
    postAd("Cameron Diaz", 6, sellAccount)
    postAd("Scarlett Johansson", 1, sellAccount)
    postAd("Jennifer Lawrence", 11, sellAccount)
    postAd("Emma Stone", 10, sellAccount)
    postAd("Emma Watson", 13, sellAccount)
    postAd("Jennifer Aniston", 15, sellAccount)
    postAd("Jennifer Lopez", 16, sellAccount)
    postAd("Katherine Heigl", 18, sellAccount)
    postAd("Kristen Stewart", 19, sellAccount)
    postAd("Mila Kunis", 20, sellAccount)
    postAd("Natalie Portman", 21, sellAccount)
    postAd("Nicole Kidman", 22, sellAccount)
    postAd("Rachel McAdams", 23, sellAccount)
