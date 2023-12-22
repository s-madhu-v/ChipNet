import tkinter as tk
from tkinter import ttk
from networks import getMyDeployments
from src.appClass import App
from src.app import setTheApp, getTheApp

defaultNetwork = "globalGanache" # set this to `None` to force user to select network

class initPage(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        self.parent = parent
        self.root = root
        self.createWidgets()
        self.layoutWidgets()
        self.okButton.invoke() if defaultNetwork else None

    def createWidgets(self):
        # Network Selector
        self.networkSelectorFrame = tk.Frame(self)
        self.selectNetworkLabel = tk.Label(
            self.networkSelectorFrame, text="Select Network: "
        )
        self.networkComboBox = ttk.Combobox(
            self.networkSelectorFrame, values=list(getMyDeployments().keys())
        )
        self.networkComboBox.set(list(getMyDeployments().keys())[0])
        self.okButton = tk.Button(
            self.networkSelectorFrame, text="OK", command=self.onSubmit
        )

    def layoutWidgets(self):
        self.networkSelectorFrame.grid(row=0, column=0, padx=15, pady=15)
        self.selectNetworkLabel.pack(side="left")
        self.networkComboBox.pack(side="left")
        self.okButton.pack(pady=10)

    def onSubmit(self):
        selectedNetwork = defaultNetwork if defaultNetwork else self.networkComboBox.get()
        print(f"selectedNetwork: {selectedNetwork}")
        self.parent.destroy()
        setTheApp(App(getMyDeployments()[selectedNetwork], selectedNetwork, self.root))
        getTheApp().setupApp()
