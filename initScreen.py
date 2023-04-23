import tkinter as tk
from tkinter import ttk
from networks import getMyDeployments
from chipnetapp.appClass import App
from chipnetapp.app import setTheApp, getTheApp


class initPage(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        self.parent = parent
        self.root = root
        self.createWidgets()
        self.layoutWidgets()

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
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)

    def onSubmit(self):
        selectedNetwork = self.networkComboBox.get()
        print(f"selectedNetwork: {selectedNetwork}")
        self.parent.destroy()
        setTheApp(App(getMyDeployments()[selectedNetwork], selectedNetwork, self.root))
        getTheApp().setupApp()
