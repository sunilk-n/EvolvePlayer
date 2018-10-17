
from PySide import QtCore
from time import sleep

class SongThread(QtCore.QThread):
    runTime = QtCore.Signal(int)
    def __init__(self, timer=0, totalSecs=240):
        super(SongThread, self).__init__()
        self.timerPerCent = totalSecs / 100
        print self.timerPerCent
        if timer == -1:
            self.currentTime = 0
        else:
            self.currentTime = timer*(100/totalSecs)
        self.totalSecs = 100
        self.eachSec = float(self.totalSecs)/totalSecs

        self.pauseTimer = True
        self.interPret = True

    def pauseTimeline(self):
        self.pauseTimer = True

    def dePauseTimeline(self):
        self.pauseTimer = False


    def interPretSong(self):
        self.interPret = False

    def run(self):
        while True:
            if self.currentTime >= self.totalSecs or not self.interPret:
                self.currentTime = 0
                break
            if not self.pauseTimer:
                self.currentTime = self.currentTime + self.eachSec
                sleep(1)

            print self.currentTime
            self.runTime.emit(self.currentTime)
