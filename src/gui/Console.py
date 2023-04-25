import tkinter as tk
from tkinter import ttk
from src.gui.header import Header
from src.style import myStyle


class Console(tk.Frame):
    def __init__(self, parent, containerCreatorFunc, heading, height=220, width=1000):
        super().__init__(parent, width=width, height=height, relief="raised")
        self["bg"] = myStyle.consoleBgColor
        self.containerCreatorFunc = containerCreatorFunc
        self.heading = heading
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()
        self.createLayout()

    def createWidgets(self):
        # create the widgets
        self.header = Header(self, heading=self.heading)
        self.leftButton = tk.Label(self, text="«", font=myStyle.arrowFont)
        self.leftButton["bg"] = myStyle.arrowColor
        self.leftButton.bind("<Button-1>", self.leftButtonHandler)
        self.frameContainer = self.containerCreatorFunc(self)
        self.rightButton = tk.Label(self, text="»", font=myStyle.arrowFont)
        self.rightButton["bg"] = myStyle.arrowColor
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
