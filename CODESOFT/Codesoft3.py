# Contact Book
def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def add_contact(contact_list):
    print("\nAdd New Contact")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {"name": name, "phone": phone, "email": email, "address": address}

    contact_list.append(contact)
    print("Contact added successfully!")


def view_contacts(contact_list):
    print("\nContact List")
    if not contact_list:
        print("No contacts found!")
        return

    for idx, contact in enumerate(contact_list, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")


def search_contact(contact_list):
    print("\nSearch Contact")
    search = input("Enter Name or Phone Number: ")

    found_contacts = [
        c for c in contact_list if search in c["name"] or search in c["phone"]
    ]
    if not found_contacts:
        print("No matching contacts found!")
    else:
        for contact in found_contacts:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")


def update_contact(contact_list):
    print("\nUpdate Contact")
    search = input("Enter Name of the contact to update: ")

    for contact in contact_list:
        if search in contact["name"]:
            print(f"\nUpdating contact: {contact['name']}")
            contact["name"] = (
                input(f"Enter New Name (Current: {contact['name']}): ")
                or contact["name"]
            )
            contact["phone"] = (
                input(f"Enter New Phone (Current: {contact['phone']}): ")
                or contact["phone"]
            )
            contact["email"] = (
                input(f"Enter New Email (Current: {contact['email']}): ")
                or contact["email"]
            )
            contact["address"] = (
                input(f"Enter New Address (Current: {contact['address']}): ")
                or contact["address"]
            )
            print("Contact updated successfully!")
            return

    print("No matching contact found to update!")


def delete_contact(contact_list):
    print("\nDelete Contact")
    search = input("Enter Name or Phone Number of the contact to delete: ")

    for contact in contact_list:
        if search in contact["name"] or search in contact["phone"]:
            contact_list.remove(contact)
            print(f"Contact {contact['name']} deleted successfully!")
            return

    print("No matching contact found to delete!")


def main():
    contact_list = []

    while True:
        display_menu()
        choice = input("Enter your choice 1 to 6: ")

        if choice == "1":
            add_contact(contact_list)
        elif choice == "2":
            view_contacts(contact_list)
        elif choice == "3":
            search_contact(contact_list)
        elif choice == "4":
            update_contact(contact_list)
        elif choice == "5":
            delete_contact(contact_list)
        elif choice == "6":
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice,Please select a valid option.")


main()
