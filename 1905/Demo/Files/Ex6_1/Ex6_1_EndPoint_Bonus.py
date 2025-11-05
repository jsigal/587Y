"""
Exercise 6.1 Modules
Ex6_1_EndPoint_Bonus.py
"""

import airlineclasses as ac
import reservationclass, reservationdata
import shutil, glob

flight_data = (221, 'HNL', 'HNL', '2022-01-03 08:30', '2022-01-03 15:40', 399.99, 2)

flight_attributes = ('flightnum', 'departcity', 'arrivecity', 'departdaytime',
                     'arrivedaytime', 'cost', 'code')

def main_pgm():
    data_dict = dict(zip(flight_attributes, flight_data))
    flt = ac.Flight(**data_dict)
    print('\nSample flight:\n', vars(flt))

    reservation1 = reservationclass.Reservation(*reservationdata.resdata1)
    reservation2 = reservationclass.Reservation(*reservationdata.resdata2)
    print('\nSample Reservation 1:')
    print(vars(reservation1), vars(reservation1.flightref), sep='\n')
    print('\nSample Reservation 2:')
    print(vars(reservation2), vars(reservation2.flightref), sep='\n')

    shutil.copy('reservationdata.py', 'reservationdata.backup')
    print('The python files')
    for name in glob.glob('*.py'):
        print(name)

if __name__ == '__main__':
    main_pgm()
