# Passing Arguments to SQL Statements
import sqlite3

connection = sqlite3.connect(r'C:\Course\1905\Data\airline.db')
curs = connection.cursor()

craftnum = (2, )
apt = ('HNL', )

for line in curs.execute('SELECT * FROM aircraft WHERE aircraftcode = ?', craftnum):
    print(line)

for line in curs.execute('SELECT * FROM airports WHERE citycode = ?', apt):
    print(line)

connection.close()


