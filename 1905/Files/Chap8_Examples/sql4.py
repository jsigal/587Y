# Updating Data
import sqlite3

connection = sqlite3.connect(r'C:\Course\1905\Data\airline.db')
curs = connection.cursor()

updateplane1 = (7, 'Blimp')
updateplane2 = ('Bell430', 6)

curs.execute('UPDATE aircraft SET aircraftcode = ? WHERE name = ?', updateplane1)

curs.execute('UPDATE aircraft SET name = ? WHERE aircraftcode = ?', updateplane2)

connection.commit()
connection.close()


