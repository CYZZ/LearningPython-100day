# 使用网格布局
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
    QHBoxLayout, QWidget, \
    QGridLayout
from PyQt5.QtCore import Qt


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
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
        label = QLabel("第一个标签", self)

        label.move(20, 30)
        label2 = QLabel("第二个标签", self)
        # height = self.menuBar().height()
        # print('height= f',height)
        button_1 = QPushButton('按钮1', self)
        button_1.move(50, 60)
        button_2 = QPushButton('按钮2', self)
        button_2.move(150, 60)

        button_3 = QPushButton('按钮3', self)

        # 创建一个网格布局对对象
        grid_layout = QGridLayout()

        grid_layout.addWidget(label, 0, 0)
        grid_layout.addWidget(button_1, 0, 1)
        grid_layout.addWidget(label2, 1, 0)
        grid_layout.addWidget(button_2, 1, 1)
        grid_layout.addWidget(button_3, 2, 0, 1, 5)

        # 设置对齐方式
        grid_layout.setAlignment(Qt.AlignTop)
        # grid_layout.setAlignment(Qt.AlignBottom)
        # grid_layout.setAlignment(Qt.AlignRight)

        # 创建一个窗口对象
        layout_widget = QWidget()
        layout_widget.setLayout(grid_layout)

        self.setCentralWidget(layout_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
