import tkinter as tk
from src.data import setInterval
from src.app import getTheApp
from src.style import myStyle

tabs = ["Home", "Buy", "Sell", "Create Ad", "Settings", "Refresh"]


class TabFrame(tk.Frame):
    def __init__(self, parent, tabNames=tabs):
        super().__init__(parent, width=1000, height=40)
        self["bg"] = myStyle.tabsFrameColor
        self.parent = parent
        self.grid_propagate(False)
        self.tabNames = tabNames
        self.tabs = []
        self.lastClickedTab = None
        self.createWidgets()
        setInterval(self.checkForRefresh, 5)

    def createWidgets(self):
        for i in range(len(self.tabNames)):
            self.tab = tk.Label(self, text=self.tabNames[i], font=myStyle.tabNameFont)
            self.tab.parent = self
            self.tabs.append(self.tab)
            self.tab["bg"] = myStyle.tabBoxColor
            # if self.tabNames[i] == "Refresh":
            #     self.tab.bind("<Button-1>", lambda event: self.parent.refresh())
            self.tab.grid(row=0, column=i, sticky="nsew")
            self.columnconfigure(i, weight=1)
        self.rowconfigure(0, weight=1)

    def bindClickHandlers(self, clickHandlersListInOrder):
        for i in range(len(self.tabs)):
            self.tabs[i].bind("<Button-1>", clickHandlersListInOrder[i])

    def checkForRefresh(self):
        if getTheApp().contractData.isRefreshNeeded():
            self.tabs[-1]["bg"] = myStyle.refreshNeededColor
