from myTkinter import myTk, myTtk
tk = myTk
#import tkinter as tk
#ttk = myttk

from chipnetapp.data import contractData
from chipnetapp.gui.adFrame import adFrame
from chipnetapp.gui.utils import createNewWindow, copy_text
from chipnetapp.service.encrypt import decryptCredentials


class credetialsViewer(tk.Frame):
    def __init__(self, parent, serviceIndex):
        super().__init__(parent)
        self.service = contractData.allServices[serviceIndex]
        self.createWidgets()
        self.layoutWidgets()

    def createWidgets(self):
        decryptedAccessLink = "Not Posted Yet"
        decryptedPassword = "Not Posted Yet"
        if self.service.accessLink != "":
            x = decryptCredentials(self.service.accessLink).split(":")
            decryptedAccessLink = ("ssh root@" + x[0] + " -p " + x[1])[:-1]
        if self.service.password != "":
            decryptedPassword = decryptCredentials(self.service.password)
        self.sshHeader = tk.Label(
            self, text="SSH Command: ", font=("American Typewriter", 16)
        )
        self.ssh = tk.Label(
            self,
            text=decryptedAccessLink,
            font=("American Typewriter", 16),
            cursor="hand2",
        )
        self.ssh.bind("<Button-1>", copy_text)
        self.passwordHeader = tk.Label(
            self, text="SSH Password: ", font=("American Typewriter", 16)
        )
        self.password = tk.Label(
            self,
            text=decryptedPassword,
            font=("American Typewriter", 16),
            cursor="hand2",
        )
        self.password.bind("<Button-1>", copy_text)

    def layoutWidgets(self):
        self.sshHeader.grid(row=0, column=0, sticky="nsew")
        self.ssh.grid(row=0, column=1, sticky="nsew", pady=10)
        self.passwordHeader.grid(row=1, column=0, sticky="nsew")
        self.password.grid(row=1, column=1, sticky="nsew")


# create a bidFrame from adFrame with a status label and a cancel bid button
class approvedBidFrame(adFrame):
    def __init__(self, parent, service):
        self.service = service
        self.ad = contractData.allAds[service.adIndex]
        self.bid = contractData.allBids[service.bidIndex]
        super().__init__(parent, self.ad, width=210, height=160)

    def showCredentials(self):
        window = createNewWindow("Credentials", "")
        credetialsViewer(window, self.service.index).pack(fill="both", expand=True)

    def createWidgets(self):
        super().createWidgets()
        self.title["bg"] = "blue"
        self.status = tk.Label(self, text="Status: Active")
        self.status["bg"] = "green"
        self.showCredentialsButton = tk.Button(
            self, text="Show Credentials", command=self.showCredentials
        )

    def layoutWidgets(self):
        self.title.grid(row=0, column=0, sticky="nsew")
        self.status.grid(row=1, column=0, sticky="nsew")
        self.showCredentialsButton.grid(row=2, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

    def updateWidget(self, service):
        self.service = service
        super().updateWidget(contractData.allAds[self.service.adIndex])
        self.status.config(text="Status: Active")
