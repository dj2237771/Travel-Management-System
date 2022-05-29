from tkinter import *
from tkinter import ttk
from gui.traveller_gui import TravellerFrame
from system.main import TravelSystem
from gui.trip_gui import TripFrame

class App(Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('Travel system')
        self.geometry('500x500')


if __name__ == "__main__":
    app = App()
    travellsystem = TravelSystem()
    tab_parent = ttk.Notebook(app)

    frame2 = TripFrame(tab_parent, travellsystem)
    tab_parent.add(frame2, text="Add Trip")
    tab_parent.grid()
    app.mainloop()
