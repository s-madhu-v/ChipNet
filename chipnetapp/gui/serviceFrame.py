import tkinter as tk
from chipnetapp.app import getTheApp
from chipnetapp.gui.adFrame import adFrame


class serviceFrame(adFrame):
    def __init__(self, parent, service):
        self.service = service
        self.ad = getTheApp().contractData.allAds[service.adIndex]
        super().__init__(parent, self.ad, width=210, height=160)

    def createWidgets(self):
        super().createWidgets()
        # show time left here...
        # self.hours = tk.Label(self, text=f"Hours: {self.bid.noOfHours}")
        self.viewLogsButton = tk.Button(
            self, text="View Logs", command=self.showServiceLogs
        )

    def layoutWidgets(self):
        self.title.grid(row=0, column=0, sticky="nsew")
        self.title["bg"] = "blue"
        self.price.grid(row=1, column=0, sticky="nsew")
        self.price["bg"] = "yellow"
        self.viewLogsButton.grid(row=2, column=0, sticky="nsew")
        self.viewLogsButton["bg"] = "red"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

    def showServiceLogs(self):
        print("fake showing Service Logs")

    def updateWidget(self, service):
        self.service = service
        super().updateWidget(getTheApp().contractData.allAds[service.adIndex])
