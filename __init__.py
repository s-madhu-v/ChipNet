from brownie import *

network.connect('ganache-GUI')
p = project.load('', name="ChipNet")
p.load_config()

from brownie import ChipNet

# project.run("./gui/gui.py")

from scripts.gui.gui import main

result = main
