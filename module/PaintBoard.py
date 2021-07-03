# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import QPixmap, QPainter, QPoint, QPen, QColor, QSize
from PyQt5.QtCore import Qt


class PaintBoard(QWidget):
    def __init__(self, Parent=None):
        """

        :param Parent:
        """
        super().__init__(Parent)
        self.__InitData()
        self.__InitView()

    def __InitData(self):
        """

        :return:
        """
        self.__size = QSize(480, 460)
        self.__board = QPixmap(self.__size)
        self.__board.fill(Qt.white)
        self.__IsEmpty = True
        self.EraserMode = False
        self.__lastPos = QPoint(0, 0)
        self.__currentPos = QPoint(0, 0)
        self.__painter = QPainter()
        self.__thickness = 10
        self.__penColor = QColor("black")
        self.__colorList = QColor.colorNames()

    def __InitView(self):
        """

        :return:
        """
        self.setFixedSize(self.__size)

    def Clear(self):
        """

        :return:
        """
        self.__board.fill(Qt.white)
        self.update()
        self.__IsEmpty = True

    def ChangePenColor(self, color="black"):
        """
        改变画笔颜色
        :param color:
        :return:
        """
        self.__penColor = QColor(color)

    def ChangePenThickness(self, thickness=10):
        """

        :param thickness:
        :return:
        """
        self.__thickness = thickness

    def IsEmpty(self):
        """

        :return:
        """
        return self.__IsEmpty

    def GetContentAsQImage(self):
        """

        :return:
        """
        image = self.__board.toImage()
        return image

    def paintEvent(self, paintEvent):
        """

        :param paintEvent:
        :return:
        """
        self.__painter.begin(self)
        self.__painter.drawPixmap(0, 0, self.__board)
        self.__painter.end()

    def mousePressEvent(self, mouseEvent):
        """

        :param mouseEvent:
        :return:
        """
        self.__currentPos = mouseEvent.pos()
        self.__lastPos = self.__currentPos

    def mouseMoveEvent(self, mouseEvent):
        """

        :param mouseEvent:
        :return:
        """
        self.__currentPos = mouseEvent.pos()
        self.__painter.begin(self.__board)

        if self.EraserMode == False:
            self.__painter.setPen(QPen(self.__penColor, self.__thickness))  # 设置画笔颜色，粗细
        else:
            self.__painter.setPen(QPen(Qt.white, 10))

        self.__painter.drawLine(self.__lastPos, self.__currentPos)
        self.__painter.end()
        self.__lastPos = self.__currentPos

        self.update()

    def mouseReleaseEvent(self, mouseEvent):
        """

        :param mouseEvent:
        :return:
        """
        self.__IsEmpty = False
