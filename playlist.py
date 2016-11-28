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
        self.songs.append(song)
        return self.songs

    def remove_song(self, song):
        self.songs.remove(song)
        return self.songs

    def add_songs(self, songs):
        # change self.songs
        self.songs[:] = map(lambda x: self.songs.append(x), songs)
        return self.songs

    def total_length(self):
        return reduce(lambda x, y: x + y, self.songs)
