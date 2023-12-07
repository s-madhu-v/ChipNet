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

# class credetialsViewer(tk.Frame):
#     def __init__(self, parent, serviceIndex):
#         super().__init__(parent)
#         self.service = getTheApp().contractData.allServices[serviceIndex]
#         self.createWidgets()
#         self.layoutWidgets()

#     def createWidgets(self):
#         decryptedAccessLink = "Not Posted Yet"
#         decryptedPassword = "Not Posted Yet"
#         if self.service.accessLink != "":
#             x = decryptCredentials(self.service.accessLink).split(":")
#             decryptedAccessLink = ("ssh root@" + x[0] + " -p " + x[1])[:-1]
#         if self.service.password != "":
#             decryptedPassword = decryptCredentials(self.service.password)
#         self.sshHeader = tk.Label(
#             self, text="SSH Command: ", font=myStyle.sshHeaderFont
#         )
#         self.ssh = tk.Label(
#             self,
#             text=decryptedAccessLink,
#             font=myStyle.sshAccessLinkFont,
#             cursor="hand2",
#         )
#         self.ssh.bind("<Button-1>", copy_text)
#         self.passwordHeader = tk.Label(
#             self, text="SSH Password: ", font=myStyle.sshPasswordHeaderFont
#         )
#         self.password = tk.Label(
#             self,
#             text=decryptedPassword,
#             font=myStyle.sshPasswordFont,
#             cursor="hand2",
#         )
#         self.password.bind("<Button-1>", copy_text)

#     def layoutWidgets(self):
#         self.sshHeader.grid(row=0, column=0, sticky="nsew")
#         self.ssh.grid(row=0, column=1, sticky="nsew", pady=10)
#         self.passwordHeader.grid(row=1, column=0, sticky="nsew")
#         self.password.grid(row=1, column=1, sticky="nsew")


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
        display_text_window(self.service.comments)
        # if self.service.password != "":
        #     decryptedPassword = decryptCredentials(self.service.password)
        
        # window = createNewWindow("Credentials", "")
        # credetialsViewer(window, self.service.index).pack(fill="both", expand=True)

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
        # self.title.grid(row=0, column=0, sticky="nsew")
        self.status.grid(row=0, column=0, sticky="nsew")
        self.status["bg"] = myStyle.serviceStatusColor
        self.showCommentsButton.grid(row=1, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def updateWidget(self, service):
        self.service = service
        super().updateWidget(getTheApp().contractData.allAds[self.service.adIndex])
        self.status.config(text="Status: Active")
