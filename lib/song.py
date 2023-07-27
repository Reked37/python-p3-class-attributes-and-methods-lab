class Song:
    count=0
    genres=[]
    artists=[]
    genre_count={}
    artist_count={}

    @classmethod
    def add_song_to_count(cls):
      Song.count+=1

    @classmethod
    def add_to_genres(cls, genre):
        Song.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        Song.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        Song.genre_count[genre]= Song.genres.count(genre)

    @classmethod
    def add_to_artist_count(cls, artist):
        Song.artist_count[artist]=Song.artists.count(artist)

    def __init__(self, name, artist, genre):
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        self.name=name
        self.artist=artist
        self.genre=genre


   

