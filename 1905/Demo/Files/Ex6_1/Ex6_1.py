"""
Exercise 6.1 Modules
Ex6_1.py
"""

import glob
import os
import shutil
import airlineclasses as ac
import reservationclass as rc, reservationdata as rd

flight_data = (221, 'HNL', 'HNL', '2022-01-03 08:30', '2022-01-03 15:40', 399.99, 2)

flight_attributes = ('flightnum', 'departcity', 'arrivecity', 'departdaytime',
                     'arrivedaytime', 'cost', 'code')

def main_pgm():
    print('This is main_pgm()')
    # step 5
    flight_dict = dict(zip(flight_attributes, flight_data))
    flt = ac.Flight(**flight_dict)
    print(vars(flt))
    # step 9
    res = (rc.Reservation(*rd.resdata1),
        rc.Reservation(*rd.resdata2))
    for r in res:
        print(r.name, r.reservationid, vars(r.flightref))
    # step 10
    # Get the path of the current file
    current_file_path = __file__
    # Get the directory of the current file
    current_directory = os.path.dirname(current_file_path)
    os.chdir(current_directory)
    shutil.copy('reservationdata.py','reservationdata.backup')
    # step 11
    for f in glob.glob('*.py'):
        print(f)

if __name__ == '__main__':
    main_pgm()
