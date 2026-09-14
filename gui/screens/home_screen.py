import wx

from gui.utils.fonts import create_title
from meetings.models import (
    ProjectModel,
)
from controllers import (
    AbstractController,
    ProjectController,
)
from utils.logger import log
from utils.database import Database
from config import Config


class HomeScreen(wx.Panel):

    project_controller: AbstractController

    def __init__(self, parent):
        super().__init__(parent)
        db = Database(config=Config())
        self.project_controller = ProjectController(db)

        sizer = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(self, label="Home")
        create_title(title)

        line = wx.StaticLine(self)

        project_title = wx.StaticText(self, label="Projects")
        create_title(project_title)

        sizer.Add(title, 0, wx.ALL, 10)
        sizer.Add(line, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        sizer.AddSpacer(20)
        sizer.Add(project_title, 0, wx.ALL, 10)

        projects = self.project_controller.fetch_all()
        log.info(f"Fetched Projects...{projects}")
        if len(projects) == 0:
            projects_msg = wx.StaticText(self, label="You have no projects.")
            sizer.Add(projects_msg, 0, wx.ALL, 10)

        self.SetSizer(sizer)
