from database import create_table_database, query_database
from entities.actor import Actors


def create_actors_table():
    query = """CREATE TABLE IF NOT EXISTS actors (
                        actors_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        actor_name TEXT)"""
    create_table_database(query)


create_actors_table()


def create_actors_movies_table():
    query = """CREATE TABLE IF NOT EXISTS actors_movies (
                        actors_movies_Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        actors_id int,
                        movie_id int,
                        FOREIGN KEY (actors_id) REFERENCES actors(actors_id),                 
                        FOREIGN KEY (movie_id) REFERENCES movies(movie_id))"""
    create_table_database(query)




def insert_actors_movies(actor_name, movie_title):
    query = """INSERT INTO actors_movies (actors_id, movie_id)
                                        SELECT(SELECT actors_id FROM actors WHERE actor_name=?), 
                                        (SELECT movie_id FROM movies WHERE movie_title=?)"""
    params = (actor_name, movie_title)
    query_database(query, params)


def create_actor(Actor):
    query = "INSERT INTO actors VALUES (?,?)"
    params = (Actor.actor_id, Actor.actor_name)

    query_database(query, params)


def get_actors_movies_table():
    query = "SELECT * FROM actors_movies"
    query_database(query)


create_actors_table()
create_actors_movies_table()
Actor1 = Actors(None,"Brad Pit")
create_actor(Actor1)
insert_actors_movies("Brad Pit", "Filmas1")
get_actors_movies_table()
# create_table_database("DROP TABLE actors_movies")
