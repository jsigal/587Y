"""
Exercise 6.1 reservationdata.py
"""

import airlineclasses


flight1 = airlineclasses.Flight(flightnum=257, departcity='HNL', arrivecity='YYZ',
                                departdaytime='2022-01-03 08:30',
                                arrivedaytime='2022-01-03 15:40',
                                cost=783.50, code=1)

flight2 = airlineclasses.Flight(flightnum=258, departcity='CDG', arrivecity='LGA',
                                departdaytime='2022-01-03 19:20',
                                arrivedaytime='2022-01-04 12:35',
                                cost=783.50, code=1)

resdata1 = ('Lars Olsen', '200X', flight1)
resdata2 = ('Paul LeBeau', '201Y', flight2)

if __name__ == '__main__':
    print(resdata1, vars(flight1))
    print(resdata2, vars(flight2))
else:
    print('reservationdata.py imported, no Reservation created')
