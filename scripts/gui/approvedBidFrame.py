import tkinter as tk
from tkinter import ttk
from scripts.data import contractData
from scripts.gui.adFrame import adFrame
import base64
from scripts.service.encrypt import decryptMsg, readPrivateKey


def decryptCredentials(msg):
    msg.encode("utf-8")
    msg = base64.b64decode(msg)
    msg = decryptMsg(msg, readPrivateKey()).decode("utf-8")
    return msg


# create a bidFrame from adFrame with a status label and a cancel bid button
class approvedBidFrame(adFrame):
    def __init__(self, parent, service):
        self.service = service
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

    def updateWidget(self, service):
        super().updateWidget(contractData.allAds[service.adIndex])
        if self.service.accessLink == "":
            self.ssh.config(text="SSH: Not yet provided")
            self.password.config(text="PASSWORD: Not yet provided")
        else:
            self.ssh.config(text=f"SSH: {decryptCredentials(self.service.accessLink)}")
            self.password.config(
                text=f"PASSWORD: {decryptCredentials(self.service.password)}"
            )
        self.status.config(text="Status: Active")
