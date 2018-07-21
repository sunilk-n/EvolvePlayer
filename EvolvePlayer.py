from PySide import QtGui
from ui.controls import MainController
import images

class EvolvePlayer(QtGui.QWidget):
    def __init__(self):
        super(EvolvePlayer, self).__init__()

        mainLayout = QtGui.QGridLayout()
        imgPath = images.getImgPath()
        print imgPath
        mainLayout.addWidget(MainController.MainController(imgPath, self))
        self.setLayout(mainLayout)

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    gui = EvolvePlayer()
    gui.show()
    sys.exit(app.exec_())