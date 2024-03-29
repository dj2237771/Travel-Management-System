import json
from os.path import exists

from system.traveller import Traveller
from system.trip import Trip
from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__


class TravelSystem:

    def __init__(self):
        self.trips = []
        self.loaddata()

    def addtrip(self, name, start_date, end_date, traveller_list, trip_leg, trip_support, trip_coordinator,
                trip_manager):
        trip = Trip(name, start_date, end_date, traveller_list, trip_leg, trip_support, trip_coordinator, trip_manager)
        self.trips.append(trip)
        self.savedata()

    def savedata(self):
        with open('data.json', 'w') as f:
            json.dump(self, f, cls=MyEncoder)

    def loaddata(self):
        if exists("data.json"):
            with open("data.json") as f:
                data = json.load(f)

                for trip in data["trips"]:

                    travellers = []
                    for traveller in trip["traveller_list"]:
                        travellers.append(Traveller(traveller["name"], traveller["address"], traveller["date_of_birth"],
                                                    traveller["emergency_contact"]))
                    self.trips.append(
                        Trip(trip["name"], trip["start_date"], trip["end_date"], travellers, trip["trip_leg"],
                             trip["trip_support"],
                             trip["trip_coordinator"], trip["trip_manager"]))

    def deletetrip(self, index):
        del self.trips[index]

    def modifytrip(self, index, name, start_date, end_date, traveller_list, trip_leg, trip_support, trip_coordinator,
                   trip_manager):
        self.trips[index].name = name
        self.trips[index].start_date = start_date
        self.trips[index].end_date = end_date
        self.trips[index].traveller_list = traveller_list
        self.trips[index].trip_leg = trip_leg
        self.trips[index].trip_support = trip_support
        self.trips[index].trip_coordinator = trip_coordinator
        self.trips[index].trip_manager = trip_manager
