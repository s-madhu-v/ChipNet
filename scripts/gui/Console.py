import tkinter as tk
from tkinter import ttk
from scripts.gui.header import Header

adConsolebackground = "red"


class Console(ttk.Frame):
    def __init__(self, parent, containerCreatorFunc, heading, backgroundColor="red"):
        super().__init__(parent, width=1000, height=220, relief="raised")
        self.containerCreatorFunc = containerCreatorFunc
        self.heading = heading
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()
        self.createLayout()

    def createWidgets(self):
        # create the widgets
        self.header = Header(self, heading=self.heading)
        self.leftButton = tk.Label(self, text="<")
        self.leftButton["bg"] = "yellow"
        self.leftButton.bind("<Button-1>", self.leftButtonHandler)
        self.frameContainer = self.containerCreatorFunc(self)
        self.rightButton = tk.Label(self, text=">")
        self.rightButton["bg"] = "yellow"
        self.rightButton.bind("<Button-1>", self.rightButtonHandler)

    def createLayout(self):
        # layout the widgets
        self.header.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.leftButton.grid(row=1, column=0, sticky="nsew")
        self.frameContainer.grid(row=1, column=1, sticky="nsew")
        self.rightButton.grid(row=1, column=2, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

    def leftButtonHandler(self, event):
        if self.frameContainer.startIndex > 0:
            self.frameContainer.startIndex -= 1
            self.frameContainer.moveContainer()

    def rightButtonHandler(self, event):
        if (
            self.frameContainer.startIndex
            < len(self.frameContainer.dataFunc()) - self.frameContainer.nofFrames
        ):
            self.frameContainer.startIndex += 1
            self.frameContainer.moveContainer()

    def updateFramesContainer(self):
        self.frameContainer.updateFrameWidgets()
