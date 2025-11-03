"""
Exercise 7.2 Managing Files
Ex7_2a.py
"""

import sys

def main():
    file = r'C:\Course\1905\Data\flights.csv'
    search_flight = '1587'


try:
    main()
except IOError as ioe:
    print('Read or Write error on file', ioe.args, file=sys.stderr)
