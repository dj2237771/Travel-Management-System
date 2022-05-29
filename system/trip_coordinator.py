class TripCoordinator:
    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password

    def create_traveller(self):

    def view_traveller(self):

    def update_traveller(self):

    def view_trip_leg(self):

    def create_trip_leg(self):

    def update_trip_leg(self):


    def create_itinerary(self):

    def take_payment(self):

    def print_recites(self):


class TripManager(TripCoordinator):
    def __init__(self, name, user, password):
        super().__init__(self, name, user, password)
    def create_trip_coordinator(self):

    def viw_trip_coordinator(self):

    def update_trip_coordinator(self):

    def delete_trip_coordinator(self):

    def view_trip(self):

    def create_trip(self):

    def update_trip(self):

    def total_invoice(self):

class Administrator(TripCoordinator):
    def __init__(self, name, user, password):
        super().__init__(self, name, user, password)
    def create_trip_manager(self):

    def viw_trip_manager(self):

    def update_trip_manager(self):

    def delete_trip_manager(self):

    def view_trip_invoice(self):

    def view_trip_payment(self):

    def delete_trip_payment(self):

    def invoice_all_trip(self):

    def payment_all_trip(self):


