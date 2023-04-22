from myTkinter import myTk, myTtk
tk = myTk
ttk = myTtk

# from tkinter import ttk

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
        self.dataFunc = dataFunc
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

    def destroyWidgets(self):
        for widget in self.frameWidgets:
            widget.destroy()
        self.frameWidgets = []

    def moveContainer(self):
        if self.nofFrames > self.containerSize:
            for i in range(self.nofFrames):
                self.widgetDataFunc(
                    self.frameWidgets[i], self.dataFunc()[self.startIndex + i]
                )
        else:
            self.nofFrames = min(self.containerSize, len(self.dataFunc()))
            self.destroyWidgets()
            self.createWidgets()

    def updateFrameWidgets(self):
        self.moveContainer()
