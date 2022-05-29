from tkinter import *
from system.traveller import Traveller


class TravellerFrame(Frame):

    def __init__(self, container, travel_system):
        super().__init__(container)
        self.traveler_list = []
        self.travel_system = travel_system

        self.__add_heading_label()

        self.__add_name_label()
        self.__add_name_entry()

        self.__add_address_label()
        self.__add_address_entry()

        self.__add_date_of_birth_label()
        self.__add_date_of_birth_entry()

        self.__add_emergency_contact_label()
        self.__add_emergency_contact_entry()

        self.__add_submit_button()

    def __add_heading_label(self):
        self.heading_label = Label(self)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(text="Add Traveller")

    def __add_name_label(self):
        self.name_label = Label(self)
        self.name_label.grid(row=1, column=0)
        self.name_label.configure(text="Name:")

    def __add_name_entry(self):
        self.name_entry = Entry(self)
        self.name_entry.grid(row=1, column=1)

    def __add_address_label(self):
        self.address_label = Label(self)
        self.address_label.grid(row=2, column=0)
        self.address_label.configure(text="Address:")

    def __add_address_entry(self):
        self.address_entry = Entry(self)
        self.address_entry.grid(row=2, column=1)

    def __add_date_of_birth_label(self):
        self.date_of_birth_label = Label(self)
        self.date_of_birth_label.grid(row=3, column=0)
        self.date_of_birth_label.configure(text="Date of birth:")

    def __add_date_of_birth_entry(self):
        self.date_of_birth_entry = Entry(self)
        self.date_of_birth_entry.grid(row=3, column=1)

    def __add_emergency_contact_label(self):
        self.emergency_contact_label = Label(self)
        self.emergency_contact_label.grid(row=4, column=0)
        self.emergency_contact_label.configure(text="Emergency Contact:")

    def __add_emergency_contact_entry(self):
        self.emergency_contact_entry = Entry(self)
        self.emergency_contact_entry.grid(row=4, column=1)

    def __add_submit_button(self):
        self.submit_button = Button(self)
        self.submit_button.grid(row=5, column=1, columnspan=2)
        self.submit_button.configure(text="Add Traveller")
        self.submit_button.bind("<ButtonRelease-1>", self.__submit_clicked)

    def __submit_clicked(self, event):
        name = self.name_entry.get()
        address = self.address_entry.get()
        date_of_birth = self.date_of_birth_entry.get()
        emergency_contact = self.emergency_contact_entry.get()

        traveller = Traveller(name, address, date_of_birth, emergency_contact)
        self.traveler_list.append(traveller)




if __name__ == "__main__":
    traveller_gui = TravellerFrame()
    traveller_gui.mainloop()
