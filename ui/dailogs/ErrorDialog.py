from PySide import QtGui, QtCore

class ErrorDialog(QtGui.QWidget):
    def __init__(self, message="", title="", parent=None):
        super(ErrorDialog, self).__init__()

        self.setParent(parent)
        self._message = message
        self._title = title
        self.setFixedSize(500, 150)

        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.msgDisp = QtGui.QLabel(self)
        self.msgDisp.setWordWrap(True)
        # self.msgDisp.setAlignment(QtCore.Qt.AlignCenter)
        okBtn = QtGui.QPushButton(self)
        okBtn.setText("OK")
        okBtn.clicked.connect(self.close)

        horSpacer1 = QtGui.QSpacerItem(1, 2, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        horSpacer2 = QtGui.QSpacerItem(1, 2, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)

        layout = QtGui.QGridLayout()
        layout.addWidget(self.msgDisp, 0, 0, 1, 2)
        layout.addWidget(okBtn, 1, 1, 1, 1)
        layout.addItem(horSpacer1, 1, 0, 1, 1)
        layout.addItem(horSpacer2, 1, 2, 1, 1)
        # layout.setMargin(15)
        self.setLayout(layout)

        self.displayWindow()

    def displayWindow(self):
        self.setWindowTitle(self._title)
        self.msgDisp.setText(self._title)

    def showErrorWindow(self):
        self.show()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    gui = ErrorDialog(message="Testing", title="Error occured here")
    gui.show()
    sys.exit(app.exec_())
