"""
CSV_reader.py
"""

import csv

class Aircraft:
    def __init__(self, aircraftcode=None, name=None):
        self.aircraftcode = aircraftcode
        self.name = name

aircraftcsv = 'C:/Course/1905/Data/aircraft.csv'

with open(aircraftcsv) as inputfile:
    filereader = csv.DictReader(inputfile)
    for dataline in filereader:   # iterate through the file
        plane = Aircraft(**dataline)
        print('One line as an Aircraft object', vars(plane))
