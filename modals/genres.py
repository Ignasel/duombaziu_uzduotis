from database import create_table_database, query_database
from entities.genre import Genres


def create_genre_table():
    query = """CREATE TABLE IF NOT EXISTS genres (
                        genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        genre_name TEXT
                        )"""
    create_table_database(query)


def create_genres_movies_table():
    query = """CREATE TABLE IF NOT EXISTS genres_movies (
                        genres_movies_Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        genre_id int,
                        movie_id int,
                        FOREIGN KEY (genre_id) REFERENCES genres(genre_id),                 
                        FOREIGN KEY (movie_id) REFERENCES movies(movie_id))"""
    create_table_database(query)


def insert_genres_movies(genre_name, movie_title):
    query = """INSERT INTO genres_movies (genre_id, movie_id)
                                        SELECT(SELECT genre_id FROM genres WHERE genre_name=?), 
                                        (SELECT movie_id FROM movies WHERE movie_title=?)"""
    params = (genre_name, movie_title)
    query_database(query, params)


def create_genre(genre):
    query = "INSERT INTO genres VALUES (?,?)"
    params = (genre.genre_id, genre.genre_name)

    query_database(query, params)


def get_genres_movies_table():
    query = "SELECT * FROM genres_movies"
    query_database(query)


create_genre_table()
create_genres_movies_table()
genre1 = Genres(None,"Siaubo")
create_genre(genre1)
insert_genres_movies("Siaubo", "Filmas1")
create_genres_movies_table()
get_genres_movies_table()
# create_table_database("DROP TABLE actors_movies")
# create_table_database("DROP TABLE genres_movies")
# create_table_database("DROP TABLE genres")
# create_table_database("DROP TABLE actors")




create_genre_table()