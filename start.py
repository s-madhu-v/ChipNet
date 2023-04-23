# from brownie import *
# p = project.load('', name="ChipNet")
# p.load_config()
# project.run("scripts/gui/gui.py")

# from myTkinter import myTk
# from chipnetapp import imtest# , main
# from new_mod.func import imfunc
from networks import setupNetworks

setupNetworks()

import tkinter as tk
from initScreen import initPage

myRoot = tk.Tk()
myRoot.title("Madhu Surisetti")
myRoot.geometry("1000x750")
myRoot.resizable(False, False)


def networkSelector(title="Select Network"):
    new_window = tk.Toplevel(myRoot)
    new_window.title(title)
    return new_window


x = initPage(networkSelector(), myRoot)
x.pack()
myRoot.mainloop()
