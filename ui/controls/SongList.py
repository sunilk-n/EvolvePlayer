from PySide import QtGui, QtCore, QtUiTools
import os
import re

from ui.controls import *
from ui import *
from core.GetSongList import GetSongList
from core.songData.SongDetails import SongDetails

class SongList(QtGui.QWidget):
    def __init__(self, parent=None):
        super(SongList, self).__init__(parent)
        self.setParent(parent)
        colors = getBasicColors()

        stylerTable = """#songLister
            {
                alternate-background-color:#333;
                background:"""+colors[1]+""";
                border:0;
                color:"""+colors[2]+""";
                font-size:18px;
            }
            #songLister::item:selected{
                background:transparent;
                color:"""+colors[0]+""";
            }
            #songLister::item:hover{
                background:transparent;
                color:"""+colors[0]+""";
            }
            #searchBox{
                height:30px;
                border:0;
                border-radius:5px;
                font-size:18px;
                background-color:"""+colors[2]+""";
            }
            #searchText{
                font-size:18px;
                color:#FFF;
            }"""

        self.setMinimumWidth(600)
        self.setStyleSheet(stylerTable)

        loader = QtUiTools.QUiLoader()
        _file = QtCore.QFile(os.path.join(getControlsPath(), "songTable.ui"))
        _file.open(QtCore.QFile.ReadOnly)
        self.songs = loader.load(_file, self)
        _file.close()

        songGenerate = GetSongList()
        self.allSongs = songGenerate.updateSongs()
        self.searchBox = self.songs.searchBox
        self.searchBox.textChanged.connect(self.addSongs)

        self.songTable = self.songs.songLister
        self.songTable.setAlternatingRowColors(True)
        self.songTable.horizontalHeader().setVisible(False)
        self.songTable.verticalHeader().setVisible(False)

        self.setLayout(self.songs.gridLayout)

        self.songModal = QtGui.QStandardItemModel(2, 2)
        self.addSongs()

    def addSongs(self, searchHint = ""):

        self.songTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.songTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.songTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        if searchHint == "":
            self.songModal.clear()

            self.songModal.setHorizontalHeaderItem(0, QtGui.QStandardItem("Song"))
            self.songModal.setHorizontalHeaderItem(1, QtGui.QStandardItem("Movie"))
            # self.songModal.setHorizontalHeaderItem(2, QtGui.QStandardItem("Music Director"))

            index = 0
            for song in self.allSongs:
                songInfo = SongDetails(song)
                items = []
                items.append(QtGui.QStandardItem(".".join(song.split('.')[:-1])))
                items.append(QtGui.QStandardItem(songInfo.movieName()))
                items.append(QtGui.QStandardItem(songInfo.singerName()))
                self.songModal.setItem(index, 0, items[0])
                self.songModal.setItem(index, 1, items[1])
                # self.songModal.setItem(index, 2, items[2])
                index += 1

        else:
            self.songModal.clear()

            self.songModal.setHorizontalHeaderItem(0, QtGui.QStandardItem("Song"))
            self.songModal.setHorizontalHeaderItem(1, QtGui.QStandardItem("Movie"))
            # self.songModal.setHorizontalHeaderItem(2, QtGui.QStandardItem("Music Director"))

            index = 0
            for song in self.allSongs:
                songInfo = SongDetails(song)
                items = []
                if re.search(searchHint, ".".join(song.split('.')[:-1]), re.I) or re.search(searchHint, songInfo.movieName(), re.I) or re.search(searchHint, songInfo.singerName(), re.I):
                    items.append(QtGui.QStandardItem(".".join(song.split('.')[:-1])))
                    items.append(QtGui.QStandardItem(songInfo.movieName()))
                    # items.append(QtGui.QStandardItem(songInfo.singerName()))
                    self.songModal.setItem(index, 0, items[0])
                    self.songModal.setItem(index, 1, items[1])
                    # self.songModal.setItem(index, 2, items[2])
                    index += 1

        self.songTable.setModel(self.songModal)

        header = self.songTable.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(1, QtGui.QHeaderView.Stretch)
        # header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    gui = SongList()
    gui.show()
    sys.exit(app.exec_())