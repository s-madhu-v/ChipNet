# The entrypoint for the GUI

import tkinter as tk
from tkinter import ttk
from scripts.gui.windowNotebook import windowNotebook
from scripts.contract.getters import getAllAds
from scripts.gui.populate import populateAds


if len(getAllAds()) == 1:
    print("Populating Ads")
    populateAds()

print("Initializing root")

# Create the root window
root = tk.Tk()

# set the title for the window
root.title("ChipNet")

# set the size of the window
root.geometry("1000x750")

# make the window unresizable
root.resizable(False, False)

# Create the notebook
notebook = windowNotebook(root)

# pack the notebook
notebook.pack()


def main():
    # run the event loop
    root.mainloop()
