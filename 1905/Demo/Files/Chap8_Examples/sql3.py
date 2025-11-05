# Inserting a Row
import sqlite3

connection = sqlite3.connect(r'C:\Course\1905\Data\airline.db')
curs = connection.cursor()

newplane1 = (5, 'Blimp')
newplane2 = (6, 'Helicopter')

curs.execute('INSERT INTO aircraft VALUES (?, ?)',
             newplane1)
curs.execute('INSERT INTO aircraft VALUES (?, ?)',
             newplane2)

connection.commit()
connection.close()
