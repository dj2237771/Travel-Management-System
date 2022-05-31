from tkinter import *


class ViewTripGui(Frame):
    def __init__(self, container, trip):
        super().__init__(container)
        # configure the root window
        self.trip = trip
        self.__add_name_label()
        self.__add_name_entry()

    def __add_name_label(self):
        self.name_label = Label(self)
        self.name_label.grid(row=1, column=0)
        self.name_label.configure(text="Name:")

    def __add_name_entry(self):
        self.name_entry = Entry(self)
        self.name_entry.delete(0,END)
        self.name_entry.insert(0,self.trip.name)
        self.name_entry.grid(row=1, column=1)

