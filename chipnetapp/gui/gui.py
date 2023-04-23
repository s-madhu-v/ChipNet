# The entrypoint for the GUI

from chipnetapp.data import updateDataRegularly, contractData
from chipnetapp.contract.getters import getAllAds
from chipnetapp.gui.populate import populateAds
from chipnetapp.gui.tabsFrame import TabFrame
from chipnetapp.gui.buyTab import buyPage
from chipnetapp.gui.homeTab import homePage
from chipnetapp.gui.sellTab import sellPage
from chipnetapp.gui.settingsTab import settingsPage
from chipnetapp.gui.root import root
from chipnetapp.events.listener import listen

if len(getAllAds()) == 1:
    print("Populating Ads")
    populateAds()


def guiSetup():
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

    # Create the settingsTab
    settings = settingsPage(root)

    allTabs = [home, buy, sell, settings]

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

    def showSettingsTab(event):
        if tabs.lastClickedTab == "Settings":
            return
        hideAllTabs(event)
        settings.grid(row=1, column=0, sticky="nsew")
        print("Settings")
        tabs.lastClickedTab = "Settings"

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
            showSettingsTab,
            showRefreshTab,
        ]
    )

    home.grid(row=1, column=0, sticky="nsew")


def main():
    # Setup gui
    guiSetup()
    # start listening for events
    listen()
    updateDataRegularly()
    # run the event loop
    root.mainloop()
