from networks import setupNetworks

setupNetworks()

import tkinter as tk
from initScreen import initPage

myRoot = tk.Tk()
myRoot["bg"] = "#FEE8B0"
myRoot.title("ChipNet")
myRoot.geometry("1000x700")
myRoot.resizable(False, False)


def networkSelector(title="Select Network"):
    new_window = tk.Toplevel(myRoot)
    new_window.title(title)
    return new_window


x = initPage(networkSelector(), myRoot)
x.pack()
myRoot.mainloop()
