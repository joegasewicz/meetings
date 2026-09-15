import wx

from gui.utils.fonts import create_title
from meetings.meeting import Meeting
from meetings.models import (
    ProjectModel,
    UserModel,
)
from meetings.controllers import (
    ProjectController,
)
from utils.database import Database
from config import Config
from utils.logger import log


class ProjectDetailScreen(wx.Panel):

    def __init__(self, parent: wx.Panel, meeting: Meeting, project_id: int):
        super().__init__(parent)
        self.meeting = meeting
        self.project_id = project_id
        log.info(f"Project detail with id: {project_id}")

        config = Config()
        db = Database(config=config)
        self.project_controller = ProjectController(db)

        sizer = wx.BoxSizer(wx.VERTICAL)

        content_sizer = wx.BoxSizer(wx.HORIZONTAL)

        left_column = self.display_left_col()
        vertical_line = wx.StaticLine(self, style=wx.LI_VERTICAL)
        right_column = self.display_right_col()

        content_sizer.Add(left_column, 1, wx.EXPAND | wx.ALL, 10)
        content_sizer.Add(vertical_line, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 100)
        content_sizer.Add(right_column, 3, wx.EXPAND | wx.ALL, 10)

        # Top menu

        data = {"project_id": project_id}
        project = self.project_controller.fetch_one(data=data)

        title = wx.StaticText(self, label=f"Project - {project.name}", style=wx.ALIGN_CENTRE)
        create_title(title)

        line = wx.StaticLine(self)

        sizer.Add(title, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(line, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        sizer.Add(content_sizer, 1, wx.EXPAND)

        self.SetSizer(sizer)


    def display_left_col(self) -> wx.Panel:
        left_column = wx.Panel(self)
        left_sizer = wx.BoxSizer(wx.VERTICAL)

        issue_title = wx.StaticText(left_column, label="Issues")
        create_title(issue_title)

        left_sizer.Add(issue_title, 0, wx.EXPAND | wx.ALL, 10)
        left_column.SetSizer(left_sizer)
        return left_column

    def display_right_col(self) -> wx.Panel:
        right_column = wx.Panel(self)
        right_sizer = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(right_column, label="Issue Details")
        create_title(title)

        right_sizer.Add(title, 0, wx.EXPAND | wx.ALL, 10)
        right_column.SetSizer(right_sizer)
        return right_column
