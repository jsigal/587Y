"""
Exercise 5.2 Inheritance
Ex5_2_EndPoint_Bonus.py
"""

# Part A

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

# Part B
# Add the subclass below

class Flight(Trip):
    def __init__(self, flightnum=-1, cost=0.0, code=0, *args, **kwargs):
        self.flightnum = flightnum
        self.cost = cost
        self.code = code
        super().__init__(*args, **kwargs)

    def discount(self):
        discount = 0.0
        if self.is_interisland():
            discount = 0.05
        elif self.is_hawaiian():
            discount = 0.10
        elif self.is_caribbean():
            discount = 0.15
        self.cost -= (self.cost * discount)


class Reservation:
    def __init__(self, name=None, reservationid=None, flightref=None):
        self.name = name
        self.reservationid = reservationid
        self.flightref = flightref


# Part C
# Sample data for Flight
fnum = 221
cost = 399.99
craftcode = 2
depcity = 'CUR'
arrcity = 'HNL'
depdt = '2022-01-03 09:00'
arrdt = '2022-01-03 16:00'

myflight = Flight(flightnum=fnum,
                  cost = cost,
                  code = craftcode,
                  departcity=depcity,
                  arrivecity=arrcity,
                  departdaytime=depdt,
                  arrivedaytime=arrdt)

print('myflight', vars(myflight))

allflights = [Flight(*[317, 99.95, 4, 'HNL', 'HKG', '2022-01-03 16:00', '2022-01-03 20:00']),
              Flight(*[102, 199.99, 42, 'HNL', 'HNL', '2022-01-03 08:30', '2022-01-03 15:40']),
              Flight(*[204, 299.99, 44, 'HKG', 'CDG', '2022-01-03 19:20', '2022-01-04 12:35']),
              Flight(*[336, 199.99, 44, 'HKG', 'GCM', '2022-01-03 16:50', '2022-01-04 09:30']),
              Flight(*[660, 299.99, 3, 'HNL', 'ITO', '2022-01-03 12:00', '2022-01-03 13:55'])]

for flt in allflights:
    print(vars(flt))
    flt.discount()
    print(flt.cost, 'after discount')

# Part D

reservations = [{"name": "Pat Holder", "reservationid": "101A", "flightref": allflights[0]},
                {"name": "Peter Smith", "reservationid": "102B", "flightref": allflights[1]},
                {"name": "Guy Gildersleeve", "reservationid": "103C", "flightref": allflights[2]},
                {"name": "Janet Rider", "reservationid": "104D", "flightref": allflights[1]},
                {"name": "Lynn Jasper", "reservationid": "105E", "flightref": allflights[3]},
                {"name": "Ian Rouselle", "reservationid": "106F", "flightref": allflights[0]}]

for res in reservations:
    reservation = Reservation(**res)
    print("Reservation", reservation.reservationid, reservation.name,
          reservation.flightref.flightnum, reservation.flightref.cost)
