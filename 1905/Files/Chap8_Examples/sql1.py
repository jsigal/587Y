# Example SQL Query
import sqlite3

connection = sqlite3.connect(r'C:\Course\1905\Data\airline.db')
curs = connection.cursor()
for line in curs.execute('SELECT * FROM aircraft'):
    print(line)
connection.close()


