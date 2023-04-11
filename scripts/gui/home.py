import wx
from scripts.deploy import populateAds
from scripts.marketplace_helpers import getAds
from random import randint


class Home(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour(wx.Colour(255, 0, 255))
        # create a scrollable panel
        self.scrolled_panel = wx.ScrolledWindow(self, style=wx.VSCROLL)
        self.scrolled_panel.SetScrollRate(0, 20)
        self.scrolled_panel.SetBackgroundColour(wx.Colour(255, 0, 0))

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.scrolled_panel.SetSizer(self.sizer)

        # add random 20 static text elements to the sizer
        for i in range(20):
            self.sizer.Add(
                wx.StaticText(self.scrolled_panel, label=f"Vicky: {randint(0, 1000)}"),
                0,
                wx.ALL,
                50,
            )
        self.scrolled_panel.SetScrollbars(1, 1, 1, 1)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.scrolled_panel, 1, wx.EXPAND)
        self.SetSizer(main_sizer)
        self.Layout()


def main():
    if len(getAds()) == 0:
        populateAds()
    app = wx.App()
    frame = wx.Frame(None, title="ChipNet")
    panel = Home(frame)
    frame.Show()
    app.MainLoop()
