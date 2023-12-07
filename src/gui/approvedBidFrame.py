import tkinter as tk
from src.gui.adFrame import adFrame
from src.gui.utils import createNewWindow, copy_text
from src.service.encrypt import decryptCredentials
from src.app import getTheApp
from src.style import myStyle

default_comments = """
Comments will be displayed here:
"""

def display_text_window(text_content=default_comments):
    if text_content == "":
        text_content = default_comments
    # Create a new window
    text_window = tk.Toplevel()
    # Create a Text widget in the new window
    text_widget = tk.Text(text_window)
    text_widget.pack()
    text_widget.insert(tk.END, text_content)

# create a bidFrame from adFrame with a status label and a cancel bid button
class approvedBidFrame(adFrame):
    def __init__(self, parent, service):
        self.service = service
        self.ad = getTheApp().contractData.allAds[service.adIndex]
        self.bid = getTheApp().contractData.allBids[service.bidIndex]
        super().__init__(
            parent,
            self.ad,
            width=myStyle.serviceFrameWidth,
            height=myStyle.serviceFrameHeight,
        )

    def showComments(self):
        decryptedComments = decryptCredentials(self.service.comments)
        display_text_window(decryptedComments)

    def createWidgets(self):
        super().createWidgets()
        self.title["bg"] = myStyle.approvedBidTitleColor
        self.status = tk.Label(
            self, text="Status       :   Active", font=myStyle.attributeFont, anchor="w"
        )
        self.status["bg"] = myStyle.approvedBidStatusColor
        self.showCommentsButton = tk.Button(
            self, text="Show Comments", command=self.showComments
        )

    def layoutWidgets(self):
        self.status.grid(row=0, column=0, sticky="nsew")
        self.status["bg"] = myStyle.serviceStatusColor
        self.showCommentsButton.grid(row=1, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def updateWidget(self, service):
        self.service = service
        super().updateWidget(getTheApp().contractData.allAds[self.service.adIndex])
        self.status.config(text="Status: Active")
