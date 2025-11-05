# Exception Class Hierarchy
def convert_any_digits(indx, digits):
    return int(digits[indx])

try:
    print(convert_any_digits(1, ['12', '34'])) # Works
    print(convert_any_digits('b', {'a': '12', 'b': '34'})) # Works
    print(convert_any_digits(3, ['12', '34'])) # IndexError
  # print(convert_any_digits('c', {'a': '12', 'b': '34'})) # KeyError
except LookupError as le:
    print('Look Up Error handled', le.args)
except ValueError as ve:
    print('Value Error handled', ve.args)
