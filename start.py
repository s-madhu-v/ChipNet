# from brownie import *
# p = project.load('', name="ChipNet")
# p.load_config()
# project.run("scripts/gui/gui.py")

# from myTkinter import myTk
# from chipnetapp import imtest# , main
# from new_mod.func import imfunc
from networks import setupNetworks

setupNetworks()

from chipnetapp.gui.gui import main

print("Starting Main()")
main()
print("Ended Main()")
