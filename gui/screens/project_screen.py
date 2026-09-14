import wx

from gui.screens.home_screen import HomeScreen
from gui.utils.fonts import create_title
from utils.logger import log


class ProjectScreen(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        sizer = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(self, label="Create New Project")
        create_title(title)

        name_label = wx.StaticText(self, label="Project name")
        self.name_input = wx.TextCtrl(self)

        # Buttons
        submit_button = wx.Button(self, label="Submit")
        submit_button.Bind(wx.EVT_BUTTON, self.on_submit)
        cancel_button = wx.Button(self, label="Cancel")
        cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)

        sizer.Add(title, 0, wx.ALL, 10)
        sizer.Add(name_label, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
        sizer.Add(self.name_input, 0, wx.ALL | wx.EXPAND, 10)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(submit_button, 0)
        button_sizer.Add(cancel_button, 0, wx.LEFT, 5)
        sizer.Add(button_sizer, 0, wx.ALL, 10)

        self.SetSizer(sizer)

    def on_cancel(self, event: wx.Event) -> None:
        self.parent.show_screen(HomeScreen)

    def on_submit(self, event: wx.Event):
        project_name = self.name_input.GetValue()
        log.info(f"Created new project: {project_name}")
        

