# Class Inheritance
class Trip:
    def __init__(self, departday=None, arriveday=None):
        self.departday = departday
        self.arriveday = arriveday
    def print_departure(self):
        print('Trip leaves on', self.departday)

class Cruise(Trip):
    def print_schedule(self):
        print('Cruise', self.departday, 'to', self.arriveday)

class Flight(Trip):
    def print_arrival(self):
        print('Flight arrives on', self.arriveday)

voyage = Cruise(departday='Friday', arriveday='Monday')
voyage.print_departure()
voyage.print_schedule()

flthome = Flight(departday='Monday', arriveday='Monday')
flthome.print_departure()
flthome.print_arrival()
