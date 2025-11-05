"""
Exercise 6.1 airlineclasses.py
"""


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


class Flight(Trip):
    def __init__(self, flightnum=-1, cost=0.0, code=0, *args, **kwargs):
        self.flightnum = flightnum
        self.cost = cost
        self.code = code
        super().__init__(*args, **kwargs)

    def discount(self):
        amount = 0.0
        if self.is_interisland():
            amount = 0.05
        elif self.is_hawaiian():
            amount = 0.10
        elif self.is_caribbean():
            amount = 0.15
        self.cost -= (self.cost * amount)

def make_sample_trip_flight():
    trip_attributes = ('departcity', 'arrivecity', 'departdaytime', 'arrivedaytime')
    trip_data = ('HNL', 'HNL', '2022-01-03 08:30', '2022-01-03 15:40')
    flight_attributes = ('flightnum', 'cost', 'code')
    flight_data = (221, 399.99, 2)
    data = dict(zip(trip_attributes, trip_data))
    sample_trip = Trip(**data)
    print('Trip:', vars(sample_trip))  # vars() returns dictionary of attributes
    data = dict(zip(trip_attributes + flight_attributes, trip_data + flight_data))
    sample_flight = Flight(**data)
    print('Flight:', vars(sample_flight))

if __name__ == '__main__':
    print('Running as main')
    make_sample_trip_flight()
else:
    print('airlineclasses.py imported, no Trip or Flight created')
