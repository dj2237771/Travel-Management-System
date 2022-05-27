from tkinter import*

class TripGui(Tk):

    def __init__(self):
        super().__init__()

        self.__add_heading_label("Trip Gui")
        self.configure(padx=10,pady=10)

        self.__add_name_label()
        self.__add_name_entry()

        self.__add_start_date_label()
        self.__add_start_date_entry()

        self.__add_end_date_label()
        self.__add_end_date_entry()

        self.__add_traveller_list_label()
        self.__add_traveller_list_entry()

        self.__add_trip_leg_label()
        self.__add_trip_leg_entry()

        self.__add_support_staff_label()
        self.__add_support_staff_entry()

        self.__add_trip_coordinator_label()
        self.__add_trip_coordinator_entry()

        self.__add_trip_manager_label()
        self.__add_trip_manager_entry()

    def __add_heading_label(self):
        self.name_label = Label()
        self.name_label.grid(row=0, column=0)

    def ___add_name_label(self):
        self.name_label = Label()
        self.name_label.grid(row=1, column=0)

    def ___add_name_entry(self):
        self.name_entry = Entry()
        self.name_entry.grid(row=1, column=1)

    def __add_start_date_label(self):
        self.start_date_label = Label()
        self.start_date_label.grid(row=2, column=0)

    def __add_start_date_entry(self):
        self.start_date_entry = Entry()
        self.start_date_entry.grid(row=2, column=1)

    def __add_end_date_label(self):
        self.end_date_label = Label()
        self.end_date_label.grid(row=3, column=0)

    def __add_end_date_entry(self):
        self.end_date_entry = Entry()
        self.end_date_entry.grid(row=3, column=1)

    def __add_traveller_list_label(self):
        self.traveller_list_label = Label()
        self.traveller_list_label.grid(row=4, column=0)

    def __add_traveller_list_entry(self):
        self.traveller_list_entry = Entry()
        self.traveller_list_entry.grid(row=4, column=1)

    def __add_trip_leg_label(self):
        self.trip_leg_label = Label()
        self.trip_leg_label.grid(row=5, column=0)

    def __add_trip_leg_entry(self):
        self.trip_leg_entry = Entry()
        self.trip_leg_entry.grid(row=5, column=1)

    def __add_support_staff_label(self):
        self.support_staff_label = Label()
        self.support_staff_label.grid(row=6, column=0)

    def __add_support_staff_entry(self):
        self.support_staff_entry = Entry()
        self.support_staff_entry.grid(row=6, column=1)

    def __add_trip_coordinator_label(self):
        self.trip_coordinator_label = Label()
        self.trip_coordinator_label.grid(row=6, column=0)

    def __add_trip_coordinator_entry(self):
        self.trip_coordinator_entry = Entry()
        self.trip_coordinator_entry.grid(row=7, column=1)

    def __add_trip_manager_label(self):
        self.trip_manager_label = Label()
        self.trip_manager_label.grid(row=8, column=0)

    def __add_trip_manager_entry(self):
        self.trip_manager_entry = Entry()
        self.trip_manager_entry.grid(row=8, column=1)

if __name__ == "__main__":
    trip_gui = TripGui()
    trip_gui.mainloop()
