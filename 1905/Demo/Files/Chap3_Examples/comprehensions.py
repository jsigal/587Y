# List Comprehension
prices = [200, 400, 500]
fee = 20
totals = [price - fee for price in prices]
print(totals[0])
for total in totals:
    print(total)

fees = [20, 50]
print([price - fee for fee in fees for price in prices])

# List Comprehension With Conditional
fee = 30
minimum = 200
print([price - fee for price in prices if price > minimum])

codes = {'France': 33, 'Japan': 81,
         'GreatBritain': 44, 'USA': 1}
caps = {'France': 'Paris', 'Cuba': 'Havana',
        'Japan': 'Tokyo'}

print([code for code in codes if code in caps])

# Additional Comprehensions
airports = {'LAX', 'HNL', 'YYZ'}
hawaiiairports = {airport for airport in airports
                  if airport in ['HNL', 'ITO']}
print(hawaiiairports)

airports = {'LAX': 'Los Angeles', 'HNL': 'Honolulu',
            'YYZ': 'Toronto'}
hawaiidict = {code: city for code, city in airports.items()
              if code in ['HNL', 'ITO']}
print(hawaiidict)

# Generator Expression
prices = [200, 400, 500]
fee = 20
totals = (price - fee for price in prices)
print(next(totals))
print('start loop')
for total in totals:
    print(total)
