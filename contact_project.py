
contacts = []
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            for contact in contacts:
                print("\nName:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("Address:", contact["address"])

    elif choice == "3":
        search = input("Enter name or phone number: ")
        found = False

        for contact in contacts:
            if search.lower() == contact["name"].lower() or search == contact["phone"]:
                print("\nName:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("Address:", contact["address"])
                found = True

        if not found:
            print("Contact not found.")

    elif choice == "4":
        search = input("Enter name of contact to update: ")
        found = False

        for contact in contacts:
            if search.lower() == contact["name"].lower():
                contact["phone"] = input("Enter new phone: ")
                contact["email"] = input("Enter new email: ")
                contact["address"] = input("Enter new address: ")
                print("Contact updated successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "5":
        search = input("Enter name of contact to delete: ")
        found = False

        for contact in contacts:
            if search.lower() == contact["name"].lower():
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Please try again.")


 