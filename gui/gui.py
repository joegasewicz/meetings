import wx

from meetings.meeting import Meeting
from gui.screens import (
    MainScreen,
)


class Gui:

    wx_app: wx.App
    home_frame: wx.Frame
    meeting: Meeting

    def __init__(self, *, meeting: Meeting):
        self.meeting = meeting
        self.wx_app = wx.App()
        self.main_screen = MainScreen(None, "Standup App", meeting)

    def run(self) -> None:
        self.wx_app.MainLoop()
