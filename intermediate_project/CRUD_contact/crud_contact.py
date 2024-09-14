# Simple Contact Book

class ContactManager:
    def __init__(self, filename):
        self.contacts = {}
        self.filename = filename
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    name, phone, email = line.strip().split(',')
                    self.contacts[name] = {'phone': phone, 'email': email}
        except FileNotFoundError:
            # If the file doesn't exist, create an empty contacts dictionary
            self.contacts = {}

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            for name, info in self.contacts.items():
                file.write(f"{name},{info['phone']},{info['email']}\n")

    def add_contact(self, name, phone, email):
        self.contacts[name] = {'phone': phone, 'email': email}
        self.save_contacts()
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

    def search_contact(self, name):
        if name in self.contacts:
            info = self.contacts[name]
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
        else:
            print(f"Contact '{name}' not found.")

    def update_contact(self, name, phone, email):
        if name in self.contacts:
            self.contacts[name]['phone'] = phone
            self.contacts[name]['email'] = email
            self.save_contacts()
            print(f"Contact '{name}' updated successfully!")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found.")


def main():
    contact_manager = ContactManager("contacts.txt")

    while True:
        print("\nContacts Book\n")
        print("1. Add Contact")
        print("2. View Contacts List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, phone, email)
            
        elif choice == '2':
            contact_manager.view_contacts()
            
        elif choice == '3':
            name = input("Enter contact name to search: ")
            contact_manager.search_contact(name)
            
        elif choice == '4':
            name = input("Enter contact name to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            contact_manager.update_contact(name, phone, email)
            
        elif choice == '5':
            name = input("Enter contact name to delete: ")
            contact_manager.delete_contact(name)
            
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
main()