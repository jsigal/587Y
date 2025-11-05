"""
Exercise 7.2 Managing Files
Ex7_2a_EndPoint.py
"""

import sys

def main():
    file = r'C:\Course\1905\Data\flights.csv'
    search_flight = '1587'
    outfile = r'search_flights.csv'
    with open(file, 'r') as inf:
        with open(outfile, 'w') as outf:
            for line in inf:
                # print(line) # display each string
                fields = line.split(",")
                # print(fields) # display each list of strings
                if fields[0] == search_flight:
                    print(fields)
                    outf.write(','.join(fields))
try:
    main()
except IOError as ioe:
    print('Read or Write error on file', ioe.args, file=sys.stderr)
