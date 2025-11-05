"""
Exercise 4.1 Creating and Calling Functions
Ex4_1_EndPoint_Bonus.py
"""

# Data for the exercise
# Please do not modify these dictionaries

# Data description of city_code_dict
#    Airport Code : Airport Name

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

# Data description of flightdict
# flightnum : [ departcity, arrivecity, departdaytime,
#                arrivedaytime, cost, code ]


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


# Part A

def list_all_cities():
    for key in city_code_dict:
        print('Airport code', key, 'Airport name', city_code_dict[key])


def flights_per_city(apt):
    for key in flightdict:
        if flightdict[key][0] == apt:
            print('Flight', key, 'on the schedule', flightdict[key])


def flights_per_cities(dep, arr):
    return [key for key in flightdict if flightdict[key][0] == dep and
            flightdict[key][1] == arr]


# Part B

print('The list of airport codes and airports is')
list_all_cities()

searchcity = 'HNL'
searchcity = 'CUR'
searchcity = 'ITO'

searchcities = ['HNL', 'CUR', 'ITO'] # put into a list
for searchcity in searchcities:
    print('The flights from', searchcity)
    flights_per_city(searchcity)

departcity = 'NRT'
arrivecity = 'ITO'
print('The flights from', departcity, 'to', arrivecity)
flights = flights_per_cities(departcity, arrivecity)
for flight in flights:
    print('Flight', flight, 'travels from', departcity, 'to', arrivecity)

departcity = 'HKG'
arrivecity = 'HNL'
print('The flights from', departcity, 'to', arrivecity)
flights = flights_per_cities(dep=departcity, arr=arrivecity)
for flight in flights:
    print('Flight', flight, 'travels from', departcity, 'to', arrivecity)

def discount(price, disc):
    return price - (price * disc)

# Build list of price and discount pairs
price_disc_list = [[100, 0.05], [299, 0.15], [399.95, 0.10]]
for p, d in price_disc_list:
    print('Original = {0} discount = {1} discounted = {2}'.format(p,
        d, discount(p, d)))

def discount_printer(prices, discounts):
    for price, disc in zip(prices, discounts):
        print('Original = {0} discount = {1} discounted = {2}'.format(
            price, disc, discount(price, disc)))

pricelist = [100, 299, 399.95]
disclist = [0.05, 0.15, 0.10]
discount_printer(pricelist, disclist)
