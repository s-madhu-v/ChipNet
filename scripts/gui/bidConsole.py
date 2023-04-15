import tkinter as tk
from tkinter import ttk
from scripts.gui.bidsContainer import createBidsContainer
from scripts.gui.Console import Console
from scripts.data import contractData

bidConsolebackground = "red"


def createBidConsole(parent):
    return Console(parent, createBidsContainer)
