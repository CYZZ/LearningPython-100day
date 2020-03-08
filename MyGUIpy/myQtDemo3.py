# 添加状态栏
import sys

from PyQt5.QtWidgets import QMainWindow, \
    QApplication, \
    QStatusBar, \
    QMenuBar, \
    QAction, \
    QMenu, \
    QLabel, \
    QPushButton, \
    QVBoxLayout, \
    QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette
import requests
from PyQt5 import QtCore
import json


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_3 = QPushButton()
        self.label2 = QLabel()
        self.label3 = QLabel()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('我是一个window Title')
        self.resize(500, 300)
        self.setMinimumSize(200, 200)
        self.setMaximumSize(500, 600)

        # 调用方法
        self.add_menu_and_status()

        # 调用布局方法
        self.add_postion_layout()

        # 添加点击事件
        self.add_button_event()

    # 设置状态和菜单
    def add_menu_and_status(self):
        # 设置状态栏
        status = QStatusBar()
        status.showMessage('显示文本')
        self.setStatusBar(status)

        # self.statusBar().showMessage('文本信息')

        # 添加菜单栏
        menu = self.menuBar()
        # 创建一个菜单
        file_menu = menu.addMenu('文件')
        # 创建一个行为
        new_action = QAction('新建文件', self)
        # 将行为添加到菜单
        file_menu.addAction(new_action)
        file_menu.addSeparator()
        # 更新状态栏文本
        new_action.setStatusTip('点击可以新建一个文件')

        edit_menu = menu.addMenu('修改')
        change_acion = QAction('设置', self)
        edit_menu.addAction(change_acion)

        # 创建另一个行为
        exit_action = QAction('退出', self)
        # 退出操作
        exit_action.setStatusTip("点击退出程序")
        # 点击关闭应用
        exit_action.triggered.connect(self.close)
        # 设置快捷键
        exit_action.setShortcut('Ctrl+Q')
        # 添加退出行为到菜单上
        file_menu.addAction(exit_action)

    # 添加控件
    def add_postion_layout(self):
        label = QLabel("第一个标签看看效果", self)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.red)
        label.setPalette(palette)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("QWidget{background-color:#ff9911}")  # 这是一个css风格的颜色设置

        label.move(20, 30)
        # height = self.menuBar().height()
        # print('height= f',height)
        button_1 = QPushButton('按钮1', self)
        button_1.move(50, 60)
        button_2 = QPushButton('按钮2', self)
        button_2.move(150, 60)

        self.button_3 = QPushButton('按钮3', self)
        self.button_3.move(200, 70)

        self.label2 = QLabel("这是第二个标签", self)
        self.label2.setWordWrap(True)

        self.label3 = QLabel("这是第三个标签",self)
        self.label3.setWordWrap(True)


        # 设置布局
        # 创建两个盒子
        hbox_1 = QHBoxLayout()
        hbox_2 = QHBoxLayout()
        hbox_3 = QHBoxLayout()

        hbox_1.addWidget(label)
        hbox_1.addWidget(button_1)

        hbox_2.addWidget(button_2)

        hbox_3.addWidget(self.button_3)
        # 创建一个垂直的盒子，包含两个水平盒子
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
        vbox.addLayout(hbox_3)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)

        # 创建一个窗口部件，设置布局为垂直的盒子
        layout_widget = QWidget()
        layout_widget.setLayout(vbox)

        # self.setCentralWidget(layout_widget)
        self.setMenuWidget(layout_widget)

    def add_button_event(self):
        print('开始调用了addButtonEvent')
        self.button_3.setCheckable(True)
        self.button_3.clicked[bool].connect(self.button3_lick)
        # QtCore.QObject.connectNotify()
        # self.button_3.clicked.connect
        # self.button_3.clicked(True)

    def button3_lick(self, p):
        if p:
            self.label2.setText('被重新赋值了')
        else:
            self.label2.setText('被还原了')
        # 开始网络请求测试
        r0 = requests.get('https://api.apiopen.top/getJoke?page=1&count=2&type=text')
        # r0 = requests.get('https://api.apiopen.top/recommendPoetry')

        print(r0.content)
        print(type(r0.content))

        str1 = str(r0.content, encoding="utf-8")

        data = json.loads(str1)
        print(data)
        message = data["message"]
        result = data["result"]
        print("message =", message)
        print("result=", result)

        # 开始字典转模型
        obj = self.dict_to_object(data)
        print(obj.result[0].text)
        print(obj.result[1].text)
        self.label2.setText(obj.result[0].text)
        self.label3.setText(obj.result[1].text)

        print(p)
        print("调用了button3Click")

    # 递归调用解析数据
    def dict_to_object(self, dictObj):
        if not isinstance(dictObj, dict):
            # 如果是数组类型就要逐个解析
            if isinstance(dictObj, list):
                inst = list()
                for item in dictObj:
                    print(item)
                    inst.append(self.dict_to_object(item))
                return inst
            return dictObj
        inst = Dict()
        for k, v in dictObj.items():
            inst[k] = self.dict_to_object(v)
        return inst


class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
