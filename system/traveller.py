import pprint


class Traveller:
    def __init__(self, name, address, date_of_birth, emergency_contact):
        self.name = name
        self.address = address
        self.date_of_birth = date_of_birth
        self.emergency_contact = emergency_contact

    def __str__(self):
        return pprint.pformat(vars(self), indent=4, width=1)

    def __repr__(self):
        return pprint.pformat(vars(self), indent=4, width=1)


class ID(Traveller):
    def __init__(self, name, address, date_of_birth, emergency_contact, id_number):
        super().__init__(name, address, date_of_birth, emergency_contact)
        self.id_number = id_number


class Passport(ID):
    def __init__(self, name, address, date_of_birth, id_number):
        super().__init__(id_number)


class Licence(ID):
    def __init__(self, name, address, date_of_birth, id_number):
        super().__init__(id_number)


class National(ID):
    def __init__(self, name, address, date_of_birth, id_number):
        super().__init__(id_number)
