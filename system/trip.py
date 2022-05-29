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

    def trip_cost(self):
        print(...)
        # self.Trip_cost = Trip_cost

    def __str__(self):
        return f' | name:{self.name}, travellers: {self.traveller_list} |\n '

    def __repr__(self):
        return f' | name:{self.name}, travellers: {self.traveller_list} |\n '

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
