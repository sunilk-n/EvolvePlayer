from PySide.QtGui import *
from PySide.QtCore import *
import math
import os
from images import *
from ui import *


class RoundProgress(QProgressBar):

    def __init__(self, parent):
        QProgressBar.__init__(self)
        self.values = self.value()
        self.values = (self.values*360)/100
        self.parent = parent
        self.setParent(parent)
        self.n = self.value()
        self.label = QLabel()
        # self.label.setStyleSheet("color:#2166a8;")
        # self.label.setFont(QFont("courrier", math.sqrt(self.width())))
        self.v = QVBoxLayout(self)
        self.setLayout(self.v)
        self.v.addWidget(self.label)

    def setSongImg(self, imgPath, songImg):
        imagePather = os.path.join(imgPath, songImg).replace('\\','/')
        imgSong = QPixmap(imagePather)
        maskImg = QPixmap(os.path.join(getImgPath(), "mask.png"))
        imgSong.scaled(160, 160, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        maskImg.scaled(160, 160, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(imgSong)
        self.label.setScaledContents(True)
        self.label.resize(160, 160)
        self.label.setMask(maskImg)
        self.label.setStyleSheet('border-radius:75px;')

    def setValue(self, n):
        self.n = n
        self.values = ((n*5650)/100)*(-1)
        # self.label.setText("<center>"+str(self.n)+"</center>")

    def setNvalue(self, n):
        self.n = n
        self.values = ((n*5650)/100)*(-1)
        # self.label.setText("<center>"+str(self.n)+"</center>")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor("darkblue"))
        painter.setPen(pen)
        pen = QPen()
        pen.setWidth(10)
        pen.setColor(QColor("lightgrey"))
        painter.setPen(pen)
        painter.drawArc(5.1, 5.1, self.width()-10, self.height()-10, 1450, -5650)
        #painter.drawEllipse(0,0,100,100)
        painter.setBrush(QColor("lightblue"))
        pen = QPen()
        pen.setWidth(11)
        pen.setColor(QColor("{0}".format(getBasicColors()[0])))
        painter.setPen(pen)
        painter.drawArc(5.1, 5.1, self.width()-10, self.height()-10, 1450, self.values)
        self.update()


class Widget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.timer = QTimer()
        self.a = 0
        # self.playBtn = playBtn
        # self.pauseBtn = pauseBtn
        # self.timer.timeout.connect(self.to)
        # self.timer.start(songTime/10)
        self.setMaximumSize(170, 170)
        self.setMinimumSize(170, 170)
        # self.setGeometry(500, 100, 200, 200)
        self.roundProgress = RoundProgress(self)
        self.roundProgress.setGeometry(0, 0, 170, 170)
        self.roundProgress.setValue(0)
        # layout = QVBoxLayout(self)
        # layout.addWidget(self.pr2)
        # self.setLayout(layout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    gui = Widget()
    gui.show()
    sys.exit(app.exec_())
