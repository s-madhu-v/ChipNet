import tkinter as tk
from tkinter import ttk
from random import randint
from scripts.gui.notebook import createNotebook
from scripts.marketplace_helpers import getAds

ads = getAds()
# from populate import ads

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

    def buyAd(self):
        print("Buy Ad")
        self.buyButton["text"] = "Bought!!!"

    def createWidgets(self):
        # create the widgets
        self.name = ttk.Label(self, text=self.ad[0])
        self.price = ttk.Label(self, text=f"Price: {self.ad[1]} ETH")
        self.sellerAddress = ttk.Label(self, text=self.ad[2])
        self.buyButton = ttk.Button(self, text="Buy", command=self.buyAd)

        # layout the widgets
        self.name.pack()
        self.price.pack()
        self.sellerAddress.pack()
        self.buyButton.pack()


# create a frame class called adContainer that shows three ads side by side horizontally
class adsContainer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=770, height=130, relief="raised", padding=10)
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()
        ttk.Style().configure("adsContainer.TFrame", background=adsContainerbg)
        self["style"] = "adsContainer.TFrame"

    def createWidgets(self):
        # create the widgets
        self.ad1 = AdFrame(self, ads[0])
        self.ad2 = AdFrame(self, ads[1])
        self.ad3 = AdFrame(self, ads[2])

        # layout the widgets
        self.ad1.pack(side="left", padx=10)
        self.ad2.pack(side="left", padx=10)
        self.ad3.pack(side="left", padx=10)


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
        self.adContainer = adsContainer(self)
        self.rightButton = tk.Button(self, text=">", width=1, height=9)

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
        self.nameLabel = ttk.Label(self, text="Name")
        self.nameEntry = ttk.Entry(self)
        self.priceLabel = ttk.Label(self, text="Price")
        self.priceEntry = ttk.Entry(self)
        self.createButton = ttk.Button(self, text="Create")

        # layout the widgets
        self.nameLabel.pack()
        self.nameEntry.pack()
        self.priceLabel.pack()
        self.priceEntry.pack()
        self.createButton.pack()
        self.createButton["command"] = self.createAd

    def createAd(self):
        name = self.nameEntry.get()
        price = self.priceEntry.get()
        ad = [name, price]
        ads.append(ad)
        print(ads)


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

# Create a label
marketplaceView = adNavigator(marketplace_tab)
marketplaceView.pack()
adMaker = adCreator(advertise_tab)
adMaker.pack()


def main():
    # run the event loop
    root.mainloop()


main()
