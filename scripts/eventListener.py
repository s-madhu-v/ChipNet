from brownie import accounts, ChipNet, web3, network
import time
import os
import git
from scripts.backend import run


def handle_ad_purchase(event):
    print(f"\n\n\n\nEvent triggered with arguments: {event.args}\n\n\n\n")
    run()


contractAddr = os.getenv("CONTRACT_ADDRESS")
contract = ChipNet.at(contractAddr)
x = network.contract.ContractEvents(contract)
x.subscribe("AdPurchased", handle_ad_purchase)

print("\nEvent Listerer Started:\n")
while True:
    time.sleep(1)
