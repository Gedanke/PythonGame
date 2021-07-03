# -*- coding: utf-8 -*-


from MainWidget import MainWidget
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    """"""
    app = QApplication(sys.argv)
    mainWidget = MainWidget()
    mainWidget.show()
    app.exit(app.exec_())
