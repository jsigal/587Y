"""
Exercise 8.1 Accessing a MySQL database
Ex8_1_Describe.py
"""

import sys
import sqlite3
import os.path
import re

def open_connection():
    databasename = r'C:\Course\1905\Data\airline.db'
    if not os.path.isfile(databasename):
        raise IOError(databasename, 'not found')
    connection = sqlite3.connect(databasename)
    return connection

def describe_tables():
    curs = connection.cursor()
    for line in curs.execute("SELECT * from sqlite_master"):
        if line[0] == 'table':
            print('Table name is', line[1])
            for col in re.findall(r'\n[a-z]+ ', line[4]):
                print('Column name is', re.sub(r'\n', '', col))
            print("Created with:", re.sub(r'\n', ' ', line[4]))
            print('=' * 110)

connection = None
try:
    connection = open_connection()
    describe_tables()
except IOError as ioe:
    print('File problems here', ioe.args, file=sys.stdout)
except sqlite3.OperationalError as oe:
    print('Something is wrong here', oe.args, file=sys.stderr)
finally:
    if connection:
        connection.close()
