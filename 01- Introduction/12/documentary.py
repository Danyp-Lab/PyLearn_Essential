from media import Media


class Documentary(Media):
    def __init__(self, type, name, director, imdb_score, url, duration, casts, topic):
        super().__init__(type, name, director, imdb_score, url, duration, casts)
        self.topic = topic


###########Test Class###############
# instance
""" 
educational_clip = EducationalContent(type="Documentary", name="The Universe Revealed",
                                      director="Dr. Astronomer", imdb_score=9.2,
                                      url="https://example.com/universe-revealed",
                                      duration=60, casts=["Narrator", "Scientists"],
                                      topic="Cosmology")

"""
# Print the data in instance

"""
                                    
print(f"Clip Name: {educational_clip.name}")
print(f"Director: {educational_clip.director}")
print(f"IMDb Score: {educational_clip.imdb_score}")
print(f"Duration: {educational_clip.duration} minutes")
print(f"Topic: {educational_clip.topic}")

"""
