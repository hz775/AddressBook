from addressbook import AddressBook
from addressbookmanager import AddressBookManager

if __name__ == "__main__":
    # UC1: Create AddressBook object
    # book1 = AddressBook()

    # UC2:adding contact
    # book1.add_contact()


    # UC3 edit contact
    # book1.edit_contact("sai")

    # UC4 delete contact
    # book1.delete_contact()

    # UC5 adding multiple contact
    # book1.add_multiple_contacts()
    # book1.display_all_contacts()

    # UC6 multiple address book
    manager=AddressBookManager()

    while True:
        print("\n=== Address Book System ===")
        print("1. Create New Address Book")
        print("2. Select Existing Address Book")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manager.create_book()
        elif choice == '2':
             manager.use_book()
        elif choice == '3':
            print("Exiting Address Book System.")
            break
        else:
            print("Invalid choice. Try again.")
