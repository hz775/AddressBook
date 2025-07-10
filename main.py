from addressbook import AddressBook
from contact import Contact

if __name__ == "__main__":
    # UC1: Create AddressBook object
    book1 = AddressBook()

    # UC2:adding contact
    book1.add_contact()


    # UC3 edit contact
    book1.edit_contact("sai")

    # UC4 delete contact
    book1.delete_contact()

    # UC5 adding multiple contact
    book1.add_multiple_contacts()
    book1.display_all_contacts()
