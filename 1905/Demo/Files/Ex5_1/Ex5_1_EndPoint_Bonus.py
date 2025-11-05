"""
Exercise 5.1 Classes and Initialization
Ex5_1_EndPoint_Bonus.py
"""

# Part A

class Aircraft:
    def __init__(self, code=None, name=None):
        self.code = code
        self.name = name


class Airport:
    def __init__(self, citycode=None, city=None):
        self.citycode = citycode
        self.city = city


class Trip:

    cariblist = ['CUR', 'GCM']
    hawaiilist = ['HNL', 'ITO']

    def __init__(self, departcity=None, arrivecity=None,
                 departdaytime=None, arrivedaytime=None):
        self.departcity = departcity
        self.arrivecity = arrivecity
        self.departdaytime = departdaytime
        self.arrivedaytime = arrivedaytime

    def is_round_trip(self):
        return self.arrivecity == self.departcity

    def is_caribbean(self):
        return self.arrivecity in Trip.cariblist

    def is_hawaiian(self):
        return self.arrivecity in Trip.hawaiilist

    def is_interisland(self):
        return self.arrivecity in Trip.hawaiilist and self.departcity in Trip.hawaiilist


# Sample data for Trip
depcity = 'CUR'
arrcity = 'HNL'
depdt = '2022-01-03 09:00'
arrdt = '2022-01-03 16:00'
mytrip = Trip(departcity=depcity,
              arrivecity=arrcity,
              departdaytime=depdt,
              arrivedaytime=arrdt)

print('mytrip', mytrip.departcity, mytrip.arrivecity, mytrip.departdaytime,
      mytrip.arrivedaytime)

print('The cariblist is', Trip.cariblist)
print('The hawaiilist is ', Trip.hawaiilist)

# test with a round trip
answer = 'is' if mytrip.is_round_trip() else 'is not'
print(mytrip.departcity, 'to', mytrip.arrivecity, answer, 'a round trip')

# create second that is not a round trip
mytrip = Trip(departcity=depcity,
              arrivecity=depcity,
              departdaytime=depdt,
              arrivedaytime=arrdt)

# test if not a round trip
answer = 'is' if mytrip.is_round_trip() else 'is not'
print(mytrip.departcity, 'to', mytrip.arrivecity, answer, 'a round trip')

# Part B
# Create list of Trip objects, pass list as positional args to constructor

alltrips = [Trip(*['HNL', 'HKG', '2022-01-03 16:00', '2022-01-03 20:00']),
Trip(*['HNL', 'HNL', '2022-01-03 08:30', '2022-01-03 15:40']),
Trip(*['HKG', 'CDG', '2022-01-03 19:20', '2022-01-04 12:35']),
Trip(*['HKG', 'GCM', '2022-01-03 16:50', '2022-01-04 09:30']),
Trip(*['HNL', 'ITO', '2022-01-03 12:00', '2022-01-03 13:55'])]


def print_trip(trp):
    print('Trip from', trp.departcity, 'to', trp.arrivecity,
            'Departs at', trp.departdaytime,
            'Arrives at', trp.arrivedaytime)


for atrip in alltrips:
    print_trip(atrip)
    if atrip.is_round_trip():
        print('\tis RoundTrip')
    if atrip.is_caribbean():
        print('\tis Caribbean')
    if atrip.is_hawaiian():
        print('\tis Hawaiian')
    if atrip.is_interisland():
        print('\tis Interisland')

# Part C    
# Sample Data for Aircraft
# code is 1
# name is Canadian Regional Jet
#
# Sample Data for Airport
# citycode is HNL
# city is Honolulu

sampleaircraft = Aircraft(code=1, name='Canadian Regional Jet')
sampleairport = Airport(citycode='HNL', city='Honolulu')
print('sampleaircraft', sampleaircraft.code, sampleaircraft.name)
print('sampleairport', sampleairport.citycode, sampleairport.city)
