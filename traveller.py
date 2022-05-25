class Traveller:
    def __init__(self, name, address, date_of_birth, emergency_contact):
        self.name = name
        self.address = address
        self.date_of_birth = date_of_birth
        self.emergency_contact = emergency_contact


class ID(Traveller):
    def __init__(self, name, id_number):
        super().__init__(name)
        self.id_number = id_number

class Passport(ID):
    def __init__(self, id_number):
        super().__init__(id_number)



