from lib.data import *
import os as _os

class GetSongList:
    def __init__(self):

        self.songPath = getSongDataPath()

    def updateSongs(self):

        songList = [x for x in _os.listdir(self.songPath) if x.endswith(".mp3")]
        return songList

    def getSelectedSong(self, songName):
        allSongs = self.updateSongs()
        if songName in allSongs:
            return _os.path.join(self.songPath, songName)
        else:
            return None

if __name__ == '__main__':

    songs = GetSongList()
    a = songs.updateSongs()
    # print songs.getSelectedSong("crazyFeeling")

