"""
Exercise 6.1 reservationclass.py
"""


class Reservation:
    def __init__(self, name=None, reservationid=None, flightref=None):
        self.name = name
        self.reservationid = reservationid
        self.flightref = flightref
