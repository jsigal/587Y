import sqlite3
import os

os.chdir(r'C:\Course\1905\Data')

con = sqlite3.connect('airline.db')

con.execute('''create table aircraft(
aircraftcode int primary key not null,
name text) ''')

con.execute('''create table airports(
citycode text primary key not null,
city text)''')

con.execute('''create table flights(
id int primary key not null,
flightnum int,
departcity text,
arrivecity text,
departtime text,
departday text,
arrivetime text,
arriveday text,
cost float,
code int)''')

con.execute('''create table reservations(
reservationid text primary key not null,
name text,
flightref int)''')
