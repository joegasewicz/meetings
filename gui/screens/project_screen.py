import wx

from gui.screens.home_screen import HomeScreen


class ProjectScreen(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        sizer = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(self, label="Create New Project")
        name_label = wx.StaticText(self, label="Project name")
        self.name_input = wx.TextCtrl(self)

        cancel_button = wx.Button(self, label="Cancel")
        cancel_button.Bind(wx.EVT_BUTTON, self._on_cancel)

        sizer.Add(title, 0, wx.ALL, 10)
        sizer.Add(name_label, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
        sizer.Add(self.name_input, 0, wx.ALL | wx.EXPAND, 10)
        sizer.Add(cancel_button, 0, wx.ALL, 10)

        self.SetSizer(sizer)

    def _on_cancel(self, event: wx.Event) -> None:
        self.parent.show_screen(HomeScreen)
