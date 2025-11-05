"""
Exercise 7.2 Managing Files
Ex7_2b.py
"""

import csv
import airlineclasses
import sys

def main():
    file = 'C:/Course/1905/Data/flights.csv'

try:
    main()
except IOError as ioe:
    print('Read or Write error on file', ioe.args, file=sys.stderr)
