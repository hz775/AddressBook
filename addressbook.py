from contact import Contact

class AddressBook:
    def __init__(self): 
        self.contacts = []

    def add_contact(self): 
        print("\nEnter your contact details: ")
        fields = ["First Name", "Last Name", "Address", "City", "State", "Zip Code", "Phone Number", "Email"]
        user_input = [input(f"{field}: ") for field in fields]

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
                





