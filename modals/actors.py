from database import create_table_database


def create_actors_table():
    query = """CREATE TABLE IF NOT EXISTS actors (
                        actors_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        actors_name TEXT)"""
    create_table_database(query)


create_actors_table()
