"""
Exercise 2.2 Strings and if.
Ex2_2.py
"""

# Part A
plane1 = 'Boeing767 6670'
plane2 = 'CRJ        950'

plane1_type = plane1[:9]
plane1_range = plane1[10:]
plane2_type = plane2[:3]
plane2_range = plane2[11:]

print(f'plane 1 is a {plane1_type} and can go this far {plane1_range}')
print(f'plane 2 is a {plane2_type} and can go this far {plane2_range}')
print(f'the two planes are {plane1_type + ' ' + plane2_type}')
print(f'the total range is {int(plane1_range)+int(plane2_range)}')

# Part B
plane1 = 'Boeing767,6670'
plane2 = 'CRJ,950'

plane1_comma = plane1.find(',')
plane2_comma = plane2.find(',')

plane1_type = plane1[:plane1_comma]
plane1_range = plane1[plane1_comma + 1:]
plane2_type = plane2[:plane2_comma]
plane2_range = plane2[plane2_comma+1:]

print(f'plane 1 is a {plane1_type} and can go this far {plane1_range}')
print(f'plane 2 is a {plane2_type} and can go this far {plane2_range}')


# Part C
if plane1_type.isupper():
    print(f'{plane1_type} is uppercase')
else:
    print(f'{plane1_type} is not uppercase')

if plane2_type.isupper():
    print(f'{plane2_type} is uppercase')
else:
    print(f'{plane2_type} is not uppercase')

# Part D

print()
print()

airport1 = "HNL,Honolulu"
airport2 = "LHR,London/Heathrow"
airport3 = "ARN,Stockholm/Arlanda"
airport4 = "HKG,Hong Kong"
airport5 = "GCM,Grand Cayman BWI"
