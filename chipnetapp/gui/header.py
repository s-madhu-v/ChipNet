import tkinter as tk


class Header(tk.Frame):
    def __init__(self, parent, heading="Sample Heading!!!"):
        super().__init__(parent)
        self.heading = heading
        self.grid_propagate(False)
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        self.label = tk.Label(self, text=self.heading, font=("Arial", 20))
        self.label["bg"] = "red"
        self.label.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
