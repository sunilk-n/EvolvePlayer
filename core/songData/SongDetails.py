from mutagen.easyid3 import EasyID3
from mutagen import File
from mutagen.mp3 import MP3

from lib.data import *
from images import *

class SongDetails:
    '''Getting and setting the metadata
    for the song which was been selected'''
    def __init__(self, song):
        songDir = getSongDataPath()
        self.fullSongPath = os.path.join(songDir, song)
        self.songTags = EasyID3(self.fullSongPath)
        self.imageFile = File(self.fullSongPath)

    def songName(self):
        '''return the song name of selected'''
        try:
            return self.songTags['title'][0]
        except:
            return "No Information"

    def movieName(self):
        try:
            return self.songTags['album'][0]
        except:
            return "No Information"

    def singerName(self):
        try:
            return self.songTags['artist'][0]
        except:
            return "No Information"

    def composerName(self):
        try:
            return self.songTags['composer'][0]
        except:
            return "No Information"

    def yearRelease(self):
        try:
            return self.songTags['date'][0]
        except:
            return "No Information"

    def imageDisplay(self):
        try:
            img = self.imageFile.tags['APIC:'].data
            with open(os.path.join(getImgPath(), "front.jpg"), 'wb') as imger:
                imger.write(img)
            return os.path.join(getImgPath(), "front.jpg")
        except:
            return None

    def getSongLength(self):
        audio = MP3(self.fullSongPath)
        print audio.info.length
        return audio.info.length

    def setSongName(self, songName):

        self.songTags['title'] = songName
        self.saveSong()
        return True

    def setMovieName(self, movieName):

        self.songTags['album'] = movieName
        self.saveSong()
        return True

    def setSingerName(self, singerNames):
        self.songTags['artist'] = singerNames
        self.saveSong()
        return True

    def setYearRelease(self, year):
        self.songTags['date'] = year
        self.saveSong()
        return True

    def setComposerName(self, composerName):
        self.songTags['composer'] = composerName
        self.saveSong()
        return True

    def saveSong(self):
        self.songTags.save()

if __name__ == '__main__':
    #song = EasyID3(os.path.join(getSongDataPath(), "crazyFeeling.mp3"))
    songName = SongDetails("crazyFeeling.mp3")
    # songName.setComposerName("Devi Sri Prasad")
    print songName.getSongLength()
