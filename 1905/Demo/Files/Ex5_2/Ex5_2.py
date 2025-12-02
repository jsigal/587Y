"""
Exercise 5.2 Inheritance
Ex5_2.py
"""

# Part A

class Reservation(): # step 8
    def __init__(self, name, reservationid, flightref):
        self.name = name
        self.reservationid = reservationid
        self.flightref = flightref

    def __str__(self):
        return f'Reservation {self.reservationid} for {self.name}: {self.flightref}'

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

    def __str__(self):
        return f'departs from {self.departcity} at {self.departdaytime}, arrives in {self.arrivecity} at {self.arrivedaytime}'

# Part B
# Add the subclass below

class Flight(Trip): # step 3
    def __init__(self, flightnum=-1, cost=0.0, code=0, *args, **kwargs):
        self.flightnum = flightnum
        self.cost = cost
        self.code = code
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'Flight {self.flightnum} code {self.code} costs {self.cost}, ' + super().__str__()

    def discount(self):
        if self.is_interisland():
            self.cost *= .95
        elif self.is_hawaiian():
            self.cost *= .90
        elif self.is_caribbean():
            self.cost *= .85

# Part C
# Sample data for Flight
fnum = 221
cost = 399.99
craftcode = 2
depcity = 'CUR'
arrcity = 'HNL'
depdt = '2022-01-03 09:00'
arrdt = '2022-01-03 16:00'

mytrip = Flight(flightnum=fnum,
                cost = cost,
                code = craftcode,
                departcity=depcity,
                arrivecity=arrcity,
                departdaytime=depdt,
                arrivedaytime=arrdt)
# step 4
print(vars(mytrip))

allflights = [Flight(*[317, 99.95, 4, 'CUR', 'ITO', '2022-01-03 16:00', '2022-01-03 20:00']),
              Flight(*[102, 199.99, 42, 'HNL', 'HNL', '2022-01-03 08:30', '2022-01-03 15:40']),
              Flight(*[204, 299.99, 44, 'HKG', 'CDG', '2022-01-03 19:20', '2022-01-04 12:35']),
              Flight(*[336, 199.99, 44, 'HKG', 'GCM', '2022-01-03 16:50', '2022-01-04 09:30']),
              Flight(*[660, 299.99, 3, 'HNL', 'ITO', '2022-01-03 12:00', '2022-01-03 13:55'])]
# step 5
for flt in allflights:
    print(flt)
    # step 7
    flt.discount()
    print(flt)

# Part D

reservations = [Reservation(**{"name": "Pat Holder", "reservationid": "101A", "flightref": allflights[0]}),
                Reservation(**{"name": "Peter Smith", "reservationid": "102B", "flightref": allflights[1]}),
                Reservation(**{"name": "Guy Gildersleeve", "reservationid": "103C", "flightref": allflights[2]}),
                Reservation(**{"name": "Janet Rider", "reservationid": "104D", "flightref": allflights[3]}),
                Reservation(**{"name": "Lynn Jasper", "reservationid": "105E", "flightref": allflights[4]}),
                Reservation(**{"name": "Ian Rouselle", "reservationid": "106F", "flightref": allflights[0]})]

for r in reservations:
    # print(r.reservationid, r.name, r.flightref)
    print(r)