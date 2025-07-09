from addressbook import AddressBook
from contact import Contact

if __name__ == "__main__":
    # UC1: Create AddressBook object
    book1 = AddressBook()

    # UC2: input from user and add
    book1.add_contact() 
    # UC3 edit contact
    book1.edit_contact("hemanth")
