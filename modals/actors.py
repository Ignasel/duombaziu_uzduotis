from database import create_table_database, query_database
from entities.actor import Actors


def create_actors_table():
    query = """CREATE TABLE IF NOT EXISTS actors (
                        actors_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        actors_name TEXT)"""
    create_table_database(query)


create_actors_table()


def create_actor(Actor):
    query = "INSERT INTO movies VALUES (?,?)"
    params = (Actor.actor_id, Actor.actor_name)

    query_database(query, params)


Actor1 = Actors(None,"Brad Pit")
create_actor(Actor1)