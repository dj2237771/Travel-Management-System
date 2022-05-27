from enum import Enum


class TripLeg:
    def __init__(self, start_location, end_location, transport, price):
        self.location = start_location
        self.location = end_location
        self.transport = transport
        self.price = price


class Location:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Location_type(Enum):
    stay = 1
    point_of_interest = 2
    transfer_point = 3


class Transport(Enum):
    plane = 1
    ferry = 2
    coach = 3
    taxi = 4
