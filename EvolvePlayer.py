"""Main application starts from here
"""
from PySide import QtGui
from ui import MainController
from core.CommandParams import CommandParams
import images
import os
from ui import *

class EvolvePlayer(QtGui.QWidget):
    """Class to define the player
    """
    def __init__(self):
        """Initialing the application

        """
        super(EvolvePlayer, self).__init__()

        mainLayout = QtGui.QGridLayout()
        imgPath = images.getImgPath()
        logoIcon = QtGui.QPixmap(os.path.join(imgPath, "logoIcon.png"))
        controller = MainController.MainController(imgPath, self)
        mainLayout.addWidget(controller)
        self.setLayout(mainLayout)

        self.setWindowIcon(logoIcon)
        self.setStyleSheet("background:{0}".format(getBasicColors()[1]))

        self.addMenuBar()

    def addMenuBar(self):
        """Adding the menu bar to the application
        """
        mainMenu = QtGui.QMenuBar(self)
        fileMenu = mainMenu.addMenu("&File")

        addFiles = QtGui.QAction("&Open", self)
        addFiles.setShortcut("Ctrl+O")
        addFiles.setStatusTip("Add files to the playlist")
        removeFiles = QtGui.QAction("&RemoveFiles", self)
        removeFiles.setShortcut("Ctrl+R")
        removeFiles.setStatusTip("Remove files from the playlist")
        quitApp = QtGui.QAction("&Quit", self)
        quitApp.setShortcut("Ctrl+Q")
        quitApp.setStatusTip("Quit the application")
        quitApp.triggered.connect(self.close)

        # statusBar = QtGui.QStatusBar(self)
        # statusBar.setVisible(True)

        fileMenu.addAction(addFiles)
        fileMenu.addAction(removeFiles)
        fileMenu.addSeparator()
        fileMenu.addAction(quitApp)


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    gui = EvolvePlayer()
    gui.show()
    sys.exit(app.exec_())
