import wx

from gui.utils.fonts import create_title
from meetings.models import (
    ProjectModel,
)


class HomeScreen(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(self, label="Home")
        create_title(title)

        line = wx.StaticLine(self)

        project_title = wx.StaticText(self, label="Projects")
        create_title(project_title)

        projects = self.get_projects()

        sizer.Add(title, 0, wx.ALL, 10)
        sizer.Add(line, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        sizer.AddSpacer(20)
        sizer.Add(project_title, 0, wx.ALL, 10)

        self.SetSizer(sizer)

    def get_projects(self) -> list[ProjectModel]:
        pass