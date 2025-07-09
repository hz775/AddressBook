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
