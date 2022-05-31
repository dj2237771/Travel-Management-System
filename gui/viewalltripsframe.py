from tkinter import *
from gui.viewtgui import ViewTripGui


class ViewAllTripFrame(Frame):
    def __init__(self, container, travelsystem):
        super().__init__(container)
        # configure the root window
        # self.__add_name_label()
        # self.__add_name_entry()
        print(travelsystem.trips)
        for i in range(len(travelsystem.trips)):
            trip = travelsystem.trips[i]
            print(trip)
            tripframe = ViewTripGui(self, trip)
            tripframe.grid(row=i, column=0)



    # def __add_name_label(self):
    #     self.name_label = Label(self)
    #     self.name_label.grid(row=1, column=0)
    #     self.name_label.configure(text="Name:")
    #
    # def __add_name_entry(self):
    #     self.name_entry = Entry(self)
    #     self.name_entry.delete(0, END)
    #     self.name_entry.insert(0, self.trip.name)
    #     self.name_entry.grid(row=1, column=1)
