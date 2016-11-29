class Song:

    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return "{} - {} from {} - {}". \
            format(self.artist, self.title, self.album, self.length)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.title == other.title and \
            self.artist == other.artist and \
            self.album == other.album and \
            self.length == other.length

    def __hash__(self):
        return hash(self.title) + hash(self.artist) \
            + hash(self.album) + hash(self.length)

    def length(self, seconds=False, minutes=False, hours=False):
        if seconds:
            return self.length.get_seconds()
        elif minutes:
            return self.length.get_minutes()
        elif hours:
            return self.length.get_hours()
        else:
            return self.length

    def __add__(self, other):
        return self.length + other.length
