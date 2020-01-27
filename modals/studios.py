from database import create_table_database, query_database
from entities.studios import Studios


def create_studio_table():
    query = """CREATE TABLE IF NOT EXISTS studios (
                        studio_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        studio_name TEXT,
                        movie_title TEXT
                        )"""
    create_table_database(query)


create_studio_table()


def create_studio(studio):
    query = "INSERT INTO studios VALUES (?,?,?)"
    params = (studio.studio_id, studio.studio_name, studio.movie_title)

    query_database(query, params)


studio1 = Studios(None, "Warner Bros", "Filmas1")


create_studio(studio1)