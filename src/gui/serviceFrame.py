import tkinter as tk
from src.app import getTheApp
from src.gui.adFrame import adFrame
from src.style import myStyle


class serviceFrame(adFrame):
    def __init__(self, parent, service):
        self.service = service
        self.ad = getTheApp().contractData.allAds[service.adIndex]
        super().__init__(
            parent,
            self.ad,
            width=myStyle.serviceFrameWidth,
            height=myStyle.serviceFrameHeight,
        )

    def createWidgets(self):
        super().createWidgets()
        # show time left here...
        # self.hours = tk.Label(self, text=f"Hours: {self.bid.noOfHours}")
        # self.viewLogsButton = tk.Button(
        #     self, text="View Logs", command=self.showServiceLogs
        # )
        self.status = tk.Label(
            self,
            text=f"Status       :   Active",
            font=myStyle.attributeFont,
            anchor="w",
        )

    def layoutWidgets(self):
        self.status.grid(row=0, column=0, sticky="nsew")
        self.status["bg"] = myStyle.serviceStatusColor
        # self.title.grid(row=0, column=0, sticky="nsew")
        # self.title["bg"] = myStyle.serviceTitleColor
        # self.price.grid(row=1, column=0, sticky="nsew")
        # self.price["bg"] = myStyle.servicePriceColor
        # self.viewLogsButton.grid(row=2, column=0, sticky="nsew")
        # self.viewLogsButton["bg"] = myStyle.serviceViewLogsButtonColor
        self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)
        # self.rowconfigure(2, weight=1)

    def showServiceLogs(self):
        print("fake showing Service Logs")

    def updateWidget(self, service):
        self.service = service
        super().updateWidget(getTheApp().contractData.allAds[service.adIndex])
