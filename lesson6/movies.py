class Movie:
    def __init__(self, name, duration, release_date, rating):
        self.name = name
        self.duration = duration
        self.release_date = release_date  #assuming only we have a year
        self.rating = rating

    def show_info(self):
        print(f"Movie name is {self.name}, its duration = {self.duration}, release_date = {self.release_date}; rating = {self.rating} ")

my_movie = Movie("The Shawshank Redemption", "1h30m", 1994, "9.5")

movie_list = [
    Movie("The Shawshank Redemption", "1h30m", 1994, "9.5"),
    Movie("The Godfather", "1h30m", 1972, "9.7"),
    Movie("The Dark Knight", "1h30m", 2008, "9.0"),
    Movie("The Godfather Part II", "1h30m", 1974, "9.0"),
    Movie("12 Angry Men", "1h30m", 1957, "9.0"),
    Movie("Schindler's List", "1h30m", 1993, "8.9")
]

class Critic:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def get_best_movie(cls, movies):
        if not movies:
            return None

        best_movie = movies[0]
        for movie in movies:
            if movie.rating > best_movie.rating:
                best_movie = movie

        return best_movie

critic = Critic("Nusrat", 32)
best_movie = critic.get_best_movie(movie_list)

best_movie.show_info()
