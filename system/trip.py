import pprint
import json

class Trip:

    def __init__(self, name, start_date, end_date, traveller_list, trip_leg, trip_support, trip_coordinator,
                 trip_manager):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.traveller_list = traveller_list
        self.trip_leg = trip_leg
        self.trip_support = trip_support
        self.trip_coordinator = trip_coordinator
        self.trip_manager = trip_manager

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def trip_cost(self):
        print(...)
        # self.Trip_cost = Trip_cost

    def __str__(self):
        return pprint.pformat(vars(self), indent=4, width=1)

    def __repr__(self):
        return pprint.pformat(vars(self), indent=4, width=1)
# •	Trip
# o	Name
# o	Strat date
# o	End date
# o	Travellers list
# o	Trip leg list
# o	Support staff
# o	Trip coordinator
# o	Trip manager
# o	Total cost: trip leg added up = total
# o	Remaining cost
