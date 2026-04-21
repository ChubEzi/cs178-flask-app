# dbCode.py
# Author: Ezri Lopez
# Helper functions for database connection and queries

import pymysql
import creds


def get_conn():
    """Returns a connection to the MySQL RDS instance."""
    conn = pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
    )
    return conn

def execute_query(query, args=()):
    """Executes a SELECT query and returns all rows as dictionaries."""
    cur = get_conn().cursor(pymysql.cursors.DictCursor)
    cur.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

def getMoviesWithGenres():
    conn = get_conn()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = """
    SELECT movie.movie_id, movie.title, genre.genre_name.
    FROM movie
    JOIN movie_genres ON movie.movie_id = movie_genres.movie_id 
    JOIN genre ON movie_genres.genre_id = genre.genre_id
    """
# FROM movie m JOIN movie_genres mg ON m.movie_id = mg.movie_id JOIN genres g ON mg.genre_id = g.genre_id;

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return results
