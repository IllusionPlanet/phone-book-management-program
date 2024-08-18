from Contact import Contact
import csv

class InitialContacts:
    def init_contacts(self):
        """Initialize the contact information"""
        list = []
        with open('D:/initialized_contacts.csv', 'r') as file:
            reader = csv.reader(file)  # reader here is a 2D list representing all info of contacts
            for row in reader:
                phone_number = row[2]
                first_name = row[0]
                last_name = row[1]
                created_time = row[3]
                updated_time = created_time
                new_contact = Contact(first_name, last_name, phone_number, created_time, updated_time)
                list.append(new_contact)
        return list
