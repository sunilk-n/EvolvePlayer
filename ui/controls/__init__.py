import os
from PySide.QtCore import QTimer

def getControlsPath():
    return os.path.dirname(os.path.realpath(__file__))
