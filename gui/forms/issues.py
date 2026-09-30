import wx

class IssueForm(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        grid = wx.FlexGridSizer(rows=2, cols=2, vgap=8, hgap=8)
        grid.AddGrowableCol(1, 1)

        self.name_ctrl = wx.TextCtrl(self)

        grid.Add(wx.StaticText(self, label="Name:"), 0, wx.ALIGN_CENTER_VERTICAL)
        grid.Add(self.name_ctrl, 1, wx.EXPAND)

        main_sizer.Add(grid, 1, wx.ALL | wx.EXPAND, 12)
        self.SetSizer(main_sizer)
