import pickle
import os

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

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

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nContacts:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact.name} - {contact.phone_number}")

def create_contact():
    print("Create Contact")
    name = input("Enter Name: ")
    phone_number = input("Enter Handphone Number: ")

    return Contact(name, phone_number)

def update_contact(contact):
    print("\nUpdate Contact:")
    print("Leave the field blank if you don't want to change it.")
    
    name = input(f"Enter Name [{contact.name}]: ") or contact.name
    phone_number = input(f"Enter Handphone Number [{contact.phone_number}]: ") or contact.phone_number

    return Contact(name, phone_number)

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
        print("2. Create Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("E. Exit")

        choice = input("Enter your choice: ").upper()

        if choice == "1":
            os.system('cls')
            display_contacts(contacts)

        elif choice == "2":
            os.system('cls')
            new_contact = create_contact()
            contacts.append(new_contact)
            save_contacts(contacts)
            print("Contact created successfully.")

        elif choice == "3":
            os.system('cls')
            display_contacts(contacts)
            if contacts:
                index = int(input("Enter the index of the contact to update: "))
                try:
                    updated_contact = update_contact(contacts[index - 1])
                    contacts[index - 1] = updated_contact
                    save_contacts(contacts)
                    print("Contact updated successfully.")
                except IndexError:
                    print("Invalid index.")

        elif choice == "4":
            os.system('cls')
            display_contacts(contacts)
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