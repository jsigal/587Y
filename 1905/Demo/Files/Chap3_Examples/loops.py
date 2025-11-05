# The for Loop
prices = [200, 400, 500]
fee = 20
totals = []
for price in prices:
    totals.append(price - fee)
print(totals)

# Looping Through A Dictionary
airports = {'YYZ': 'Toronto', 'NRT': 'Tokyo'}

for code in airports.keys():
    print(code)

for code in airports:
    print(code)

for value in airports.values():
    print(value)

for key, value in airports.items():
    print(key, value)

# Nested Looping
prices = [200, 400, 500]
fees = [20, 50]
totals = []
for fee in fees:
    for price in prices:
        totals.append(price - fee)
print(totals)

# Membership Quiz With a Loop
codes = {'France': 33, 'Japan': 81,
         'GreatBritain': 44, 'USA': 1}
caps = {'France': 'Paris', 'Cuba': 'Havana',
        'Japan': 'Tokyo'}

countries = []
for code in codes:
    if code in caps:
        countries.append(code)

print(countries)

# Using break, continue, and else in a Loop
airports = ['LAX', 'HNL', 'YYZ']
for airport in airports:
    if airport == 'HNL':
        break
    print('with break', airport)
else:
    print('The end', airport)

for airport in airports:
    if airport == 'HNL':
        continue
    print('with continue', airport)
