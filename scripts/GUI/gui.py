import tkinter as tk
from tkinter import ttk
from scripts.buy import postAd
from scripts.GUI.marketplace import adLabel
from scripts.GUI.notebook import createNotebook
from scripts.marketplace_helpers import getAds, getAd

# create the main window
root = tk.Tk()

notebook, marketplace_tab, advertise_tab, purchases_tab, account_tab = createNotebook(
    root
)


def deployContract():
    contractAddress = run("deploy")
    print(f"Contract address: {contractAddress}")


def populateAds():
    postAd("malin")
    postAd("alice")
    postAd("megan")
    postAd("sonali")
    postAd("Kajal")
    postAd("benoist")
    postAd("Amy Adams")
    postAd("Beckinsale")


def displayAds(frame, rowLength=3):
    ads = getAds()
    for i in range(len(ads)):
        adLabel(ads[i], frame).grid(
            row=int(i / rowLength), column=i % rowLength, padx=10, pady=10
        )


def main():
    # start the main event loop
    # populateAds()
    displayAds(marketplace_tab, 5)
    root.mainloop()
