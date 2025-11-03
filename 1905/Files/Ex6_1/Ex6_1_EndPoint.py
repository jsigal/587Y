"""
Exercise 6.1 Modules
Ex6_1_EndPoint.py
"""

import airlineclasses as ac

flight_data = (221, 'HNL', 'HNL', '2022-01-03 08:30', '2022-01-03 15:40', 399.99, 2)

flight_attributes = ('flightnum', 'departcity', 'arrivecity', 'departdaytime',
                     'arrivedaytime', 'cost', 'code')

def main_pgm():
    data_dict = dict(zip(flight_attributes, flight_data))
    flt = ac.Flight(**data_dict)
    print('Sample flight', vars(flt))


if __name__ == '__main__':
    main_pgm()
