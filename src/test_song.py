import unittest
from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song(title="Odin", artist="Manowar",
                         album="The Sons of Odin", length="3:44")

    def test_hash(self):
        self.song2 = Song(title="Odin", artist="Manowar",
                          album="The Sons of Odin", length="3:44")
        self.song3 = Song(title="Odin", artist="Manowar",
                          album="The Sons of Odina", length="3:44")
        self.assertEqual(hash(self.song), hash(self.song2))
        self.assertNotEqual(hash(self.song), hash(self.song3))


if __name__ == '__main__':
    unittest.main()
