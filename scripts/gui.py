from tkinter import *
from brownie import run

root = Tk()


def deployContract():
    contractAddress = run("deploy")
    print(f"Contract address: {contractAddress}")


myButton = Button(root, text="fakeRun!", command=deployContract)
myButton.grid(row=0, column=0)
root.mainloop()
