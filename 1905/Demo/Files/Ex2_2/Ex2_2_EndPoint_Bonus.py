"""
Exercise 2.2 Strings and if.
Ex2_2_EndPoint_Bonus.py
"""

# Part A
plane1 = 'Boeing767 6670'
plane2 = 'CRJ        950'

plane1_type = plane1[:9]
plane2_type = plane2[:3]

plane1_miles = plane1[10:]
plane2_miles = plane2[11:]

print("plane1's type is", plane1_type, 'it flies', plane1_miles, 'miles')
print("plane2's type is", plane2_type, 'it flies', plane2_miles, 'miles')

totaltype = plane1_type + plane2_type
print('The concatenation of all plane types is', totaltype)

totalmiles = int(plane1_miles) + int(plane2_miles)
print('The total miles from all planes is', totalmiles)

# Part B
plane1 = 'Boeing767,6670'
plane2 = 'CRJ,950'

comma = plane1.find(',')
plane1_type = plane1[:comma]
plane1_miles = plane1[comma + 1:]

comma = plane2.find(',')
plane2_type = plane2[:comma]
plane2_miles = plane2[comma + 1:]

print("plane1's type is", plane1_type, 'it flies', plane1_miles)
print("plane2's type is", plane2_type, 'it flies', plane2_miles)

# Part C

print('The all uppercase plane type is')
if plane1_type.isupper():
    print(plane1_type)

if plane2_type.isupper():
    print(plane2_type)

print('The plane type that ends is a digit is', end=' ')
if plane1_type[-1].isdigit():
    print(plane1_type)

if plane2_type[-1].isdigit():
    print(plane2_type)

print('The plane that travels farther is', end=' ')
if int(plane1_miles) > int(plane2_miles):
    print(plane1_type, 'has range', plane1_miles)
else:
    print(plane2_type, 'has range', plane2_miles)

# Part D

print("""Python is Guido's invention""")
print('''They say "Python is Guido's invention"''')

airport1 = "HNL,Honolulu"
airport2 = "LHR,London/Heathrow"
airport3 = "ARN,Stockholm/Arlanda"
airport4 = "HKG,Hong Kong"
airport5 = "GCM,Grand Cayman BWI"

comma = airport1.find(',')
code1 = airport1[:comma]
city1 = airport1[comma + 1:]
comma = airport2.find(',')
code2 = airport2[:comma]
city2 = airport2[comma + 1:]
comma = airport3.find(',')
code3 = airport3[:comma]
city3 = airport3[comma + 1:]
comma = airport4.find(',')
code4 = airport4[:comma]
city4 = airport4[comma + 1:]
comma = airport5.find(',')
code5 = airport5[:comma]
city5 = airport5[comma + 1:]

codes = '"{0}","{1}","{2}","{3}","{4}"'.format(code1, code2, code3, code4, code5)
print('Airport codes', codes)

cities = '"{0}","{1}","{2}","{3}","{4}"'.format(city1, city2, city3, city4, city5)
print('City names', cities)

print(airport1.split(','))
