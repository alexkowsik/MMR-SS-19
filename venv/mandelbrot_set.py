import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc
import numpy as np
import matplotlib.pyplot as plt

class MandelbrotMenge():

    def __init__(self):
        self.width = 600
        self.height = 400

        self.display = qw.QLabel()
        self.display.setGeometry(400, 150, self.width, self.height)
        self.display.mousePressEvent = self.MousePressEvent

        self.colormap = plt.cm.jet

        self.interval1 = [-2, 1]
        self.interval2 = [1, -1]
        self.zoom = 1

        self.X = None
        self.Y = None
        self.NUMS = None
        self.count = None

        self.mandelbrot(self.interval1, self.interval2)



    def mandelbrot(self, interval1, interval2):
        self.X = np.linspace(interval1[0], interval1[1], self.width).reshape((1, self.width))
        self.Y = np.linspace(interval2[0], interval2[1], self.height).reshape((self.height, 1))
        self.NUMS = np.tile(self.X, (self.height, 1)) + 1j * np.tile(self.Y, (1, self.width))

        self.count = np.zeros([self.height, self.width], dtype=np.uint8)

        for i in range(self.height):
            for j in range(self.width):
                self.count[i, j] =  self.seqenceCounter(self.NUMS[i, j])

        self.draw(self.count)


    def seqenceCounter(self, c):
        n = 100
        z = 0
        for i in range(n):
            z = z**2 + c
            if z > 2:
                return i
        return n


    def draw(self, count):
        max = np.max(count)
        min = np.min(count)
        if max == 0:
            max = 1
        count = (count - min) / max
        colfloat = self.colormap(count)
        colint = np.asarray(colfloat * 255, dtype=np.uint8)

        img = qg.QImage(colint.data, self.width, self.height, qg.QImage.Format_RGBA8888)

        self.display.setPixmap(qg.QPixmap.fromImage(img))
        self.display.show()


    def MousePressEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        y = QMouseEvent.y()

        newW = (abs(self.interval1[0]) + abs(self.interval1[1])) / 4
        newH = (abs(self.interval2[0]) + abs(self.interval2[1])) / 4

        print(newW, newH, x, y, self.X[0][x], self.Y[y][0])

        self.interval1 = [self.X[0][x] - newW, self.X[0][x] + newW]
        self.interval2 = [self.Y[y][0] + newH, self.Y[y][0] - newH]

        print(self.interval1, self.interval2)

        self.mandelbrot(self.interval1, self.interval2)



if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    MandelbrotMenge()
    app.exec_()
