import tkinter as tk
from tkinter import ttk
from scripts.gui.adsContainer import createAdsContainer
from scripts.gui.Console import Console
from scripts.data import contractData

adConsolebackground = "red"


def createAdConsole(parent):
    return Console(parent, createAdsContainer)
