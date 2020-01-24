from database import create_table_database
from entities.movie import Movies


def create_movies_table():
    query = """CREATE TABLE IF NOT EXISTS movies (
                        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        movie_title TEXT,
                        realese_date INT,
                        rating FLOAT
                        )"""
    create_table_database(query)


create_movies_table()

def create_movie():
    query = "INSERT INTO movies VALUES (?,?,?,?)"
    params = (Movies.movie_id, Movies.movie_title, Movies.release_date, Movies.rating)

    create_table_database(query, params)


movie1 = Movies("","Knyga1", 2020, 8.5)
create_movie()


def get_movies_table():
    query = """SELECT * FROM movies"""
    create_table_database(query)

get_movies_table(movie1)