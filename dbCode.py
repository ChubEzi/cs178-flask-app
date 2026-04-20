# dbCode.py
# Author: Your Name
# Helper functions for database connection and queries

import pymysql
import creds
#import credits as creds

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
    SELECT movies.movie_id, movies.name, genres.genre_name
    FROM movies
    JOIN genres ON movies.genre_id = genres.genre_id
    """

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return results
