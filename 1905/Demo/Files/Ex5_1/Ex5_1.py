"""
Exercise 5.1 Classes and Initialization
Ex5_1.py
"""

# Part A

from typing import ClassVar

# step 12/13
class Aircraft:
    """
    Docstring for Aircraft
    """
    code:int
    name:str

    def __init__(self, code : int = None, name : str = None):
        self.code = code
        self.name = name

    def __str__(self):
        return f'code={self.code}, name={self.name}'


class Airport:
    """
    Docstring for Airport
    """
    citycode:str
    city:str

    def __init__(self, citycode : str = None, city : str = None):
        self.citycode = citycode
        self.city = city

    def __str__(self):
        return f'citycode={self.citycode}, code={self.city}'

class Trip:
    """This is a class to represent a Trip"""
    departcity : str
    arrivecity : str
    departdaytime : str
    arrivedaytime : str 
    cariblist : ClassVar[list] = ['GCM', 'CUR']
    hawaiilist : ClassVar[list] = ['ITO', 'HNL']

    def __init__(self, departcity : str=None, arrivecity:str=None,
                 departdaytime : str=None, arrivedaytime: str=None):
        self.departcity = departcity
        self.arrivecity = arrivecity
        self.departdaytime = departdaytime
        self.arrivedaytime = arrivedaytime
    def is_round_trip(self): # step 5
        """
        Docstring for is_round_trip
        
        :param self: Description
        """
        return self.departcity == self.arrivecity
    def is_hawiian(self): # step 8
        """
        Docstring for is_hawiian
        
        :param self: Description
        """
        return self.arrivecity in Trip.hawaiilist
    def is_caribbean(self): # step 8
        """
        Docstring for is_caribbean
        
        :param self: Description
        """
        return self.arrivecity in Trip.hawaiilist
    def is_interisland(self): # step 8
        """
        Docstring for is_interisland
        
        :param self: Description
        """
        return self.arrivecity in Trip.hawaiilist and self.departcity in Trip.hawaiilist   

# Sample data for Trip
depcity = 'CUR'
arrcity = 'HNL'
depdt = '2022-01-03 09:00'
arrdt = '2022-01-03 16:00'
# step 3 
mytrip = Trip(departcity=depcity,
              arrivecity=arrcity,
              departdaytime=depdt,
              arrivedaytime=arrdt)

# step 4
print(f'mytrip departs from {mytrip.departcity} at {mytrip.departdaytime} and arrives in {mytrip.departcity} at {mytrip.arrivedaytime}')
print(Trip.cariblist, Trip.hawaiilist)

# step 6
def test_rt():
    if mytrip.is_round_trip():
        print('round trip')
    else:
        print('not round trip')
test_rt()

# step 7
mytrip.arrivecity = mytrip.departcity
test_rt()

# Part B
# Create list of Trip objects, pass list as positional args to constructor

# step 9
alltrips = [Trip(*['HNL', 'HKG', '2022-01-03 16:00', '2022-01-03 20:00']),
Trip(*['HNL', 'HNL', '2022-01-03 08:30', '2022-01-03 15:40']),
Trip(*['HKG', 'CDG', '2022-01-03 19:20', '2022-01-04 12:35']),
Trip(*['HKG', 'GCM', '2022-01-03 16:50', '2022-01-04 09:30']),
Trip(*['HNL', 'ITO', '2022-01-03 12:00', '2022-01-03 13:55'])]


def print_trip(trp):
    print('Trip from', trp.departcity, 'to', trp.arrivecity,
            'Departs at', trp.departdaytime,
            'Arrives at', trp.arrivedaytime, end=' ')

# Step 10
for trip in alltrips:
    print_trip(trip)
    print(f'round_trip { trip.is_round_trip()}, caribbean {trip.is_caribbean()}, hawaiian {trip.is_hawiian()}, interisland {trip.is_interisland()}')

# Part C
# Sample Data for Aircraft
# code is 1
# name is Canadian Regional Jet
#
# Sample Data for Airport
# code is HNL
# citycity is Honolulu

# step 14
aircraft = Aircraft(1, "Canadian Regional Jet")
print(aircraft)
airport = Airport("HNL", "Honolulu")
print(airport)
airport.pref =5
print(airport.pref)
airport2 = Airport("LAX", "Los Angeles")
print(airport2)
# print(airport2.pref)