import tkinter as tk
from tkinter import ttk

adConsolebackground = "red"


class Console(ttk.Frame):
    def __init__(self, parent, containerCreatorFunc, backgroundColor="red"):
        super().__init__(parent, width=860, height=170, relief="raised")
        self.containerCreatorFunc = containerCreatorFunc
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()
        self.createLayout()
        ttk.Style().configure("Console.TFrame", background=backgroundColor)
        self["style"] = "Console.TFrame"

    def createWidgets(self):
        # create the widgets
        self.leftButton = tk.Button(self, text="<", width=1, height=9)
        self.leftButton["command"] = lambda: self.leftButtonHandler()
        self.frameContainer = self.containerCreatorFunc(self)
        self.rightButton = tk.Button(self, text=">", width=1, height=9)
        self.rightButton["command"] = lambda: self.rightButtonHandler()

    def createLayout(self):
        # layout the widgets
        self.leftButton.pack(side="left")
        self.frameContainer.pack(side="left")
        self.rightButton.pack(side="left")

    def leftButtonHandler(self):
        if self.frameContainer.startIndex > 0:
            self.frameContainer.startIndex -= 1
            self.frameContainer.moveContainer()

    def rightButtonHandler(self):
        if (
            self.frameContainer.startIndex
            < len(self.frameContainer.dataFunc()) - self.frameContainer.nofFrames
        ):
            self.frameContainer.startIndex += 1
            self.frameContainer.moveContainer()

    def updateFramesContainer(self):
        self.frameContainer.updateFrameWidgets()
