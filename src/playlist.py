from song import Song
from date_parser import TimeParser
from functools import reduce
import random
from prettytable import PrettyTable
import json
from collections import OrderedDict


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs = []
        self.current_songs = []
        self.songs_played = -1

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

    def artists(self):
        art_hist = {}
        for song in self.songs:
            if song.artist not in art_hist:
                art_hist[song.artist] = 1
            else:
                art_hist[song.artist] += 1
        return art_hist

    def next_song(self):
        if self.shuffle:
            return self.__shuffle_help()
        if self.repeat:
            return self.__repeat_help()

    def __repeat_help(self):
        self.songs_played += 1
        if self.songs_played == len(self.songs):
            self.songs_played = 0
        return self.songs[self.songs_played]

    def __shuffle_help(self):
        idx = random.randrange(0, len(self.songs))
        if len(self.current_songs) == len(self.songs):
            self.current_songs = [self.songs[idx]]
            return self.songs[idx]
        while self.songs[idx] in self.current_songs:
            idx = random.randrange(0, len(self.songs))
        self.current_songs.append(self.songs[idx])
        return self.songs[idx]

    def pprint_playlist(self):
        table = PrettyTable(["Artist", "Song", "Length"])
        for song in self.songs:
            table.add_row([song.artist, song.title, song.length])
        return table

    def __dasherize(self):
        return self.name.replace(' ', '-')

    def save(self):
        json_string = OrderedDict([['name', self.name],
                                   ['repeat', self.repeat],
                                   ['shuffle', self.shuffle]])
        song_list = []
        for song in self.songs:
            song_list.append(OrderedDict([['title', song.title],
                                          ['artist', song.artist],
                                          ['album', song.album],
                                          ['length', str(song.length)]]))
        json_string['songs'] = song_list
        with open('playlist-data/{}.json'
                  .format(self.__dasherize()), 'w') as f:
            json.dump(json_string, f, indent=4)


def main():
    song1 = Song(title="Odin", artist="Manowar",
                 album="The Sons of Odin", length=TimeParser("3:44"))
    song2 = Song(title="Odina", artist="Nightwish",
                 album="The Sons of Odina", length=TimeParser("3:44"))
    song3 = Song(title="Nothing else matters", artist="Metallica",
                 album="The Black Album", length=TimeParser('2:45'))
    playlist = Playlist("my playlist", False, True)  # shuffle is True
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.add_song(song3)
    # print(playlist.next_song())
    # print(playlist.next_song())
    # print(playlist.next_song())
    # print(playlist.next_song())
    print(playlist.pprint_playlist())
    playlist.save()


if __name__ == '__main__':
    main()
