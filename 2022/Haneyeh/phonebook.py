import os


def menu():
    print("1) Add Contact")
    print("2) Edit Contact")
    print("3) Search Contact")
    print("4) Delete Contact")
    print("5) Display Contacts")
    print("6) Exit")


def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")

    f = open("contacts.txt", "a")
    contact = f"{name}:{phone}\n"
    f.write(contact)
    print(contact[:-2], "saved successfuly.")
    f.close()


def search_contact(name):
    index = 0
    f = open("contacts.txt", "r")
    contacts = f.readlines()
    f.close()

    for contact in contacts:
        contact_name, phone = contact.split(":")
        if contact_name == name:
            return index
        index += 1

    return -1


def delete_contact(name):
    index = search_contact(name)
    f = open("contacts.txt", "r")
    contacts = f.readlines()
    f.close()
    if index != -1:
        del contacts[index]
    else:
        print("contact not found")

    f = open("contacts.txt", "w")
    for c in contacts:
        f.write(c)
    f.close()


def edit_contact(name):
    index = search_contact(name)
    f = open("contacts.txt", "r")
    contacts = f.readlines()
    f.close()
    if index != -1:
        new_name = input("New name: ")
        new_phone = input("New phone: ")
        contacts[index] = f"{new_name}:{new_phone}\n"
    else:
        print("contact not found")

    # Write again
    f = open("contacts.txt", "w")
    for c in contacts:
        f.write(c)
    f.close()


def display_contacts():
    f = open("contacts.txt", "r")
    contacts = f.readlines()
    for c in contacts:
        print(c)


while True:
    os.system("cls")
    menu()
    response = input("Choose from menu: ")
    if response == "6":
        break
    if response == "1":
        add_contact()

    if response == "2":
        pass

    if response == "3":
        name = input("Enter name to search: ")
        search_contact(name)

    if response == "4":
        name = input("Contact name to delete: ")
        delete_contact(name)

    if response == "2":
        name = input("Contact name to Edit: ")
        edit_contact(name)

    if response == "5":
        display_contacts()

    input("Press ENTER key to continue ...")
