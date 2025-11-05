"""
Exercise 3.2 Dictionaries, Sets, and Looping
Ex3_2_EndPoint.py
"""

# Part A
city_code_dict = {
    'HNL': 'Honolulu',
    'ITO': 'Hilo',
    'LHR': 'London/Heathrow',
    'ARN': 'Stockholm/Arlanda',
    'HKG': 'Hong Kong',
    'YYZ': 'Toronto',
    'CDG': 'Paris/Charles de Gaulle',
    'NRT': 'Tokyo/Narita',
    'GCM': 'Grand Cayman BWI',
    'CUR': 'Curacao Netherland Antilles'}

print('The airport codes and cities')
for key in city_code_dict:
    print(key, city_code_dict[key])

# Part B
codelist = ['HNL', 'ITO', 'LHR', 'LGA', 'GCM', 'MSY']
flightlist = ['HNL', 'HKG', '2022-01-03 16:00', '2022-01-03 20:00', 99.95, 4]

inkeys = []
notinkeys = []
for code in codelist:
    if code in city_code_dict:
        inkeys.append(code)
    else:
        notinkeys.append(code)
print('By looping the codes that are keys', inkeys)
print('By looping the codes that are not keys', notinkeys)

inkeys = [code for code in codelist if code in city_code_dict]
notinkeys = [code for code in codelist if code not in city_code_dict]
print('By list comprehension codes that are keys', inkeys)
print('By list comprehension codes that are not keys', notinkeys)

inkeys = list(set(codelist) & city_code_dict.keys())  # Dictionary keys are set-like
notinkeys = list(set(codelist) - city_code_dict.keys())
print('By sets codes that are keys', inkeys)
print('By sets codes that are not keys', notinkeys)

# Part C
flightdict = {
    102: ['HNL', 'HKG', '2022-01-03 16:00', '2022-01-03 20:00', 99.95, 4],
    132: ['HNL', 'HNL', '2022-01-03 08:30', '2022-01-03 15:40', 59.0, 2],
    276: ['HKG', 'CDG', '2022-01-03 19:20', '2022-01-04 12:35', 233.99, 2],
    303: ['HKG', 'ARN', '2022-01-03 16:50', '2022-01-04 13:30', 233.99, 2],
    498: ['NRT', 'ITO', '2022-01-03 12:00', '2022-01-03 20:55', 159.99, 2],
    390: ['CUR', 'CUR', '2022-01-03 09:00', '2022-01-03 16:30', 599.95, 3],
    465: ['NRT', 'YYZ', '2022-01-03 20:15', '2022-01-04 09:45', 59.0, 3],
    1305: ['ITO', 'ARN', '2022-01-03 18:50', '2022-01-04 10:00', 125.0, 2],
    375: ['HKG', 'HNL', '2022-01-03 09:10', '2022-01-03 16:30', 299.99, 4],
    444: ['NRT', 'LHR', '2022-01-03 23:15', '2022-01-04 13:20', 125.0, 3],
    1572: ['HNL', 'HNL', '2022-01-03 09:40', '2022-01-03 16:10', 125.0, 2]}

# Part D
airports = (
    "HNL,Honolulu",
    "LHR,London/Heathrow",
    "ARN,Stockholm/Arlanda",
    "HKG,Hong Kong",
    "GCM,Grand Cayman BWI")
