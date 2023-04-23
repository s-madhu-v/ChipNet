import tkinter as tk
from tkinter import ttk
from start import availableNetworks, defaultNetwork

# from chipnetapp.data import (
#    setMyAccount,
#    contractData,
#    getMyAccount,
#    availabeNetworks,
#    getCurrentNetwork,
#    changeToNetwork,
# )


class initPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.createWidgets()
        self.layoutWidgets()

    def createWidgets(self):
        # Network Selector
        self.networkSelectorFrame = tk.Frame(self)
        self.selectNetworkLabel = tk.Label(
            self.networkSelectorFrame, text="Select Network: "
        )
        self.networkComboBox = ttk.Combobox(
            self.networkSelectorFrame, values=availableNetworks
        )
        self.networkComboBox.set(defaultNetwork)
        self.networkComboBox.bind(
            "<<ComboboxSelected>>", lambda event: self.onNetworkSelect(event)
        )

    def layoutWidgets(self):
        self.networkSelectorFrame.grid(row=0, column=0, padx=15, pady=15)
        self.selectNetworkLabel.pack(side="left")
        self.networkComboBox.pack(side="left")
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)

    def onNetworkSelect(self, event):
        selectedNetwork = self.networkComboBox.get()
        print(f"selectedNetwork: {selectedNetwork}")

    def refresh(self):
        print("refreshing")
