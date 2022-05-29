from tkinter import *
from system.trip_coordinator import TripCoordinator


class TravellerGui(Tk):

    def __init__(self, travel_system):
        super().__init__()
        self.travel_system = travel_system

        self.__add_heading_label()

        self.__add_name_label()
        self.__add_name_entry()

        self.__add_user_label()
        self.__add_user_entry()

        self.__add_password_label()
        self.__add_password_entry()

    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(text="Add Traveller")

    def __add_name_label(self):
        self.name_label = Label()
        self.name_label.grid(row=1, column=0)
        self.name_label.configure(text="Name:")

    def __add_name_entry(self):
        self.name_entry = Entry()
        self.name_entry.grid(row=1, column=1)

    def __add_user_label(self):
        self.user_label = Label()
        self.user_label.grid(row=2, column=0)
        self.user_label.configure(text="Username:")

    def __add_user_entry(self):
        self.user_entry = Entry()
        self.user_entry.grid(row=2, column=1)

    def __add_password_label(self):
        self.password_label = Label()
        self.password_label.grid(row=3, column=0)
        self.password_label.configure(text="Date of birth:")

    def __add_password_entry(self):
        self.password_entry = Entry()
        self.password_entry.grid(row=3, column=1)

    def __add_submit_button(self):
        self.submit_button = Button()
        self.submit_button.grid(row=5, column=1, columnspan=2)
        self.submit_button.configure(text="Submit")
        self.submit_button.bind("<ButtonRelease-1>", self.__submit_clicked)

    def __submit_clicked(self, event):
        name = self.name_entry.get()
        user = self.user_entry.get()
        password = self.password_entry.get()

        trip_coordinator = TripCoordinator(name, user, password)
        self.travel_system.coordinators.append(trip_coordinator)


if __name__ == "__main__":
    traveller_gui = TravellerGui()
    traveller_gui.mainloop()
