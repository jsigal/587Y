# The raise Statement
import string
def print_age_in_days(years):
    for digit in years:
        if digit not in string.digits:
            raise ValueError('Cannot convert', digit)
    print('Your age in days is more than', 365 * int(years))

try:
    age = input('Enter your age: ')
    print_age_in_days(age)
except ValueError as ve:
    print('You did not input the age as an integer')
    print('Value Error handled', ve.args)
