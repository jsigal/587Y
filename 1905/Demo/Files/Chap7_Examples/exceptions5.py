# Exception Instances
def print_age_in_days(years):
    print('Age in days is', 365.25 * int(years))

try:
    age = input('Enter your age: ')
    print_age_in_days(age)
except ValueError as ve:
    print('You did not input the age as an integer')
    print('Value Error handled', ve.args)
else:
    print(age, 'was successfully converted to integer')
finally:
    print('Input test complete')




