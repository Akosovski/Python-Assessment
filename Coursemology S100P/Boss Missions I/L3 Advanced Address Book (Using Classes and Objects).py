import pickle
import os

# contacts.pkl file will be created once upon creating the first contact
# os.system('cls') is to clear the menu so it doesn't stacks

class Contact:
    def __init__(self, first_name, last_name, phone_number, email, address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

def load_contacts():
    try:
        with open("contacts.pkl", "rb") as file:
            contacts = pickle.load(file)
    except (FileNotFoundError, EOFError):
        contacts = []
    return contacts

def save_contacts(contacts):
    with open("contacts.pkl", "wb") as file:
        pickle.dump(contacts, file)

def display_contacts_summary(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nContacts:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact.first_name} {contact.last_name}")

def display_contact_details(contact):
    print("\nContact Details:")
    print(f"First Name: {contact.first_name}")
    print(f"Last Name: {contact.last_name}")
    print(f"Phone Number: {contact.phone_number}")
    print(f"Email: {contact.email}")
    print(f"Address: {contact.address}")

def create_contact():
    print("\nCreate Contact")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")

    while True:
        try:
            phone_number = int(input("Enter Phone Number: "))
            break
        except ValueError:
            print("Error: Please enter a valid integer for the phone number.")

    email = input("Enter Email Address: ")
    address = input("Enter Address: ")

    return Contact(first_name, last_name, phone_number, email, address)

def update_contact(contact):
    print("\nUpdate Contact:")
    print("Leave the field blank if you don't want to change it.")
    
    first_name = input(f"Enter First Name [{contact.first_name}]: ") or contact.first_name
    last_name = input(f"Enter Last Name [{contact.last_name}]: ") or contact.last_name

    while True:
        try:
            print("Please enter a valid integer for the phone number.")
            phone_number = int(input(f"Enter Phone Number [{contact.phone_number}]: ")) or contact.phone_number
            break
        except ValueError:
            print("Error: Please enter a valid integer for the phone number.")

    email = input(f"Enter Email Address [{contact.email}]: ") or contact.email
    address = input(f"Enter Address [{contact.address}]: ") or contact.address

    return Contact(first_name, last_name, phone_number, email, address)

def delete_contact(contacts, index):
    try:
        del contacts[index - 1]
        print("Contact deleted successfully.")
    except IndexError:
        print("Invalid index. No contact deleted.")

def main():
    contacts = load_contacts()

    while True:
        print("\nAddress Book Menu:")
        print("1. Display Contacts")
        print("2. Display Contact Details")
        print("3. Create Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("E. Exit Program")

        choice = input("Enter your choice: ").upper()

        if choice == "1":
            os.system('cls')
            display_contacts_summary(contacts)

        elif choice == "2":
            os.system('cls')
            display_contacts_summary(contacts)
            if contacts:
                index = int(input("Enter the index of the contact to view details: "))
                try:
                    display_contact_details(contacts[index - 1])
                except IndexError:
                    print("Invalid index.")

        elif choice == "3":
            os.system('cls')
            new_contact = create_contact()
            contacts.append(new_contact)
            save_contacts(contacts)
            print("Contact created successfully.")

        elif choice == "4":
            os.system('cls')
            display_contacts_summary(contacts)
            if contacts:
                index = int(input("Enter the index of the contact to update: "))
                try:
                    updated_contact = update_contact(contacts[index - 1])
                    contacts[index - 1] = updated_contact
                    save_contacts(contacts)
                    print("Contact updated successfully.")
                except IndexError:
                    print("Invalid index.")

        elif choice == "5":
            os.system('cls')
            display_contacts_summary(contacts)
            if contacts:
                index = int(input("Enter the index of the contact to delete: "))
                delete_contact(contacts, index)
                save_contacts(contacts)

        elif choice == "E":
            print("Exiting Address Book.\n")
            break
        else:
            print("Invalid choice. Please try again.")

main()