"""
Exercise 7.1 Exceptions
Ex7_1_EndPoint_Bonus.py
"""

import sys

def print_ftoc(temps):
    if temps:
        for temp in temps:
            try:
                temp = float(temp)
            except ValueError as ve:
                print('ValueError handled', ve.args, 'with temp =', temp)
                print('Proceeding using 0.0 as temp')
                temp = 0.0
            ctemp = (temp - 32) * 5.0 / 9.0
            print('Farenheit temperature {0} is Celsius {1:.2f}'.format(temp, ctemp))
    else:
        raise IndexError('Zero length list')


temps1 = ['123.0', '34.0', '5', '85']
temps2 = ['123.0', '34.0', 'five', '85']
temps3 = []

try:
    print_ftoc(temps1)
    print_ftoc(temps2)
    print_ftoc(temps3)
except ValueError as ve:
    print('ValueError encountered in main program', ve.args, file=sys.stderr)
except IndexError as ie:
    print('IndexError encountered', ie.args, file=sys.stderr)
