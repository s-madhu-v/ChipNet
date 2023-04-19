# The entrypoint for the GUI

from scripts.contract.getters import getAllAds
from scripts.gui.populate import populateAds
from scripts.gui.tabsFrame import TabFrame
from scripts.gui.buyTab import buyPage
from scripts.gui.homeTab import homePage
from scripts.gui.sellTab import sellPage
from scripts.gui.root import root
from scripts.data import updateDataRegularly, contractData
from scripts.events.listener import listen

if len(getAllAds()) == 1:
    print("Populating Ads")
    populateAds()


# set the title for the window
root.title("ChipNet")

# set the size of the window
root.geometry("1000x750")

# make the window unresizable
root.resizable(False, False)

# Create the tabs
tabs = TabFrame(root)
tabs.grid(row=0, column=0, sticky="nsew")

# Create the homeTab
home = homePage(root)

# Create the buyTab
buy = buyPage(root)

# Create the sellTab
sell = sellPage(root)

allTabs = [home, buy, sell]


def hideAllTabs(event):
    for tab in allTabs:
        tab.grid_forget()


def showHomeTab(event):
    if tabs.lastClickedTab == "Home":
        return
    hideAllTabs(event)
    home.grid(row=1, column=0, sticky="nsew")
    tabs.lastClickedTab = "Home"


def showBuyTab(event):
    if tabs.lastClickedTab == "Buy":
        return
    hideAllTabs(event)
    buy.grid(row=1, column=0, sticky="nsew")
    tabs.lastClickedTab = "Buy"


def showSellTab(event):
    if tabs.lastClickedTab == "Sell":
        return
    hideAllTabs(event)
    sell.grid(row=1, column=0, sticky="nsew")
    tabs.lastClickedTab = "Sell"


def showMyServicesTab(event):
    if tabs.lastClickedTab == "My Services":
        return
    hideAllTabs(event)
    print("my services")
    tabs.lastClickedTab = "My Services"


def showMyAccountTab(event):
    if tabs.lastClickedTab == "My Account":
        return
    hideAllTabs(event)
    print("my account")
    tabs.lastClickedTab = "My Account"


def showRefreshTab(event):
    buy.refresh()
    sell.refresh()
    tabs.tabs[-1]["bg"] = "green"
    contractData.updateChangeMetric()
    tabs.lastClickedTab = "Refresh"


tabs.bindClickHandlers(
    [
        showHomeTab,
        showBuyTab,
        showSellTab,
        showMyServicesTab,
        showMyAccountTab,
        showRefreshTab,
    ]
)

home.grid(row=1, column=0, sticky="nsew")


def main():
    # start listening for events
    listen()
    updateDataRegularly()
    # run the event loop
    root.mainloop()
