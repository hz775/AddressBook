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

                        





