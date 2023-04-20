from brownie import *

p = project.load('', name="ChipNet")
p.load_config()
from brownie.project.ChipNet import *
network.connect('ganache-GUI')
