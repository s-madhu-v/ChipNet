import tkinter as tk
from tkinter import ttk

adsContainerbackground = "blue"


class Container(ttk.Frame):
    def __init__(
        self,
        parent,
        dataFunc,
        widgetDataFunc,
        frameClass,
        width,
        height,
        containerSize=4,
        startIndex=0,
        backgroundColor="green",
    ):
        super().__init__(
            parent, width=width, height=height, relief="raised", padding=10
        )
        self.dataFunc = dataFunc
        self.widgetDataFunc = widgetDataFunc
        self.frameClass = frameClass
        self.startIndex = startIndex
        self.containerSize = containerSize
        self.nofFrames = min(self.containerSize, len(dataFunc()))
        self.frameWidgets = []
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.createWidgets()
        self.startAdIndx = 0  # remove this later; indentaion issues?
        print(f"\n\n====={self.nofFrames}=====\n\n")  # this too

    def createWidgets(self):
        for i in range(self.nofFrames):
            widget = self.frameClass(self, self.dataFunc()[self.startIndex + i])
            self.frameWidgets.append(widget)
            widget.grid(row=0, column=i, sticky="nsew", padx=10)

    def handleNoOfFramesChange(self):
        self.nofFrames = min(self.containerSize, len(self.dataFunc()))
        if self.nofFrames < len(self.frameWidgets):
            for i in range(self.nofFrames, len(self.FrameWidgets)):
                self.frameWidgets[i].destroy()
            self.frameWidgets = self.frameWidgets[: self.nofFrames]
        elif self.nofFrames > len(self.frameWidgets):
            for i in range(len(self.frameWidgets), self.nofFrames):
                widget = self.frameClass(self, self.dataFunc()[self.startIndex + i])
                self.frameWidgets.append(widget)
                widget.pack(side="left", padx=10)

    def moveContainer(self):
        # self.handleNoOfFramesChange()
        for i in range(self.nofFrames):
            self.widgetDataFunc(
                self.frameWidgets[i], self.dataFunc()[self.startIndex + i]
            )

    def updateFrameWidgets(self):
        self.moveContainer()
