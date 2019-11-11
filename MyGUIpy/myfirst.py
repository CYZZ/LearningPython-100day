import wx
import qrcode
import os


class myfirst(wx.Frame):
    fileContent = wx.TextCtrl
    win = wx.Frame

    def __init__(self, parent, title):
        super(myfirst, self).__init__(parent, title=title, size=(400, 500))

    def createGUI(self):
        win = wx.Frame(None, title=self.Title, size=self.GetSize())
        win.SetMinSize(self.GetSize())
        win.SetMaxSize(self.GetSize() * 2)
        win.Show()
        # 保存属性
        self.win = win

        openButton = wx.Button(win, label='Open', pos=(225, 5), size=(80, 25))
        saveButton = wx.Button(win, label='Save', pos=(315, 5), size=(80, 25))

        saveButton.Bind(wx.EVT_BUTTON, self.saveButtonClick)
        openButton.Bind(wx.EVT_BUTTON, self.openButtonClick)

        fileName = wx.TextCtrl(win, pos=(5, 5), size=(210, 25))
        # fileName.Value = '默认文字'
        fileName.ChangeValue('默认文字')
        fileContent = wx.TextCtrl(win, pos=(5, 35), size=(390, 260), style=wx.TE_MULTILINE | wx.HSCROLL)
        fileContent.SetHelpText('占位文字？')
        self.fileContent = fileContent

    def saveButtonClick(self, event):
        print("saveButton被点击了")
        root_dir = os.path.abspath(".")
        print(root_dir)

    def openButtonClick(self, event):
        print("OpenButton被点击了")
        data = self.fileContent.Value
        print("当前需要显示成二维码的内容=")
        print(data)
        # 生成二维码
        img = qrcode.make(data=data)

        # 直接显示二维码
        img.show()

        # 保存二维码为文件
        # img.save("baidu.jpg")


app = wx.App()
first = myfirst(None, '嘿嘿嘿')

first.createGUI()
app.MainLoop()
