import wx
import wx.xrc
import SubClassFrame as vf

app = wx.App(clearSigInt = True)
frame = vf.SubClassFrame(parent=None)
frame.Show()
app.MainLoop()

