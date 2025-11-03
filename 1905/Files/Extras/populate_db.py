import sqlite3
import csv
import os

os.chdir(r'C:\Course\1905\Data')
con = sqlite3.connect('airline.db')
curs = con.cursor()

airportscsv = 'C:/Course/1905/Data/airports.csv'
with open(airportscsv, 'r') as infile:
    linereader = csv.reader(infile)
    for oneline in linereader:
        curs.execute('''insert into airports values(?,?)''', oneline)
con.commit()

aircraftcsv = 'C:/Course/1905/Data/aircraft.csv'
with open(aircraftcsv, 'r') as infile:
    linereader = csv.reader(infile)
    for oneline in linereader:
        curs.execute('''insert into aircraft values(?,?)''', oneline)
con.commit()

flightscsv = 'C:/Course/1905/Data/flights.csv'
with open(flightscsv, 'r') as infile:
    linereader = csv.reader(infile)
    for oneline in linereader:
        curs.execute('''insert into flights values(?,?,?,?,?,?,?,?,?,?)''', oneline)
con.commit()

reservationscsv = 'C:/Course/1905/Data/reservations.csv'
with open(reservationscsv, 'r') as infile:
    linereader = csv.reader(infile)
    for oneline in linereader:
        curs.execute('''insert into reservations values(?,?,?)''', oneline)
con.commit()
con.close()
