from database import create_table_database, query_database
from entities.director import Directors


def create_directors_table():
    query = """CREATE TABLE IF NOT EXISTS directors (
                        director_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        director_name TEXT,
                        movie_title TEXT
                        )"""
    create_table_database(query)


create_directors_table()


def create_director(director):
    query = "INSERT INTO directors VALUES (?,?,?)"
    params = (director.director_id, director.director_name, director.movie_title)

    query_database(query, params)


director1 = Directors(None, "Chistopher Nolan", "Filmas1")
create_director(director1)