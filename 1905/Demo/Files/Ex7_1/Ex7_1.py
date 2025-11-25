"""
Exercise 7.1 Exceptions
Ex7_1.py
"""

# step 7
import sys

def print_ftoc(temps):
    # step 12
    if len(temps) == 0:
        raise IndexError('no temps to process')
    for temp in temps:
        try: # step 10
            ctemp = (float(temp) - 32) * 5.0 / 9.0
        except ValueError as ve: # step 10
            print('invalid value for temperature', file=sys.stderr) # step 7
            print(f'the arguments to ValueError were {ve.args}', file=sys.stderr) # step 9
            ctemp = 0.0
        print('Farenheit temperature {0} is Celsius {1:.2f}'.format(temp, ctemp))


temps1 = ['123.0', '34.0', '5', '85']
temps2 = ['123.0', '34.0', 'five', '85']
temps3 = []

try: # step 6
    print_ftoc(temps1)
    print_ftoc(temps2)
    print_ftoc(temps3) # step 11
except ValueError as ve: # step 6 & 8
    print('invalid value for temperature', file=sys.stderr) # step 7
    print(f'the arguments to ValueError were {ve.args}', file=sys.stderr) # step 9
except IndexError as ie: # post step 12
    print(f'IndexError{ie.args}')