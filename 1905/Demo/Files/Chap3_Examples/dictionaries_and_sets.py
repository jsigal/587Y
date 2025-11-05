# Dictionary Operations
cities = {'YYZ': 'Toronto', 'NRT': 'Tokyo/Narita'}
print(cities['NRT'])
cities['NRT'] = 'Tokyo'
cities['HNL'] = 'Honolulu'
print(cities)
del cities['YYZ']
print(cities)

# Dictionary Methods and Functions
depcode = input("Enter the departure ")
print(cities.get(depcode.upper(), "Incorrect code"))
arrcode = input("Enter the arrival ")
print(cities[arrcode.upper()])

# View Objects
cities = {'YYZ': 'Toronto', 'NRT': 'Tokyo'}
ckeys = cities.keys()
cvalues = cities.values()
print(ckeys, cvalues, sep='\n')
cities['HNL'] = 'Honolulu'
print(ckeys, cvalues, sep='\n')
print(cities.items())

# Creating a Dictionary
apts = {'SFO': 'San Francisco', 'LAX': 'Los Angeles'}
print(apts)
apts = dict((('SFO', 'San Francisco'), ('LAX', 'Los Angeles')))
print(apts)
apts = dict(SFO='San Francisco', LAX='Los Angeles')
print(apts)

# zip() Function
codes = ['ORD', 'MCO']
cities = ['Chicago', 'Orlando']
bycodes = dict(zip(codes, cities))
bycities = dict(zip(cities, codes))
print(bycodes)
print(bycities)

# Copying a Dictionary
cities = {'YYZ': 'Toronto', 'NRT': 'Tokyo'}
favcities = cities
print(favcities is cities)
favcities = cities.copy()
print(favcities is cities)
print(favcities == cities)

# Sets
hawaii_airports = set(['HNL', 'ITO', 'HNL'])
pacific_airports = {'HNL', 'NRT', 'SYD', 'LAX'}
hawaii_airports.add('LNY')
pacific_airports.remove('LAX')
print(hawaii_airports)
print(pacific_airports)

print(hawaii_airports - pacific_airports)
print(pacific_airports - hawaii_airports)
print(hawaii_airports | pacific_airports)
print(hawaii_airports & pacific_airports)
print(hawaii_airports > pacific_airports)
