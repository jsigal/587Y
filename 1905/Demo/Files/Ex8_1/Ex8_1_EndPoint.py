"""
Exercise 8.1 Accessing a MySQL database
Ex8_1_EndPoint.py
"""

import sys
import sqlite3
import os.path

new_flight = [99999, 'HNL', 'CDG', "2022-02-04 04:00", "2022-02-04", 599.95, 4]

def open_connection():
    databasename = r'C:\Course\1905\Data\airline.db'
    if not os.path.isfile(databasename):
        raise IOError(databasename, 'not found')
    return sqlite3.connect(databasename)

def search_db(conn):
    cur = conn.cursor()
    for row in cur.execute("SELECT * FROM flights"):
        print(row)

connection = None
try:
    connection = open_connection()
    search_db(connection)
except IOError as ioe:
    print('File problems here', ioe.args, file=sys.stdout)
except sqlite3.OperationalError as oe:
    print('Something is wrong here', oe.args, file=sys.stderr)
finally:
    if connection:
        connection.close()
