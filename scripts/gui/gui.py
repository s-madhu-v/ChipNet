# The entrypoint for the GUI

import tkinter as tk
from scripts.gui.windowNotebook import windowNotebook
from scripts.contract.getters import getAllAds
from scripts.gui.populate import populateAds
from scripts.gui.marketplace import marketplace

if len(getAllAds()) == 1:
    print("Populating Ads")
    populateAds()

# Create the root window
root = tk.Tk()

# set the title for the window
root.title("ChipNet")

# set the size of the window
root.geometry("1000x750")

# make the window unresizable
root.resizable(False, False)

# Create the notebook
# notebook = windowNotebook(root)

# pack the notebook
# notebook.pack()

# Create the marketplace
mk = marketplace(root)
mk.grid(row=0, column=0, sticky="nsew")


def main():
    # run the event loop
    root.mainloop()
