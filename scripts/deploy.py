from brownie import accounts, ChipNet, web3
import time
import os


def main():
    myAccount = accounts[0]
    # deploy the contract to the network
    chipNet = ChipNet.deploy({"from": myAccount})
    # print the address of the contract
    print(f"Contract address: {chipNet.address}")
    # print the balance of the contract
    print(f"Contract balance: {web3.fromWei(chipNet.balance(), 'ether')} ETH")
    # print the balance of the account that deployed the contract
    print(f"Account balance: {web3.fromWei(myAccount.balance(), 'ether')} ETH")
