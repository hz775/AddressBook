from addressbook import AddressBook
from contact import Contact

if __name__ == "__main__":
    # UC1: Create AddressBook object
    book1 = AddressBook()

    # UC2: input from user and add
    while True:
        book1.add_contact()
        more = input("Add another contact? (y/n): ").lower()
        if more != 'y':
            break


    book1.display_all_contacts()

    # UC3 edit contact
    book1.edit_contact("sai")
    # UC4 delete contact
    book1.delete_contact()
