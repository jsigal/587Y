"""
Exercise 7.2 Managing Files
Ex7_2b_EndPoint_Bonus.py
"""
import csv
import airlineclasses
import sys

def main():
    file = 'C:/Course/1905/Data/flights.csv'

    with open(file, 'r') as inf:
        filereader = csv.DictReader(inf)
        allflights = [airlineclasses.Flight(**datadict) for datadict in filereader]

    print(len(allflights), 'flights created')
    print('Last flight', vars(allflights[-1]))

try:
    main()
except IOError as ioe:
    print('Read or Write error on file', ioe.args, file=sys.stderr)