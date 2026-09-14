import wx

from gui.screens.project_screen import ProjectScreen
from gui.screens.home_screen import HomeScreen
from meetings import Meeting


class MainScreen(wx.Frame):

    current_screen: wx.Panel

    def __init__(self, parent: str, title: str, meeting: Meeting):
        wx.Frame.__init__(self, parent, title=title, size=(1000, 700))
        self.meeting = meeting
        self.current_screen = None
        self.show_screen(HomeScreen, self.meeting)
        self._create_menu()

        self.Show(True)

    def _create_menu(self) -> None:
        self.CreateStatusBar()
        # Main menu
        file_menu = wx.Menu()
        new_project_item = file_menu.Append(wx.ID_ANY, "&New Project", "Create a new project")
        file_menu.AppendSeparator()
        # Status bar
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_MENU, self._on_new_project, new_project_item)

    def _on_new_project(self, event: wx.Event) -> None:
        self.show_screen(ProjectScreen, self.meeting)

    def show_screen(self, screen_class, *args, **kwargs):
        if self.current_screen:
            self.current_screen.Destroy()
        self.current_screen = screen_class(self, *args, **kwargs)
        self.current_screen.Show()
        self.Layout()
