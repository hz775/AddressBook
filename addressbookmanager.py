from addressbook import AddressBook

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
