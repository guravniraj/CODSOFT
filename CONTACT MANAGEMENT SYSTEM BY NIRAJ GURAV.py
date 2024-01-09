# Contact Management System created by Niraj Gurav

contacts = []

def add_contact():
    print("\nEnter contact details:")
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")

    contact = {
        'Name': name,
        'Phone Number': phone_number,
        'Email': email,
        'Address': address
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['Name']}, Phone Number: {contact['Phone Number']}")

def search_contact():
    search_term = input("\nEnter name or phone number to search: ")
    found = False

    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone Number']:
            print("\nContact Found:")
            print(f"Name: {contact['Name']}")
            print(f"Phone Number: {contact['Phone Number']}")
            print(f"Email: {contact['Email']}")
            print(f"Address: {contact['Address']}")
            found = True

    if not found:
        print("Contact not found.")

def update_contact():
    search_term = input("\nEnter name or phone number of contact to update: ")
    found = False

    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone Number']:
            print("\nContact Found. Enter new details:")
            contact['Name'] = input("Name: ")
            contact['Phone Number'] = input("Phone Number: ")
            contact['Email'] = input("Email: ")
            contact['Address'] = input("Address: ")
            print("Contact updated successfully!")
            found = True

    if not found:
        print("Contact not found.")

def delete_contact():
    search_term = input("\nEnter name or phone number of contact to delete: ")
    found = False

    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone Number']:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            found = True

    if not found:
        print("Contact not found.")

while True:
    print("\nContact Management System - By Niraj Gurav")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Thank you. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")