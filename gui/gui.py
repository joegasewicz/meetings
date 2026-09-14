import wx

from meetings.meeting import Meeting
from gui.screens import (
    MainScreen,
)


class Gui:

    wx_app: wx.App
    home_frame: wx.Frame
    issue_tracker: Meeting

    def __init__(self, *, issue_tracker: Meeting):
        self.issue_tracker = issue_tracker
        self.wx_app = wx.App()

        self.main_screen = MainScreen(None, "Standup App")

    def run(self) -> None:
        self.wx_app.MainLoop()
