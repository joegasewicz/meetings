import wx

from controllers.issues import IssueController
from gui.utils.fonts import create_title
from meetings.meeting import Meeting
from meetings.controllers import (
    ProjectController,
)
from gui.screens.create_issue_screen import CreateIssueScreen
from models import IssueModel
from utils.database import Database
from config import Config
from utils.logger import log


class ProjectDetailScreen(wx.Panel):

    selected_issue: IssueModel

    def __init__(self, parent, meeting: Meeting, project_id: int):
        super().__init__(parent)
        self.meeting = meeting
        self.project_id = project_id
        self.parent = parent
        log.info(f"Project detail with id: {project_id}")

        config = Config()
        db = Database(config=config)
        self.project_controller = ProjectController(db)
        self.issue_controller = IssueController(db)
        self.issues = self.issue_controller.fetch_all(data={"project_id": project_id})

        sizer = wx.BoxSizer(wx.VERTICAL)

        content_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Left Column
        left_column = self.display_left_col()

        vertical_line = wx.StaticLine(self, style=wx.LI_VERTICAL)

        # Right Column
        self.right_column = self.display_right_col()

        # Right Inner Detail Area
        self.right_inner_detail_column, self.right_inner_detail_sizer = self.right_inner_detail_col()
        self.right_sizer.Add(self.right_inner_detail_column, 1, wx.EXPAND | wx.ALL, 10)

        # Set Columns to main Content
        content_sizer.Add(left_column, 1, wx.EXPAND | wx.ALL, 10)
        content_sizer.Add(vertical_line, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 100)
        content_sizer.Add(self.right_column, 3, wx.EXPAND | wx.ALL, 10)

        # Top menu
        data = {"project_id": self.project_id}
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

        # Title
        issue_title = wx.StaticText(left_column, label="Issues")
        create_title(issue_title)
        left_sizer.Add(issue_title, 0, wx.EXPAND | wx.ALL, 10)

        # Issue Create Button
        create_button = wx.Button(left_column, label="Create issue")
        create_button.Bind(wx.EVT_BUTTON, lambda e: self.parent.show_screen(CreateIssueScreen, self.meeting, self.project_id))
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(create_button, 0)
        left_sizer.Add(button_sizer, 0, wx.ALL, 10)

        line = wx.StaticLine(left_column)
        left_sizer.Add(line, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # Issues
        self.issue_list = wx.ListBox(
            left_column,
            choices=[f"{issue.name} - ({issue.status.name})" for issue in self.issues],
            style=wx.LB_SINGLE,
        )
        self.issue_list.Bind(wx.EVT_LISTBOX, self.on_issue_select)
        left_sizer.Add(self.issue_list, 1, wx.EXPAND | wx.ALL, 10)

        left_column.SetSizer(left_sizer)
        return left_column

    def display_right_col(self) -> wx.Panel:
        self.right_sizer = wx.BoxSizer(wx.VERTICAL)
        self.right_column = wx.Panel(self)
        title = wx.StaticText(self.right_column, label="Issue Details")
        create_title(title)

        self.right_sizer.Add(title, 0, wx.EXPAND | wx.ALL, 10)
        self.right_column.SetSizer(self.right_sizer)
        return self.right_column

    def right_inner_detail_col(self) -> tuple[wx.Panel, wx.BoxSizer]:
        inner_sizer = wx.BoxSizer(wx.VERTICAL)
        inner_column = wx.Panel(self.right_column)

        inner_column.SetSizer(inner_sizer)
        return inner_column, inner_sizer

    def on_issue_select(self, event):
        self.right_inner_detail_sizer.Clear(delete_windows=True)
        index = event.GetSelection()
        self.selected_issue = self.issues[index]
        self.right_inner_detail_sizer.AddSpacer(20)
        # Name
        title = wx.StaticText(self.right_inner_detail_column, label=self.selected_issue.name)
        create_title(title=title, size=15)
        self.right_inner_detail_sizer.Add(title, 0, wx.EXPAND | wx.ALL, 10)

        # Notes
        notes = wx.StaticText(self.right_inner_detail_column, label=self.selected_issue.notes or "No notes")
        notes.Wrap(400)
        self.right_inner_detail_sizer.Add(notes, 0, wx.EXPAND | wx.ALL, 10)

        # Deadline
        date_label = f"Deadline: {self.selected_issue.deadline.strftime('%d/%m/%Y') or 'No deadline'}"
        deadline = wx.StaticText(
            self.right_inner_detail_column,
            label=date_label,
        )
        self.right_inner_detail_sizer.Add(deadline, 0, wx.EXPAND | wx.ALL, 10)

        # Status
        status_label = wx.StaticText(
            self.right_inner_detail_column,
            label=f"Status: {self.selected_issue.status.name}",
        )
        self.right_inner_detail_sizer.Add(status_label, 0, wx.EXPAND | wx.ALL, 10)

        self.right_inner_detail_column.Layout()
        self.right_column.Layout()
