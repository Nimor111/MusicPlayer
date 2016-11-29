from song import Song
from date_parser import TimeParser
from functools import reduce


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs = []

    def add_song(self, song):
        try:
            self.songs.append(song)
        except TypeError as e:
            print(e)
        finally:
            return self.songs

    def remove_song(self, song):
        try:
            self.songs.remove(song)
        except TypeError as e:
            print(e)
        finally:
            return self.songs

    def add_songs(self, songs):
        try:
            for song in songs:
                self.songs.append(song)
        except TypeError as e:
            print(e)
        finally:
            return self.songs

    def total_length(self):
        return reduce(lambda x, y: x + y, self.songs)
