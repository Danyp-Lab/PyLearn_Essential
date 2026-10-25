from media import Media


class Clip(Media):
    def __init__(self, type, name, director, imdb_score, url, duration, casts, category):
        super().__init__(type, name, director, imdb_score, url, duration, casts)
        self.category = category


# TestClass:
""" 
clip1 = Clip(type="Movie", name="Inception", director="Christopher Nolan",
             imdb_score=8.8, url="https://www.imdb.com/title/tt0816692/",
             duration=148, casts=["Matthew McConaughey,Anne Hathaway,Jessica Chastain"],
             category="Science Fiction")
"""
# Print the details of the clip
"""
print(f"Clip Name: {clip1.name}")
print(f"Director: {clip1.director}")
print(f"IMDb Score: {clip1.imdb_score}")
print(f"Duration: {clip1.duration} minutes")
print(f"Category: {clip1.category}")


"""
