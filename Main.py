from InitialContacts import InitialContacts
from PhoneBook import PhoneBook

if __name__ == '__main__':
    initial_contacts = InitialContacts()
    list = initial_contacts.init_contacts()
    logs = []
    phone_book = PhoneBook()

    while True:
        print('\n')
        print('================================================')
        print('=====Phone Book Management Application v1.0=====')
        print('================================================')
        print('-----Enter 1 To View All Contacts-----')
        print('-----Enter 2 To Add New Contact-----')
        print('-----Enter 3 To Search Contact-----')
        print('-----Enter 4 To Update Contact-----')
        print('-----Enter 5 To Delete Contact-----')
        print('-----Enter 6 To View Log-----')
        print('-----Enter 0 To Exit The Application-----')
        num = input()
        if num == '1':
            phone_book.view_contacts(list)
        if num == '2':
            phone_book.create_contact(list, logs)
        if num == '3':
            phone_book.search_contact(list)
        if num == '4':
            phone_book.update_contact(list, logs)
        if num == '5':
            phone_book.delete_contact(list, logs)
        if num == '6':
            phone_book.view_logs(logs)
        if num == '0':
            exit(0)

        input('\n-----Press Enter to continue')



