# The entrypoint for the GUI
# This file is responsible for creating the main window and all of the tabs
from src.gui.tabsFrame import TabFrame
from src.gui.buyTab import buyPage
from src.gui.homeTab import homePage
from src.gui.sellTab import sellPage
from src.gui.settingsTab import settingsPage


class appGui:
    def __init__(self, app) -> None:
        self.app = app
        self.root = app.root
        self.tabBar = TabFrame(self.root)
        self.homeTab = homePage(self.root)
        self.buyTab = buyPage(self.root)
        self.sellTab = sellPage(self.root)
        self.settingsTab = settingsPage(self.root)
        self.allTabs = [self.homeTab, self.buyTab, self.sellTab, self.settingsTab]
        self.setupAppWindow()

    def setupAppWindow(self):
        self.bindClickHandlers()
        self.layoutWidgets()
        self.showHomeTab()

    def layoutWidgets(self):
        self.tabBar.grid(row=0, column=0, sticky="nsew")

    def hideAllTabs(self):
        for tab in self.allTabs:
            tab.grid_forget()

    def showHomeTab(self, event=None):
        if self.tabBar.lastClickedTab == "Home":
            return
        self.hideAllTabs()
        self.homeTab.grid(row=1, column=0, sticky="nsew")
        self.tabBar.lastClickedTab = "Home"

    def showBuyTab(self, event):
        if self.tabBar.lastClickedTab == "Buy":
            return
        self.hideAllTabs()
        self.buyTab.grid(row=1, column=0, sticky="nsew")
        self.tabBar.lastClickedTab = "Buy"

    def showSellTab(self, event):
        if self.tabBar.lastClickedTab == "Sell":
            return
        self.hideAllTabs()
        self.sellTab.grid(row=1, column=0, sticky="nsew")
        self.tabBar.lastClickedTab = "Sell"

    def showMyServicesTab(self, event):
        if self.tabBar.lastClickedTab == "My Services":
            return
        self.hideAllTabs()
        print("my services")
        self.tabBar.lastClickedTab = "My Services"

    def showSettingsTab(self, event):
        if self.tabBar.lastClickedTab == "Settings":
            return
        self.hideAllTabs()
        self.settingsTab.grid(row=1, column=0, sticky="nsew")
        print("Settings")
        self.tabBar.lastClickedTab = "Settings"

    def showRefreshTab(self, event):
        self.buyTab.refresh()
        self.sellTab.refresh()
        self.tabBar.tabs[-1]["bg"] = "green"
        self.app.contractData.updateChangeMetric()
        self.tabBar.lastClickedTab = "Refresh"

    def bindClickHandlers(self):
        self.tabBar.bindClickHandlers(
            [
                self.showHomeTab,
                self.showBuyTab,
                self.showSellTab,
                self.showMyServicesTab,
                self.showSettingsTab,
                self.showRefreshTab,
            ]
        )
