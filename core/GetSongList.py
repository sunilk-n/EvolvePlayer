from lib.data import *
import os as _os

class GetSongList:
    def __init__(self):

        self.songPath = getSongDataPath()

    def updateSongs(self):

        songList = [x for x in _os.listdir(self.songPath) if x.endswith(".mp3")]
        return songList

if __name__ == '__main__':

    songs = GetSongList()
    print songs.updateSongs()
