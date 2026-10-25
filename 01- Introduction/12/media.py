from pytube import YouTube


class Media:
    def __init__(self, type, name, director, imdb_score, url, duration, casts):
        self.type = type
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.casts = casts

    def download(self):
        try:
            yt = YouTube(self.url)
            yt.title
            stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
            stream.download()
            print("Download complete!")
        except Exception as e:
            print(f"Error downloading video: {e}")
