import wx

from config import Config
from controllers.issues import IssueController
from controllers.statuses import StatusController
from gui.utils.fonts import create_title
from meetings import Meeting
from utils.database import Database
from gui.forms import IssueForm
from utils.logger import log


class CreateIssueScreen(wx.Panel):

    def __init__(self, parent: wx.Panel, meeting: Meeting, project_id: int):
        super().__init__(parent)
        self.parent = parent
        self.meeting = meeting
        self.project_id = project_id
        config = Config()
        db = Database(config=config)
        self.issue_controller = IssueController(db)
        self.status_controller = StatusController(db)

        sizer = wx.BoxSizer(wx.VERTICAL)

        # Title
        title = wx.StaticText(self, label="Create New Issue", style=wx.ALIGN_CENTRE)
        create_title(title)
        sizer.Add(title, 0, wx.EXPAND | wx.ALL, 10)
        # Title line
        line = wx.StaticLine(self)
        sizer.Add(line, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        sizer.AddSpacer(20)

        # Form
        self.issue_form = IssueForm(
            parent=self,
            top_parent=parent,
            database=db,
            issue_controller=self.issue_controller,
            status_controller=self.status_controller,
            meeting=self.meeting,
            user_id=self.meeting.user.id,
            project_id=self.project_id,
        )
        self._display_form(sizer)

        self.SetSizer(sizer)

    def _display_form(self, sizer) -> None:
        form_row = wx.BoxSizer(wx.HORIZONTAL)
        form_left_spacer = wx.Panel(self)
        form_right_spacer = wx.Panel(self)

        form_row.Add(form_left_spacer, 2, wx.EXPAND)
        form_row.Add(self.issue_form, 6, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)
        form_row.Add(form_right_spacer, 2, wx.EXPAND)
        sizer.Add(form_row, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)
