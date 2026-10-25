from media import Media


class Film(Media):
    def __init__(self, type, name, director, imdb_score, url, duration, casts, genre):
        super().__init__(type, name, director, imdb_score, url, duration, casts)
        self.genre = genre
