import unittest
from playlist import Playlist, Song, TimeParser


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist("my_playlist")

    def test_add_song(self):
        song1 = Song(title="Odin", artist="Manowar",
                     album="The Sons of Odin", length=TimeParser("3:44"))
        song2 = Song(title="Odin", artist="Manowar",
                     album="The Sons of Odina", length=TimeParser("3:44"))
        self.playlist.add_song(song1)
        self.playlist.add_song(song2)
        self.assertEqual(self.playlist.songs, [song1, song2])
        self.assertRaises(TypeError, self.playlist.add_song(1))

    def test_remove_song(self):
        song1 = Song(title="Odin", artist="Manowar",
                     album="The Sons of Odin", length=TimeParser("3:44"))
        song2 = Song(title="Odin", artist="Manowar",
                     album="The Sons of Odina", length=TimeParser("3:44"))
        self.playlist.add_song(song1)
        self.playlist.add_song(song2)
        self.playlist.remove_song(song2)
        self.assertEqual(self.playlist.songs, [song1])

    def test_add_songs(self):
        song1 = Song(title="Odin", artist="Manowar",
                     album="The Sons of Odin", length=TimeParser("3:44"))
        song2 = Song(title="Odin", artist="Manowar",
                     album="The Sons of Odina", length=TimeParser("3:44"))
        songs = [song1, song2]
        self.playlist.add_songs(songs)
        self.assertEqual(self.playlist.songs, [song1, song2])
        self.assertRaises(TypeError, self.playlist.add_songs([song1, 1]))

    def test_length(self):
        song1 = Song(title="Odin", artist="Manowar",
                     album="The Sons of Odin", length=TimeParser("3:44"))
        song2 = Song(title="Odin", artist="Manowar",
                     album="The Sons of Odina", length=TimeParser("3:44"))
        self.playlist.add_song(song1)
        self.playlist.add_song(song2)
        self.assertEqual(self.playlist.total_length(), song1 + song2)

    def test_artists(self):
        song1 = Song(title="Odin", artist="Manowar",
                     album="The Sons of Odin", length=TimeParser("3:44"))
        song2 = Song(title="Odin", artist="Nightwish",
                     album="The Sons of Odina", length=TimeParser("3:44"))
        self.playlist.add_song(song1)
        self.playlist.add_song(song2)
        self.assertEqual(self.playlist.artists(),
                         {'Manowar': 1, 'Nightwish': 1})


if __name__ == '__main__':
    unittest.main()
