import tkinter as tk
from tkinter import ttk
from scripts.data import contractData
from scripts.gui.adFrame import adFrame


# create a bidFrame from adFrame with a status label and a cancel bid button
class serviceFrame(adFrame):
    def __init__(self, parent, service):
        self.ad = contractData.allAds[service.adIndex]
        self.bid = contractData.allBids[service.bidIndex]
        super().__init__(parent, self.ad, width=220, height=170)

    def createWidgets(self):
        super().createWidgets()
        self.status = ttk.Label(self, text="Status: Active")
        self.ssh = ttk.Label(self, text=f"SSH: {self.service.accessLink}")
        self.password = ttk.Label(self, text=f"PASSWORD: {self.service.password}")

    def layoutWidgets(self):
        super().layoutWidgets()
        self.status.pack()
        self.ssh.pack()
        self.password.pack()
        self.buyButton.pack_forget()
        self.price.pack_forget()
        self.sellerAddress.pack_forget()
