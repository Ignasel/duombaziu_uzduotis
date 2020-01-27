from database import create_table_database, query_database
from entities.movie import Movies


def create_movies_table():
    query = """CREATE TABLE IF NOT EXISTS movies (
                        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        movie_title TEXT,
                        release_date INT,
                        rating FLOAT,
                        FOREIGN KEY(movie_title) REFERENCES boxOffice(movie_title)
                        )"""
    create_table_database(query)


# create_movies_table()


def create_movie(Movie):
    query = "INSERT INTO movies VALUES (?,?,?,?)"
    params = (Movie.movie_id, Movie.movie_title, Movie.release_date, Movie.rating)

    query_database(query, params)


movie1 = Movies(None,"Filmas1", 2020, 8.5)
# create_movie(movie1)


def get_movies_table():
    query = """SELECT * FROM movies
               INNER JOIN boxOffice on movies.movie_title = boxOffice.movie_title"""
    query_database(query)


get_movies_table()
# create_table_database("DROP TABLE movies")