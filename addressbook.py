from contact import Contact

class AddressBook:
    def __init__(self): 
        self.contacts = []

    def add_contact(self): 
        print("\nEnter your contact details: ")
        fields = ["First Name", "Last Name", "Address", "City", "State", "Zip Code", "Phone Number", "Email"]
        user_input = [input(f"{field}: ") for field in fields]
        first_name, last_name = user_input[0], user_input[1]

        if any(c.first_name.lower() == first_name.lower() and c.last_name.lower() == last_name.lower() for c in self.contacts):
            print("\n Duplicate contact. A person with this name already exists.")
            return


        contact = Contact(*user_input)
        self.contacts.append(contact)
        print("Contact added successfully")

    def edit_contact(self, name_to_edit):
        for contact in self.contacts:
            if contact.first_name.lower() == name_to_edit.lower():
                print(f"\nContact found. Enter new details:")
                contact.first_name = input(f"First Name ({contact.first_name}): ") or contact.first_name
                contact.last_name = input(f"Last Name ({contact.last_name}): ") or contact.last_name
                contact.address = input(f"Address ({contact.address}): ") or contact.address
                contact.city = input(f"City ({contact.city}): ") or contact.city
                contact.state = input(f"State ({contact.state}): ") or contact.state
                contact.zip_code = input(f"Zip Code ({contact.zip_code}): ") or contact.zip_code
                contact.phone_number = input(f"Phone Number ({contact.phone_number}): ") or contact.phone_number
                contact.email = input(f"Email ({contact.email}): ") or contact.email

                print("\n Contact updated successfully:")
                contact.display_contact()
                return
        
        print("Contact not found.")
    
    def display_all_contacts(self):
        if not self.contacts:
            print("No contacts to display.\n")
        else:
            print("\nAll Contacts:")
            for contact in self.contacts:
                contact.display_contact()
                print("-" * 30)

    def delete_contact(self):
        print("\nDelete Contact:")
        first_name_to_delete = input("Enter First Name: ")
        last_name_to_delete = input("Enter Last Name: ")

        for person in self.contacts:
            if person.first_name == first_name_to_delete and person.last_name == last_name_to_delete:
                self.contacts.remove(person)
                print(" Contact deleted successfully.")
                return
        print(" Contact not found.")

    def add_multiple_contacts(self):
        while True:
            self.add_contact()
            cont = input("Do you want to add another contact? (y/n): ")
            if cont != "y":
                break

    def view_contacts(self):
        if not self.contacts:
            print("No contacts added")
        else:
            print("Contacts List: ")
            for contact in self.contacts:
                contact.display_contact()

    def sort_contacts_by_name(self):
        if not self.contacts:
            print("No contacts added")
            return

        sorted_contacts = sorted(self.contacts, key=lambda c: (c.first_name.lower() + " " + c.last_name.lower()))

        print("\nContacts sorted alphabetically by name:\n")
        for contact in sorted_contacts:
            contact.display_contact()
            print("-" * 30)

    def sort_contacts_by_field(self):
        if not self.contacts:
            print("No contacts to sort.")
            return

        field = input("Sort by City, State, or Zip Code? ").strip().lower()

        if field == "city":
            sorted_contacts = sorted(self.contacts, key=lambda c: c.city.lower())
        elif field == "state":
            sorted_contacts = sorted(self.contacts, key=lambda c: c.state.lower())
        elif field == "zip":
            sorted_contacts = sorted(self.contacts, key=lambda c: int(c.zip_code))
        else:
            print("Invalid field. Choose from City, State, or Zip.")
            return

        print(f"\nContacts sorted by {field.title()}:")
        for contact in sorted_contacts:
            contact.display_contact()


    def file_io(self, filename: str, action: str = "save") -> None:
        action = action.lower()
        try:
            if action == "save":
                with open(filename, "w", encoding="utf-8") as file:
                    for c in self.contacts:
                        file.write(
                            f"{c.first_name}|{c.last_name}|{c.address}|"
                            f"{c.city}|{c.state}|{c.zip_code}|"
                            f"{c.phone_number}|{c.email}\n"
                        )
                print(f" Address book saved to '{filename}'")

            elif action == "load":
                with open(filename, "r", encoding="utf-8") as file:
                    self.contacts.clear()
                    for line in file:
                        parts = line.rstrip("\n").split("|")
                        if len(parts) == 8:
                            self.contacts.append(Contact(*parts))
                        else:
                            print(f"Skipping malformed line: {line.strip()}")
                print(f" Address book loaded from '{filename}' "
                      f"({len(self.contacts)} contacts)")

            else:
                print(" Invalid action. Use 'save' or 'load'.")

        except FileNotFoundError:
            print(f" File '{filename}' not found.")
        except Exception as e:
            print(f" Error during file I/O: {e}")

        

                            





