import wx


def create_title(
    title: wx.StaticText,
    size: int = 20,
    weight: int = wx.FONTWEIGHT_BOLD
) -> None:
    """
    Increase a static strings font size & weight.
    :param title:
    :param size:
    :param weight:
    :return:
    """
    title_font = title.GetFont()
    title_font.SetPointSize(size)
    title_font.SetWeight(weight)
    title.SetFont(title_font)
