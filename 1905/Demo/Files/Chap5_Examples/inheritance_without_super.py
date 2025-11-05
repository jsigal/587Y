# Subclass Instance Initialization
class Trip:
    def __init__(self, departday=None, arriveday=None):
        self.departday = departday
        self.arriveday = arriveday

    def print_departure(self):
        print('Trip leaves on', self.departday)

class Cruise(Trip):
    def __init__(self, departday, arriveday, ship=None):
        self.ship = ship
        Trip.__init__(self, departday=departday,
                      arriveday=arriveday)

    def print_schedule(self):
        print('Cruise', self.departday, 'to', self.arriveday)

voyage = Cruise(departday='Friday', arriveday='Monday',
                ship='Sea Breeze')
voyage.print_departure()
voyage.print_schedule()
