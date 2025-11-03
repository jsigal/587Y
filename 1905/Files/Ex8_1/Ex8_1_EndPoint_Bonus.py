"""
Exercise 8.1 Accessing a MySQL database
Ex8_1_Endpoint_Bonus.py
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
    search_flight = input('Enter the flight number to retrieve -> ')
    cur.execute("SELECT * from flights where flightnum = ?", (search_flight, ))
    if (row := cur.fetchone()) is not None:
        print(row)
        for row in cur:
            print(row)
    else:
        print('Nothing found for flight', search_flight)


def insert_row(conn):
    cur = conn.cursor()
    sql = "INSERT INTO flights VALUES(?, ?, ?, ?, ?, ?, ?)"
    cur.execute(sql, new_flight)
    conn.commit()


def delete_row(conn):
    cur = conn.cursor()
    sql = "DELETE FROM flights WHERE flightnum = ?"
    cur.execute(sql, (new_flight[0], ))
    conn.commit()

connection = None
try:
    connection = open_connection()
    insert_row(connection)
    search_db(connection)
    delete_row(connection)

except IOError as ioe:
    print('File problems here', ioe.args, file=sys.stdout)
except sqlite3.OperationalError as oe:
    print('Something is wrong here', oe.args, file=sys.stderr)
finally:
    if connection:
        connection.close()
