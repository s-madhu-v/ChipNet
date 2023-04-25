import tkinter as tk
from src.style import myStyle


class Header(tk.Frame):
    def __init__(
        self, parent, heading="Sample Heading!!!", height=myStyle.headerHeight
    ):
        super().__init__(parent)
        self.heading = heading
        self.grid_propagate(False)
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        self.label = tk.Label(self, text=self.heading, font=myStyle.headerFont)
        self.label["bg"] = myStyle.headerColor
        self.label.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
