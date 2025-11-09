# The for Loop
prices = [200, 400, 500]
fee = 20
totals = []
for price in prices:
    totals.append(price - fee)
print(totals, type(totals))
print("first display")
for x in totals:
    print(x)
print("second display")
for x in totals:
    print(x)
# comprehensions
totals = [price - fee for price in prices]
print(totals, type(totals))

# Nested Looping
prices = [200, 400, 500]
fees = [20, 50]
totals = []
for fee in fees:
    for price in prices:
        totals.append(price - fee)
print(totals)
# Nested Looping via comp
prices = [200, 400, 500]
fees = [20, 50]
totals = [price - fee for price in prices for fee in fees]
print(totals)


# Membership Quiz With a Loop
codes = {'France': 33, 'Japan': 81,
         'GreatBritain': 44, 'USA': 1}
caps = {'France': 'Paris', 'Cuba': 'Havana',
        'Japan': 'Tokyo'}

countries = []
codes_not_in_caps =[]
for code in codes:
    if code in caps:
        countries.append(code)
    else:
        codes_not_in_caps.append(code)

print(countries)
print(codes_not_in_caps)

# Membership Quiz With a Loop via comp-
codes = {'France': 33, 'Japan': 81,
         'GreatBritain': 44, 'USA': 1}
caps = {'France': 'Paris', 'Cuba': 'Havana',
        'Japan': 'Tokyo'}
# codes in caps
countries = [code for code in codes if code in caps]
print(countries)
# codes not in caps
codes_not_in_caps = [code for code in codes if code not in caps]
print(codes_not_in_caps)


# The for Loop
prices = [200, 400, 500]
fee = 20
totals = []
for price in prices:
    totals.append(price - fee)
print(totals, type(totals))
print("first display")
for x in totals:
    print(x)
print("second display")
for x in totals:
    print(x)
# comprehensions
totals = [price - fee for price in prices]
print(totals, type(totals))
print("first display")
for x in totals:
    print(x)
print("second display")
for x in totals:
    print(x)
# generator
totals = (price - fee for price in prices)
print(totals, type(totals))
print("first display")
for x in totals:
    print(x)
print("second display")
for x in totals:
    print(x)