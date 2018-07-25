from PySide import QtGui, QtUiTools, QtCore
from ui.controls import *
from images import *
from core.CommandParams import CommandParams
from ProgressBar import Widget
from ui import *

class MainController(QtGui.QWidget):
    def __init__(self, imgPath, parent=None):
        super(MainController, self).__init__(parent)
        self.setParent(parent)

        self.playFlag = True

        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile(os.path.join(getControlsPath(),"controlUi.ui"))
        file.open(QtCore.QFile.ReadOnly)
        self.musicCtrl = loader.load(file, self)
        file.close()
        ctrlWidth = self.musicCtrl.frameGeometry().width()
        ctrlHeight = self.musicCtrl.frameGeometry().height()+170
        maxCtrlSize = QtCore.QSize(ctrlWidth, ctrlHeight)
        self.setMaximumSize(maxCtrlSize)
        # self.setMinimumSize(minCtrlSize)

        playImg = QtGui.QPixmap(os.path.join(imgPath, "play.png"))
        self.pauseImg = QtGui.QPixmap(os.path.join(imgPath, "pause.png"))
        stopImg = QtGui.QPixmap(os.path.join(imgPath, "stop.png"))
        prevImg = QtGui.QPixmap(os.path.join(imgPath, "previous.png"))
        nextImg = QtGui.QPixmap(os.path.join(imgPath, "next.png"))
        repImg = QtGui.QPixmap(os.path.join(imgPath, "repeat.png"))

        self.musicCtrl.playBtn.setIcon(playImg)
        self.musicCtrl.stopBtn.setIcon(stopImg)
        self.musicCtrl.nextBtn.setIcon(repImg)
        self.musicCtrl.prevBtn.setIcon(prevImg)
        self.musicCtrl.repeatBtn.setIcon(nextImg)

        self.progressBar = Widget()
        self.progressBar.pr2.setSongImg(imgPath, "front.jpg")

        outerLayout = QtGui.QGridLayout()
        outerLayout.addWidget(self.progressBar, 0, 1, 1, 1)
        outerLayout.addWidget(self.musicCtrl, 1, 0, 1, 3)
        self.setLayout(outerLayout)
        self.musicCtrl.playBtn.setShortcut("Space")
        self.musicCtrl.nextBtn.setShortcut("N")
        self.musicCtrl.prevBtn.setShortcut("B")

        self.createPauseBtn()


        self.musicCtrl.playBtn.clicked.connect(self.pauseSong)
        self.pauseBtn.clicked.connect(self.playSong)

    def createPauseBtn(self):
        self.pauseBtn = QtGui.QPushButton(self.musicCtrl)
        self.pauseBtn.setObjectName("pausebtn")
        self.pauseBtn.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.pauseBtn.setMaximumSize(100, 100)
        self.pauseBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pauseBtn.setStyleSheet("max-height:100px;max-width:100px;border-radius:49px;")
        self.pauseBtn.setIcon(self.pauseImg)
        self.pauseBtn.setIconSize(QtCore.QSize(100, 100))

        self.musicCtrl.gridLayout.addWidget(self.pauseBtn, 0, 2, 2, 1)
        self.pauseBtn.setVisible(False)
        self.pauseBtn.setShortcut("Space")

    def pauseSong(self, *args):
        self.pauseBtn.setVisible(True)
        self.musicCtrl.playBtn.setVisible(False)

    def playSong(self, *args):
        self.musicCtrl.playBtn.setVisible(True)
        self.pauseBtn.setVisible(False)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    gui = MainController(getImgPath())
    gui.show()
    sys.exit(app.exec_())
