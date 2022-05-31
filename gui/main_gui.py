from tkinter import *
from tkinter import ttk

from system.trip import Trip
from gui.traveller_gui import TravellerFrame
from gui.logingui import LoginFrame
from gui.viewalltripsframe import ViewAllTripFrame
from system.travelsystem import TravelSystem
from gui.trip_gui import TripFrame
import pprint

class App(Tk):
    def __init__(self, trip_system):
        super().__init__()
        # configure the root window
        self.title('Travel system')
        self.geometry('500x500')
        self.trip_system = trip_system


if __name__ == "__main__":
    travellsystem = TravelSystem()
    app = App(travellsystem)
    tab_parent = ttk.Notebook(app)

    frame1 = LoginFrame(tab_parent, tab_parent)
    frame2 = TripFrame(tab_parent, travellsystem)
    frame3 = ViewAllTripFrame(tab_parent, travellsystem)
    tab_parent.add(frame1, text="Login")
    tab_parent.add(frame2, text="Add Trip", state="disable")
    tab_parent.add(frame3, text="View all Trips", state="disable")
    tab_parent.grid()
    app.mainloop()

