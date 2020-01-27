from database import create_table_database, query_database
from entities.genre import Genres


def create_genre_table():
    query = """CREATE TABLE IF NOT EXISTS genres (
                        genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name INTEGER,
                        )"""
    create_table_database(query)


create_genre_table()