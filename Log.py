class Log:
    def __init__(self, operation, contact, timestamp):
        self.operation = operation
        self.contact = contact
        self.timestamp = timestamp

    def __str__(self):
        """Connect all the properties of a log object together when being printed"""
        return ('%s            %s            %s            ' %
                (self.operation, self.contact, self.timestamp))