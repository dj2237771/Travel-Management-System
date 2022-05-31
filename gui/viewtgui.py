from tkinter import *


class ViewTripGui(Frame):
    def __init__(self, container, trip, travelsystem, index):
        super().__init__(container)
        # configure the root window

        self.travelsystem = travelsystem
        self.tripindex = index
        self.trip = trip
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
        self.__add_submit_button()
        self.__add_delete_button()

    def __add_name_label(self):
        self.name_label = Label(self)
        self.name_label.grid(row=1, column=0)
        self.name_label.configure(text="Name:")

    def __add_name_entry(self):
        self.name_entry = Entry(self)
        self.name_entry.delete(0, END)
        self.name_entry.insert(0, self.trip.name)
        self.name_entry.grid(row=1, column=1)

    def __add_start_date_label(self):
        self.start_date_label = Label(self)
        self.start_date_label.grid(row=2, column=0)
        self.start_date_label.configure(text="Start Date:")

    def __add_start_date_entry(self):
        self.start_date_entry = Entry(self)
        self.start_date_entry.delete(0, END)
        self.start_date_entry.insert(0, self.trip.start_date)
        self.start_date_entry.grid(row=2, column=1)

    def __add_end_date_label(self):
        self.end_date_label = Label(self)
        self.end_date_label.grid(row=3, column=0)
        self.end_date_label.configure(text="End Date:")

    def __add_end_date_entry(self):
        self.end_date_entry = Entry(self)
        self.end_date_entry.delete(0, END)
        self.end_date_entry.insert(0, self.trip.end_date)
        self.end_date_entry.grid(row=3, column=1)

    def __add_traveller_list_label(self):
        self.traveller_list_label = Label(self)
        self.traveller_list_label.grid(row=4, column=0)
        self.traveller_list_label.configure(text="Traveller list:")

    def __add_traveller_list_entry(self):
        self.traveller_list_entry = Entry(self)
        self.traveller_list_entry.delete(0, END)
        self.traveller_list_entry.insert(0, self.trip.traveller_list)
        self.traveller_list_entry.grid(row=4, column=1)

    def __add_trip_leg_label(self):
        self.trip_leg_label = Label(self)
        self.trip_leg_label.grid(row=5, column=0)
        self.trip_leg_label.configure(text="Trip Leg:")

    def __add_trip_leg_entry(self):
        self.trip_leg_entry = Entry(self)
        self.trip_leg_entry.delete(0, END)
        self.trip_leg_entry.insert(0, self.trip.trip_leg)
        self.trip_leg_entry.grid(row=5, column=1)

    def __add_support_staff_label(self):
        self.support_staff_label = Label(self)
        self.support_staff_label.grid(row=6, column=0)
        self.support_staff_label.configure(text="Trip Support:")

    def __add_support_staff_entry(self):
        self.support_staff_entry = Entry(self)
        self.support_staff_entry.delete(0, END)
        self.support_staff_entry.insert(0, self.trip.trip_support)
        self.support_staff_entry.grid(row=6, column=1)

    def __add_trip_coordinator_label(self):
        self.trip_coordinator_label = Label(self)
        self.trip_coordinator_label.grid(row=7, column=0)
        self.trip_coordinator_label.configure(text="Trip Coordinator:")

    def __add_trip_coordinator_entry(self):
        self.trip_coordinator_entry = Entry(self)
        self.trip_coordinator_entry.delete(0, END)
        self.trip_coordinator_entry.insert(0, self.trip.trip_coordinator)
        self.trip_coordinator_entry.grid(row=7, column=1)

    def __add_trip_manager_label(self):
        self.trip_manager_label = Label(self)
        self.trip_manager_label.grid(row=8, column=0)
        self.trip_manager_label.configure(text="Trip Manager:")

    def __add_trip_manager_entry(self):
        self.trip_manager_entry = Entry(self)
        self.trip_manager_entry.delete(0, END)
        self.trip_manager_entry.insert(0, self.trip.trip_manager)
        self.trip_manager_entry.grid(row=8, column=1)

    def __add_submit_button(self):
        self.submit_button = Button(self)
        self.submit_button.grid(row=10, column=1, columnspan=2)
        self.submit_button.configure(text="Submit")
        self.submit_button.bind("<ButtonRelease-1>", self.__submit_clicked)

    def __add_delete_button(self):
        self.submit_button = Button(self)
        self.submit_button.grid(row=10, column=3, columnspan=2)
        self.submit_button.configure(text="Delete")
        self.submit_button.bind("<ButtonRelease-1>", self.__delete_clicked)

    def __submit_clicked(self, event):
        name = self.name_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        trip_leg = self.trip_leg_entry.get()
        trip_support = self.support_staff_entry.get()
        trip_coordinator = self.trip_coordinator_entry.get()
        trip_manager = self.trip_manager_entry.get()
        self.travelsystem.modifytrip(self.tripindex, name, start_date, end_date, self.trip.traveller_list, trip_leg, trip_support,
                                     trip_coordinator,
                                     trip_manager)
        self.travelsystem.savedata()

    def __delete_clicked(self, event):
        self.travelsystem.deletetrip(self.tripindex)
        super().grid_forget()
        self.travelsystem.savedata()
        super().destroy()
