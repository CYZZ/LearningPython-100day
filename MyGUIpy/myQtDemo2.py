import sys
from PyQt5.QtWidgets import QApplication, QWidget


# 集成自QWidget
class GUi(QWidget):
    def __init__(self):
        # 实例化super类，用来创建窗口
        super.__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('我是集成的标题')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUi()
    gui.show()
    sys.exit(app.exec_())
