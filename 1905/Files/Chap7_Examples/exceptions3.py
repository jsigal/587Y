# Handling Multiple Exception Types
def print_age_in_days(years):
    print('Age in days is', 365.25 * int(years))

try:
    age = input('Enter your age: ')
    print_age_in_days(age)
except ValueError:
    print('You did not input the age as an integer')
except EOFError:
    print('End of file from standard input')
except:
    print('Non Value or EOF error occurred')


