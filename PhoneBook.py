import datetime

from Contact import Contact
import time
import csv

from Log import Log


class PhoneBook:
    def create_contact(self, list, logs):
        """Choose a way to create new contact"""
        print('\n-----Creating New Contact-----')
        num = input('-----Enter 1 to create contact individually:\n'
                    '-----Enter 2 to create contacts by batch:\n')
        if num == '1':
            self.create_contact_individually(list, logs)
        elif num == '2':
            self.create_contacts_by_batch(list, logs)

    def create_contact_individually(self, list, logs):
        """Create contact individually by entering information"""
        phone_number = input('-----Enter phone number of the contact:\n')
        # validate the phone number by validate_phone_number() function
        while self.validate_phone_number(phone_number, list) == 'Format Error':
            phone_number = input('-----Phone Number has a wrong format. '
                                 'Please Enter phone number of the contact again:\n')
        if self.validate_phone_number(phone_number, list) == 'Exists':
            print('Contact already exists.')
            return
        first_name = input('-----Enter first name of the contact:\n')
        last_name = input('-----Enter last name of the contact:\n')
        # get local time in the format of datetime
        created_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        updated_time = created_time
        new_contact = Contact(first_name, last_name, phone_number, created_time, updated_time)
        # Make a new log when an operation is submitted. Same to other operations.
        new_log = Log('Create', first_name+' '+last_name, created_time)
        list.append(new_contact)
        logs.append(new_log)
        print('Created new contact successfully!')

    def create_contacts_by_batch(self, list, logs):
        """
        Create contacts by batch by importing a CSV file located in a particular position.
        For example, contacts info is at D disk here.
        """
        with open('D:/contacts.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                phone_number = row[2]
                while self.validate_phone_number(phone_number, list) == 'Format Error':
                    print(phone_number)
                    phone_number = input('-----Phone Number has a wrong format. '
                                         'Please Enter phone number of the contact again:\n')
                if self.validate_phone_number(phone_number, list) == 'Exists':
                    print('Contact already exists.')
                    continue
                first_name = row[0]
                last_name = row[1]
                created_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                updated_time = created_time
                new_contact = Contact(first_name, last_name, phone_number, created_time, updated_time)
                new_log = Log('Create', first_name+' '+last_name, created_time)
                list.append(new_contact)
                logs.append(new_log)
            print('Created new contacts successfully!')

    def validate_phone_number(self, phone_number, list):
        """Validate the phone number in two aspects. The format and the existence."""
        if len(phone_number) != 14:  # The length of a phone number must be 14.
            return 'Format Error'
        if (phone_number[0] != '(' or phone_number[4] != ')' or phone_number[5] != ' '
                or phone_number[9] != '-'):  # There must be brackets, space and hyphen in specific position.
            return 'Format Error'
        for contact in list:
            if phone_number == contact.phone_number:
                return 'Exists'
        return 'Correct'

    def view_contacts(self, list):
        """
        View contacts while alphabetical sorting contacts
        and grouping contacts according to the initial letter of first name.
        """
        print('\n-----Viewing Contacts-----')
        print('First Name            Last Name            Phone Number')
        list.sort(key=lambda x: x.first_name)  # alphabetical sorting according to first name
        print('A-H')  # grouping by specific range of letters
        for contact in list:
            if 'A' <= contact.first_name[0] <= 'K':
                print(contact)
        print('\nI-P')
        for contact in list:
            if 'I' <= contact.first_name[0] <= 'P':
                print(contact)
        print('\nQ-Z')
        for contact in list:
            if 'Q' <= contact.first_name[0] <= 'Z':
                print(contact)

    def search_contact_by_name(self, list):
        """Search a contact by name."""
        first_name = input('-----Enter the First Name of contact:\n')
        last_name = input('-----Enter the Last Name of contact:\n')
        # Use a flag to handle possible situation of no results. Same to functions below.
        flag = False
        print('\n-------------------------------------------------------')
        print('First Name            Last Name            Phone Number')
        for contact in list:
            if (contact.first_name.__contains__(first_name)
                    and contact.last_name.__contains__(last_name)):
                print(contact)
                flag = True
        if not flag:
            print('No results.')

    def search_contact_by_phone_number(self, list):
        """Search a contact by phone number."""
        phone_number = input('-----Enter the Phone Number of contact:\n')
        flag = False
        print('\n-------------------------------------------------------')
        print('First Name            Last Name            Phone Number')
        for contact in list:
            if contact.phone_number.__contains__(phone_number):
                print(contact)
                flag = True
        if not flag:
            print('No results.')

    def search_contact_by_period(self, list):
        """Search contacts by a specific period."""
        # Convert inputted string type into datetime type to make it easier for comparing.
        period_from_str = input('-----Enter the beginning of the period: (yyyy-MM-dd HH:mm:ss)\n')
        period_from = datetime.datetime.strptime(period_from_str, '%Y-%m-%d %H:%M:%S')
        period_to_str = input('-----Enter the end of the period: (yyyy-MM-dd HH:mm:ss)\n')
        period_to = datetime.datetime.strptime(period_to_str, '%Y-%m-%d %H:%M:%S')
        flag = False
        for contact in list:
            contact_date = datetime.datetime.strptime(contact.created_time, '%Y-%m-%d %H:%M:%S')
            if period_from <= contact_date <= period_to:
                print(contact)
                flag = True
        if not flag:
            print('No results.')

    def search_contact(self, list):
        """Choose a way to search contacts."""
        print('\n-----Searching Contact-----')
        num = input('-----Enter 1 to search contact by Name:\n'
                    '-----Enter 2 to search contact by Phone Number:\n'
                    '-----Enter 3 to search contact by Period:\n')
        if num == '1':
            self.search_contact_by_name(list)
        elif num == '2':
            self.search_contact_by_phone_number(list)
        elif num == '3':
            self.search_contact_by_period(list)

    def update_contact(self, list, logs):
        """Update contacts for different parameters."""
        print('\n-----Updating Contact-----')
        phone_number = input('-----Enter the Phone Number of contact that needed updating:\n')
        flag = False
        print('\n-------------------------------------------------------')
        print('First Name            Last Name            Phone Number')
        first_name = ''
        last_name = ''
        for contact in list:
            if contact.phone_number == phone_number:
                print(contact)
                created_time = contact.created_time
                first_name = contact.first_name
                last_name = contact.last_name
                flag = True
                contact.phone_number = 'target'
        if not flag:
            print('No results.')
            return

        will_change_phone_number = input('-----Do you want to change the Phone Number? (y/n)\n')
        if will_change_phone_number == 'y':
            phone_number = input('-----Enter new phone number of the contact:\n')
            while self.validate_phone_number(phone_number, list) == 'Format Error':
                phone_number = input('-----Phone Number has a wrong format. '
                                     'Please Enter phone number of the contact again:\n')
            if self.validate_phone_number(phone_number, list) == 'Exists':
                print('Contact already exists.')
                return
        will_change_first_name = input('-----Do you want to change the First Name? (y/n)\n')
        if will_change_first_name == 'y':
            first_name = input('-----Enter new first name of the contact:\n')

        will_change_last_name = input('-----Do you want to change the Last Name? (y/n)\n')
        if will_change_last_name == 'y':
            last_name = input('-----Enter new last name of the contact:\n')

        updated_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        for contact in list:
            if contact.phone_number == 'target':
                contact.phone_number = phone_number
                contact.first_name = first_name
                contact.last_name = last_name
                contact.updated_time = updated_time
                if will_change_phone_number == 'y':
                    new_log = Log('Update_Phone_Number', contact.first_name+' '+contact.last_name,
                                  updated_time)
                    logs.append(new_log)
                if will_change_first_name == 'y':
                    new_log = Log('Update_First_Name', contact.first_name+' '+contact.last_name,
                                  updated_time)
                    logs.append(new_log)
                if will_change_last_name == 'y':
                    new_log = Log('Update_Last_Name', contact.first_name+' '+contact.last_name,
                                  updated_time)
                    logs.append(new_log)
        print('Updated contact successfully!')

    def delete_contact(self, list, logs):
        """Delete an existed contact or delete contacts in batch."""
        print('\n-----Deleting Contact-----')
        phone_number_str = input('-----Enter all the Phone Numbers of contacts which need to be deleted '
                                 "(separated with a single ',' ):\n")
        flag = False
        print('\n-------------------------------------------------------')
        print('First Name            Last Name            Phone Number')
        phone_numbers = phone_number_str.split(',')
        for phone_number in phone_numbers:
            for contact in list:
                if contact.phone_number == phone_number:
                    print(contact)
                    flag = True
        if not flag:
            print('No results.')
            return
        will_delete = input('Are you sure to delete contacts above? (y/n)\n')
        if will_delete == 'y':
            for phone_number in phone_numbers:
                for contact in list:
                    if contact.phone_number == phone_number:
                        list.remove(contact)
                        new_log = Log('Delete', contact.first_name+' '+contact.last_name,
                                      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                        logs.append(new_log)
            print('Deleted contacts successfully!')

    def view_logs(self, logs):
        """View all logs of the application or check logs related to a individual contact."""
        print('\n-----Viewing Logs-----')
        num = input('-----Enter 1 to view all logs:\n'
                    '-----Enter 2 to view logs about a individual contact:\n')
        if num == '1':
            print('\n-------------------------------------------------------')
            print('Operation            Contact Name            Timestamp')
            for log in logs:
                print(log)
        elif num == '2':
            name = input('-----Enter full name of the contact:\n')
            print('\n-------------------------------------------------------')
            print('Operation            Timestamp')
            for log in logs:
                if log.contact == name:
                    print(log.operation + '            ' + log.timestamp)



