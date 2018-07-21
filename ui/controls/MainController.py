from PySide import QtGui, QtUiTools, QtCore
from ui.controls import *
from images import *

class MainController(QtGui.QWidget):
    def __init__(self, imgPath, parent=None):
        super(MainController, self).__init__(parent)
        self.setParent(parent)

        self.setMaximumSize(600, 200)
        self.setMinimumSize(0, 200)

        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile(os.path.join(getControlsPath(),"controlUi.ui"))
        file.open(QtCore.QFile.ReadOnly)
        myWidget = loader.load(file, self)
        file.close()

        playImg = QtGui.QPixmap(os.path.join(imgPath, "play.png"))
        stopImg = QtGui.QPixmap(os.path.join(imgPath, "stop.png"))
        prevImg = QtGui.QPixmap(os.path.join(imgPath, "previous.png"))
        nextImg = QtGui.QPixmap(os.path.join(imgPath, "next.png"))
        repImg = QtGui.QPixmap(os.path.join(imgPath, "previous.png"))

        myWidget.playBtn.setIcon(playImg)
        myWidget.stopBtn.setIcon(stopImg)
        myWidget.nextBtn.setIcon(nextImg)
        myWidget.prevBtn.setIcon(prevImg)
        myWidget.repeatBtn.setIcon(repImg)

        outerLayout = QtGui.QGridLayout()
        outerLayout.addWidget(myWidget, 0, 0, 1, 1)
        self.setLayout(outerLayout)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    gui = MainController(getImgPath())
    gui.show()
    sys.exit(app.exec_())
