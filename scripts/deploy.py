from brownie import accounts, ChipNet, web3
import os


# A function to print balances of all accounts created by ganache
def printBalances():
    for account in accounts:
        print(f"ACCOUNT: {account}")
        print(
            f"The balance of this account is {web3.fromWei(account.balance(), 'ether')} ETH"
        )


def main():
    myAccount = accounts[0]
    buyerAccount = accounts[1]
    sellerAccount = accounts[2]
    # deploy the contract to the network
    chipNet = ChipNet.deploy({"from": myAccount})
    # print the address of the contract
    print(f"Contract address: {chipNet.address}")
    # print the balance of the contract
    print(f"Contract balance: {web3.fromWei(chipNet.balance(), 'ether')} ETH")
    # print the balance of the account that deployed the contract
    print(f"Account balance: {web3.fromWei(myAccount.balance(), 'ether')} ETH")
    # post an advertisement
    txn = chipNet.postAd(
        "My Ad", "I am selling 1000 chips for 1 ETH", 200, {"from": sellerAccount}
    )
    txn.wait(1)
    # print the number of ads
    print(f"Number of ads: {chipNet.getAdsCount()}")
    # print the latest ad
    print(f"Latest ad: {chipNet.getAd(chipNet.getAdsCount() - 1)}")
