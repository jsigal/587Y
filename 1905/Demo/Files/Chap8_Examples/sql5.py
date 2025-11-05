# Deleting Data
import sqlite3

connection = sqlite3.connect(r'C:\Course\1905\Data\airline.db')
curs = connection.cursor()

planecode = (6, )
planetype = ('Blimp', )

curs.execute('DELETE FROM aircraft WHERE aircraftcode = ?', planecode)

curs.execute('DELETE FROM aircraft WHERE name = ?', planetype)

connection.commit()
connection.close()


