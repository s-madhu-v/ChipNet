import tkinter as tk
from tkinter import ttk
from random import randint
from scripts.gui.notebook import createNotebook
from scripts.marketplace_helpers import getAds
from scripts.deploy import populateAds
from scripts.buy import buyAd
from scripts.buy import postAd
from brownie import accounts


# Styles
adFramebg = "green"
adsContainerbg = "blue"
adNavigatorbg = "red"


# create a frame class for the ads
class AdFrame(ttk.Frame):
    def __init__(self, parent, ad):
        super().__init__(
            parent,
            padding=10,
            relief="raised",
            width=220,
            height=110,
        )
        self.ad = ad
        self.createWidgets()
        ttk.Style().configure("AdFrame.TFrame", background=adFramebg)
        self["style"] = "AdFrame.TFrame"
        self.pack_propagate(False)
        self.grid_propagate(False)

    def buyThisAd(self):
        print("Buying Ad")
        buyAd(self.ad[0], accounts[0])
        self.buyButton["text"] = "Bought!!!"

    def createWidgets(self):
        # create the widgets
        self.name = ttk.Label(self, text=self.ad[1])
        self.price = ttk.Label(self, text=f"Price: {int(self.ad[2]/(10**18))} ETH")
        self.sellerAddress = ttk.Label(self, text=self.ad[3])
        isactive = self.ad[4]
        self.buyButton = ttk.Button(self, text="Buy", command=self.buyThisAd)
        if isactive == False:
            self.buyButton["text"] = "Sold"
            self.buyButton["state"] = "disabled"

        # layout the widgets
        self.name.pack()
        self.price.pack()
        self.sellerAddress.pack()
        self.buyButton.pack()


# create a frame class called adContainer that shows three ads side by side horizontally
class adsContainer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=770, height=130, relief="raised", padding=10)
        self.nofAds = 3
        self.ads = []
        self.startAdIndex = 0
        self.adWidgets = []
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()
        ttk.Style().configure("adsContainer.TFrame", background=adsContainerbg)
        self["style"] = "adsContainer.TFrame"
        self.startAdIndx = 0
        print(f"\n\n====={self.nofAds}=====\n\n")

    def updateAds(self):
        self.ads = getAds()

    def createWidgets(self):
        self.updateAds()
        print(self.nofAds)
        for i in range(self.nofAds):
            widget = AdFrame(self, self.ads[self.startAdIndex + i])
            self.adWidgets.append(widget)
            widget.pack(side="left", padx=10)

    def moveAdWidgets(self):
        for i in range(self.nofAds):
            self.adWidgets[i].ad = self.ads[self.startAdIndex + i]
            self.adWidgets[i].name["text"] = self.adWidgets[i].ad[1]
            self.adWidgets[i].price[
                "text"
            ] = f"Price: {int(self.adWidgets[i].ad[2]/(10**18))} ETH"
            self.adWidgets[i].sellerAddress["text"] = self.adWidgets[i].ad[3]
            isactive = self.adWidgets[i].ad[4]
            if isactive == False:
                self.adWidgets[i].buyButton["text"] = "Sold"
                self.adWidgets[i].buyButton["state"] = "disabled"
            else:
                self.adWidgets[i].buyButton["text"] = "Buy"
                self.adWidgets[i].buyButton["state"] = "normal"

    def updateAdWidgets(self):
        self.updateAds()
        self.moveAdWidgets()


# create a handler so that when left button is clicked, offset is increased by 1 and the ads are updated
def leftButtonHandler(self):
    if self.adContainer.startAdIndex > 0:
        self.adContainer.startAdIndex -= 1
        self.adContainer.moveAdWidgets()


# create a right button handler so that when right button is clicked, offset is decreased by 1 and the ads are updated
def rightButtonHandler(self):
    if (
        self.adContainer.startAdIndex
        < len(self.adContainer.ads) - self.adContainer.nofAds
    ):
        self.adContainer.startAdIndex += 1
        self.adContainer.moveAdWidgets()


# create a frame class called adNavigator that has 1 button on the left, an adContainer in the middle, and 1 button on the right
class adNavigator(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=860, height=170, relief="raised")
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()
        ttk.Style().configure("adNavigator.TFrame", background=adNavigatorbg)
        self["style"] = "adNavigator.TFrame"

    def createWidgets(self):
        # create the widgets
        self.leftButton = tk.Button(self, text="<", width=1, height=9)
        self.leftButton["command"] = lambda: leftButtonHandler(self)
        self.adContainer = adsContainer(self)
        self.rightButton = tk.Button(self, text=">", width=1, height=9)
        self.rightButton["command"] = lambda: rightButtonHandler(self)

        # layout the widgets
        self.leftButton.pack(side="left")
        self.adContainer.pack(side="left")
        self.rightButton.pack(side="left")


# create a class to let users create a new ad
class adCreator(ttk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            width=860,
            height=170,
            relief="raised",
        )
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()
        ttk.Style().configure("createAd.TFrame", background=adNavigatorbg)
        self["style"] = "createAd.TFrame"

    def createWidgets(self):
        # create the widgets
        self.titleLabel = ttk.Label(self, text="Title")
        self.titleEntry = ttk.Entry(self)
        self.priceLabel = ttk.Label(self, text="Price")
        self.priceEntry = ttk.Entry(self)
        self.createButton = ttk.Button(self, text="Create")

        # layout the widgets
        self.titleLabel.pack()
        self.titleEntry.pack()
        self.priceLabel.pack()
        self.priceEntry.pack()
        self.createButton.pack()
        self.createButton["command"] = self.createAd

    def createAd(self):
        title = self.titleEntry.get()
        price = self.priceEntry.get()
        postAd(title, price, accounts[0])


# Create the root window
root = tk.Tk()
root.title("ChipNet")
root.geometry("1000x750")
# make the window unresizable
root.resizable(False, False)

# Create the notebook
notebook, marketplace_tab, advertise_tab, purchases_tab, account_tab = createNotebook(
    root
)
notebook.pack()


# create an update button in marketplace tab
updateButton = ttk.Button(marketplace_tab, text="Update")
updateButton.pack()
updateButton["command"] = lambda: marketplaceView.adContainer.updateAdWidgets()
marketplaceView = adNavigator(marketplace_tab)
marketplaceView.pack()
adMaker = adCreator(advertise_tab)
adMaker.pack()


def main():
    # run the event loop
    root.mainloop()


main()
