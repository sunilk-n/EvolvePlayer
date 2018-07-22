from PySide import QtGui
from PIL import _imaging
from ui.controls import MainController
from core.CommandParams import CommandParams
import images
import os

class EvolvePlayer(QtGui.QWidget):
    def __init__(self):
        super(EvolvePlayer, self).__init__()

        mainLayout = QtGui.QGridLayout()
        imgPath = images.getImgPath()
        logoIcon = QtGui.QPixmap(os.path.join(imgPath, "logoIcon.png"))
        controller = MainController.MainController(imgPath, self)
        mainLayout.addWidget(controller)
        self.setLayout(mainLayout)

        self.setWindowIcon(logoIcon)
        self.setStyleSheet("background:#444243")


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    gui = EvolvePlayer()
    gui.show()
    sys.exit(app.exec_())
