from addressbook import AddressBook
from collections import defaultdict

class AddressBookManager:
    def __init__(self):
        self.books = {}  

    def create_book(self):
        name = input("Enter a unique name for the new address book: ").strip()
        if name in self.books:
            print(f"'{name}' already exists.")
        else:
            self.books[name] = AddressBook()
            print(f"Address Book '{name}' created.")

    def list_books(self):
        if not self.books:
            print("No address books found.")
        else:
            print("Address Books:")
            for name in self.books:
                print(f" - {name}")

    def use_book(self):
        self.list_books()
        name = input("Enter the name of the book to manage: ").strip()
        if name in self.books:
            self.manage_book(self.books[name])
        else:
            print(f"No book found with the name '{name}'.")

    # here book reperesents the name of book to manage
    def manage_book(self, book):    
        while True:
            print("\nManage Address Book:")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Back")
            choice = input("Choice: ")

            match choice:
                case "1": book.add_contact()
                case "2": book.view_contacts()
                case "3": break
                case _: print("Invalid choice.")

    def search_person_by_city_or_state(self):
        if not self.books:
            print("No Address Books available.")
            return

        search_field = input("Would you like to search by 'city' or 'state'?: ").strip().lower()
        if search_field not in ("city", "state"):
            print("Invalid choice. Please enter either 'city' or 'state'.")
            return

        value = input(f"Enter the {search_field.title()} name to search for: ").strip().lower()
        found = False

        for book_name, book in self.books.items():
            matching_contacts = [
                contact for contact in book.contacts
                if (search_field == "city" and contact.city.lower() == value) or
                (search_field == "state" and contact.state.lower() == value)
            ]

            if matching_contacts:
                print(f"\n Found in Address Book: {book_name}")
                for contact in matching_contacts:
                    contact.display_contact()
                    print("-" * 30)
                found = True

        if not found:
            print(f"\nNo contacts found in {search_field.title()} '{value.title()}'.")

    

    def view_persons_by_city_or_state(self):
        if not self.books:
            print("No Address Books available.")
            return

        # Create two dictionaries to map City and State to list of Contacts
        city_dict = defaultdict(list)
        state_dict = defaultdict(list)


        for book_name, book in self.books.items():
            for contact in book.contacts:
                city_dict[contact.city].append(contact)
                state_dict[contact.state].append(contact)

        option = input("View persons by 'city' or 'state'?: ").strip().lower()
        if option == "city":
            for city, contacts in city_dict.items():
                print(f"\nCity: {city}")
                for contact in contacts:
                    contact.display_contact()
                    print("-" * 30)
        elif option == "state":
            for state, contacts in state_dict.items():
                print(f"\nState: {state}")
                for contact in contacts:
                    contact.display_contact()
                    print("-" * 30)
        else:
            print("Invalid choice. Please enter either 'city' or 'state'.")

    def count_persons_by_city_or_state(self):
        option = input("Count persons by 'city' or 'state'?: ").strip().lower()
        if option not in ("city", "state"):
            print("Invalid choice. Please enter 'city' or 'state'.")
            return

        name = input(f"Enter the {option.title()} name: ").strip()

        persons = [
            contact for book in self.books.values() for contact in book.contacts
            if (option == "city" and contact.city.lower() == name.lower()) or
            (option == "state" and contact.state.lower() == name.lower())
        ]

        if not persons:
            print(f"No persons found in {option.title()} '{name.title()}'.")
            return

        print(f"\nTotal number of persons in {option.title()} '{name.title()}': {len(persons)}\n")

        print("Contact Numbers:")
        for person in persons:
            print(f"{person.first_name} {person.last_name} - {person.phone_number}")

    

