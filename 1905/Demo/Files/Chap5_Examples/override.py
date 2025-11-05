# Overriding Methods
class Trip:
    def __init__(self, departday=None, arriveday=None):
        self.departday = departday
        self.arriveday = arriveday

    def print_trip(self):
        print('Schedule is', self.departday, self.arriveday)

class Cruise(Trip):
    def __init__(self, ship=None, *args, **kwargs):
        self.ship = ship
        super().__init__(*args, **kwargs)

    def print_trip(self):
        print('Ship is', self.ship)

day1 = Cruise(departday='Friday', arriveday='Saturday',
                  ship='Moonbeam')
day1.print_trip()

# Overriding Methods - Continued
class Trip:
    def __init__(self, departday=None, arriveday=None):
        self.departday = departday
        self.arriveday = arriveday

    def print_trip(self):
        print('Schedule is', self.departday, self.arriveday,
              end=' ')

class Cruise(Trip):
    def __init__(self, ship=None, *args, **kwargs):
        self.ship = ship
        super().__init__(*args, **kwargs)

    def print_trip(self):
        super().print_trip()
        print('Ship is', self.ship)

travels = [Cruise(departday='Friday', arriveday='Saturday',
           ship='Moonbeam'),
           Cruise(departday='Wednesday', arriveday='Friday',
           ship='Golden Sun')]

for travel in travels:
    travel.print_trip()
