# The __init__() Method
class Cruise:
    """ This class describes a cruise."""
    def __init__(self, ship=None, cost=0.0, cabin=0):
        self.ship = ship
        self.cost = cost
        self.cabin = cabin

# The self Parameter
myvacation = Cruise(ship='Voyager', cabin=101)
yourvacation = Cruise(ship='Sundowner',
                      cost=157.50, cabin=511)
print(myvacation.ship, myvacation.cabin, myvacation.cost)
print(yourvacation.ship, yourvacation.cabin, yourvacation.cost)

# __init__() Parameter Styles
class Cruise:
    """ This class describes a cruise."""
    def __init__(self, shipname, price, room):
        self.ship = shipname
        self.cost = price
        self.cabin = room

myvacation = Cruise(shipname='Voyager', price=0, room=101)
yourvacation = Cruise('Sundowner', 157.50, 511)
print(myvacation.ship, myvacation.cabin, myvacation.cost)
print(yourvacation.ship, yourvacation.cabin, yourvacation.cost)

# Modifying Instance Attributes
myvacation.cost = 400.0
myvacation.cabin = 104
print(myvacation.ship, myvacation.cabin, myvacation.cost)
print(yourvacation.ship, yourvacation.cabin, yourvacation.cost)


# Methods
class Cruise:
    """ This class describes a cruise."""
    def __init__(self, ship=None, cost=0.0, cabin=0):
        self.ship = ship
        self.cost = cost
        self.cabin = cabin

    def dine(self, amount):
        self.cost += amount

myvacation = Cruise(ship='Voyager', cabin=101)
yourvacation = Cruise(ship='Sundowner',
                      cost=157.50, cabin=511)
myvacation.dine(125.0)
yourvacation.dine(215.50)
print('myvacation', myvacation.cost)
print('yourvacation', yourvacation.cost)

# Class Attributes
class Cruise:
    """ This class describes a cruise."""

    premiumcabins = (101, 102, 105, 106, 109, 110)

    def __init__(self, ship=None, cost=0.0, cabin=0):
        self.ship = ship
        self.cost = cost
        self.cabin = cabin
        self.charge_upgrade()

    def charge_upgrade(self):
        if self.cabin in Cruise.premiumcabins:
            self.cost += 50.0

myvacation = Cruise(ship='Voyager', cabin=101)
print(myvacation.cost)