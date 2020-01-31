from database import create_table_database, query_database
from entities.movie import Movies


def create_movies_table():
    query = """CREATE TABLE IF NOT EXISTS movies (
                        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        movie_title TEXT,
                        release_date INT,
                        rating FLOAT,
                        boxoffice_id INT,
                        directors_id INT,
                        studios_id INT,
                        FOREIGN KEY(boxoffice_id) REFERENCES boxOffice(boxoffice_id),
                        FOREIGN KEY(directors_id) REFERENCES directors(director_id),
                        FOREIGN KEY(studios_id) REFERENCES studios(studio_id),
                        FOREIGN KEY(movie_id) REFERENCES genres_movies(movie_id),
                        FOREIGN KEY(movie_id) REFERENCES actors_movies(movie_id)
                        )"""
    create_table_database(query)


# create_movies_table()


def create_movie(Movie):
    query = "INSERT INTO movies VALUES (?,?,?,?,?,?,?)"
    params = (Movie.movie_id, Movie.movie_title, Movie.release_date, Movie.rating, Movie.boxoffice_id, Movie.director_id,
              Movie.studio_id)

    query_database(query, params)


movie1 = Movies(None,"Filmas1", 2020, 8.5, 1, 1, 1)
create_movie(movie1)


def get_movies_table():
    query = """SELECT * FROM movies
               INNER JOIN boxOffice on movies.boxoffice_id = boxOffice.boxoffice_id"""
    query_database(query)


# get_movies_table()
create_table_database("DROP TABLE movies")