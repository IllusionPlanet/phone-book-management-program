class Contact:
    def __init__(self, first_name, last_name, phone_number, created_time, updated_time):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.created_time = created_time
        self.updated_time = updated_time

    def __str__(self):
        """Connect all the properties of a contact object together when being printed"""
        return ('%s            %s            %s            ' %
                (self.first_name, self.last_name, self.phone_number))



