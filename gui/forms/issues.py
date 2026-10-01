from datetime import date

import wx
import wx.adv

from controllers import AbstractController

from meetings import Meeting
from utils.database import Database
from utils.logger import log


class IssueForm(wx.Panel):

    name: str
    notes: str
    deadline: wx.DateTime
    status_id: str

    def __init__(
        self, *,
        parent,
        top_parent,
        database: Database,
        issue_controller: AbstractController,
        status_controller: AbstractController,
        meeting: Meeting,
        project_id: int,
        user_id: int,
    ):
        super().__init__(parent)
        self.database = database
        self.issue_controller = issue_controller
        self.status_controller = status_controller
        self.parent = parent
        self.top_parent = top_parent
        self.meeting = meeting
        self.project_id = project_id
        self.user_id = user_id

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        grid = wx.FlexGridSizer(rows=5, cols=2, vgap=8, hgap=8)
        grid.AddGrowableCol(1, 1)

        # Name
        self.name_ctrl = wx.TextCtrl(self)
        grid.Add(wx.StaticText(self, label="Name:"), 0, wx.ALIGN_CENTER_VERTICAL)
        grid.Add(self.name_ctrl, 1, wx.EXPAND)

        # Notes
        self.notes_ctrl = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_WORDWRAP)
        grid.Add(wx.StaticText(self, label="Notes:"), 0, wx.ALIGN_CENTER_VERTICAL)
        grid.Add(self.notes_ctrl, 1, wx.EXPAND)

        # Deadline
        self.deadline_ctrl = wx.adv.DatePickerCtrl(self)
        grid.Add(wx.StaticText(self, label="Deadline:"), 0, wx.ALIGN_CENTER_VERTICAL)
        grid.Add(self.deadline_ctrl, 1, wx.EXPAND)

        # Status
        choices = [status.name for status in self.meeting.statuses]
        self.status_ctrl = wx.ComboBox(self, value="Backlog", choices=choices, style=wx.CB_READONLY)
        grid.Add(wx.StaticText(self, label="Status:"), 0, wx.ALIGN_CENTER_VERTICAL)
        grid.Add(self.status_ctrl, 1, wx.EXPAND)

        # Submit
        self.submit_btn = wx.Button(self, label="Create", style=wx.ALIGN_CENTER)
        self.submit_btn.Bind(wx.EVT_BUTTON, self.on_submit)
        grid.Add(wx.StaticText(self, label=""), 0, wx.ALIGN_CENTER_VERTICAL) # Spacer
        grid.Add(self.submit_btn, 1, wx.EXPAND)

        main_sizer.Add(grid, 1, wx.ALL | wx.EXPAND, 12)
        self.SetSizer(main_sizer)

    def on_submit(self, event) -> None:
        from gui.screens.project_detail_screen import ProjectDetailScreen
        self.name = self.name_ctrl.GetValue()
        self.notes = self.notes_ctrl.GetValue()
        deadline = self.deadline_ctrl.GetValue()
        self.status_name = self.status_ctrl.GetValue()

        # get status by name
        data = {"name": self.status_name}
        status = self.status_controller.fetch_one(data=data)
        if not status:
            return # TODO

        issue_date = date(
            year=deadline.GetYear(),
            month=deadline.GetMonth(),
            day=deadline.GetDay(),
        )

        data = {
            "name": self.name,
            "notes": self.notes,
            "deadline": issue_date,
            "status_id": status.id,
            "project_id": self.project_id,
            "user_id": self.user_id,
        }

        issue = self.issue_controller.create(data=data)
        if not issue:
            pass # TODO
        self.top_parent.show_screen(ProjectDetailScreen, self.meeting, self.project_id)
