from tkinter import *
from gui.viewtgui import ViewTripGui


class ViewAllTripFrame(Frame):
    def __init__(self, container, travelsystem):
        super().__init__(container)
        self.tripviews = []
        # configure the root window
        # self.__add_name_label()
        # self.__add_name_entry()
        print(travelsystem.trips)
        self.travelsystem = travelsystem
        re_button = Button(self)
        re_button.grid(row=0, column=1, columnspan=2)
        re_button.configure(text="Refresh")
        re_button.bind("<ButtonRelease-1>", self.refresh)

        for i in range(len(travelsystem.trips)):
            trip = travelsystem.trips[i]
            print(trip)
            tripframe = ViewTripGui(self, trip, travelsystem, i)
            tripframe.grid(row=i+1, column=0)
            self.tripviews.append(tripframe)
    def refresh(self, event):
        for tripview in self.tripviews:
            # tripview.grid_forget()
            tripview.destroy()
        self.tripviews = []
        for i in range(len(self.travelsystem.trips)):
            trip = self.travelsystem.trips[i]
            print(trip)
            tripframe = ViewTripGui(self, trip, self.travelsystem, i)
            tripframe.grid(row=i+1, column=0)
            self.tripviews.append(tripframe)



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
