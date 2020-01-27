from database import create_table_database, query_database
from entities.boxoffice import Boxoffice


def create_boxOffice_table():
    query = """CREATE TABLE IF NOT EXISTS boxOffice (
                        boxoffice_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        gross INTEGER,
                        movie_title TEXT
                        )"""
    create_table_database(query)


create_boxOffice_table()


def create_boxOffice(boxoffice):
    query = "INSERT INTO boxOffice VALUES (?,?,?)"
    params = (boxoffice.boxoffice_id, boxoffice.gross, boxoffice.movie_title)

    query_database(query, params)


boxoffice1 = Boxoffice(None, 50000000, "Filmas1")
create_boxOffice(boxoffice1)



# create_table_database("DROP TABLE boxOffice")

query_database("PRAGMA table_info(boxOffice)")