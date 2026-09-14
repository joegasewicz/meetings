import wx


class HomeScreen(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(self, label="Home")
        sizer.Add(title, 0, wx.ALL, 10)

        self.SetSizer(sizer)
