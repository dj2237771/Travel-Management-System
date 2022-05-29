from system.traveller import Traveller
from system.trip import Trip


class TravelSystem:

    def __init__(self):
        self.trips = []
        self.travellers = []

    def addtrip(self, name, start_date, end_date, traveller_list, trip_leg, trip_support, trip_coordinator, trip_manager):
        trip = Trip(name, start_date, end_date, traveller_list, trip_leg, trip_support, trip_coordinator, trip_manager)
        self.trips.append(trip)

    def addtraveller(self, name, address, date_of_birth, emergency_contact):
        traveller = Traveller(name, address, date_of_birth, emergency_contact)
        self.travellers.append(traveller)
