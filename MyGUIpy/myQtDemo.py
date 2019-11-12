from PyQt5 import QtWidgets, QtGui
# import PyQt5

import sys


# 参考教程https://zmister.com/archives/category/guidevelop/pyqt5_basic/

class GUi():
    def __init__(self):
        self.window = QtWidgets.QWidget()
        self.initUI()

    def initUI(self):
        self.window.setWindowTitle('我是个牛逼的标题')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = GUi()
    gui.window.show()
    sys.exit(app.exec_())

# app = QtWidgets.QApplication(sys.argv)
# window = QtWidgets.QWidget()
#
# # 设置窗口的大小
# window.resize(400, 400)
# window.setMinimumSize(300, 300)
# window.setMaximumSize(600, 600)
#
# # 设置初始位置
# window.move(100, 200)
# window.setWindowTitle('我是个牛逼的标题')
#
# window.show()
# sys.exit(app.exec_())
