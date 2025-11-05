"""
Exercise 5.1 Classes and Initialization
Ex5_1.py
"""

# Part A

class Trip:

    cariblist = ['GCM', 'CUR']
    hawaiilist = ['ITO', 'HNL']

    def __init__(self, departcity=None, arrivecity=None,
                 departdaytime=None, arrivedaytime=None):
        self.departcity = departcity
        self.arrivecity = arrivecity
        self.departdaytime = departdaytime
        self.arrivedaytime = arrivedaytime

# Sample data for Trip
depcity = 'CUR'
arrcity = 'HNL'
depdt = '2022-01-03 09:00'
arrdt = '2022-01-03 16:00'
# mytrip = Trip(departcity=depcity,
#               arrivecity=arrcity,
#               departdaytime=depdt,
#               arrivedaytime=arrdt)

# Part B
# Create list of Trip objects, pass list as positional args to constructor

# alltrips = [Trip(*['HNL', 'HKG', '2022-01-03 16:00', '2022-01-03 20:00']),
# Trip(*['HNL', 'HNL', '2022-01-03 08:30', '2022-01-03 15:40']),
# Trip(*['HKG', 'CDG', '2022-01-03 19:20', '2022-01-04 12:35']),
# Trip(*['HKG', 'GCM', '2022-01-03 16:50', '2022-01-04 09:30']),
# Trip(*['HNL', 'ITO', '2022-01-03 12:00', '2022-01-03 13:55'])]

#
# def print_trip(trp):
#     print('Trip from', trp.departcity, 'to', trp.arrivecity,
#             'Departs at', trp.departdaytime,
#             'Arrives at', trp.arrivedaytime, end=' ')



# Part C
# Sample Data for Aircraft
# code is 1
# name is Canadian Regional Jet
#
# Sample Data for Airport
# code is HNL
# citycity is Honolulu
