# Subclass Instance Initialization Using super()
class Trip:
    def __init__(self, departday=None, arriveday=None):
        self.departday = departday
        self.arriveday = arriveday

    def print_departure(self):
        print('Trip leaves on', self.departday)

class Cruise(Trip):
    def __init__(self, departday, arriveday, ship=None):
        self.ship = ship
        super().__init__(departday=departday,
                         arriveday=arriveday)

    def print_schedule(self):
        print('Cruise', self.departday, 'to', self.arriveday)

voyage = Cruise(departday='Friday', arriveday='Monday',
                ship='Sea Breeze')
voyage.print_departure()
voyage.print_schedule()

# Calling Superclass Methods Using *args and **kwargs
class Trip:
    def __init__(self, departday=None, arriveday=None):
        self.departday = departday
        self.arriveday = arriveday

    def print_departure(self):
        print('Trip leaves on', self.departday)

class Cruise(Trip):
    def __init__(self, ship=None, *args, **kwargs):
        self.ship = ship
        super().__init__(*args, **kwargs)

    def print_schedule(self):
        print('Cruise', self.departday, 'to', self.arriveday)

voyage = Cruise(departday='Friday', arriveday='Monday',
                ship='Sea Breeze')
voyage.print_departure()
voyage.print_schedule()
