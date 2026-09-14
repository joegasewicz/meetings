import wx


class MainScreen(wx.Frame):

    def __init__(self, parent: str, title: str):
        wx.Frame.__init__(self, parent, title=title, size=(1000, 700))
        # self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        self.CreateStatusBar()

        # Main menu
        file_menu = wx.Menu()
        file_menu.Append(wx.ID_ANY, "&New Project", "Create a new project")
        file_menu.AppendSeparator()
             # Status bar
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        self.SetMenuBar(menu_bar)


        self.Show(True)
