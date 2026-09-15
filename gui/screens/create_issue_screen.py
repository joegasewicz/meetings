import wx

from config import Config
from controllers import IssueController
from gui.utils.fonts import create_title
from meetings import Meeting
from utils.database import Database


class CreateIssueScreen(wx.Panel):

    def __init__(self, parent: wx.Panel, meeting: Meeting):
        super().__init__(parent)
        self.parent = parent
        self.meeting = meeting
        config = Config()
        db = Database(config=config)
        self.issue_controller = IssueController(db)

        sizer = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(self, label="Create New Issue")
        create_title(title)

        sizer.Add(title, wx.ALL, 10)

        self.SetSizer(sizer)
