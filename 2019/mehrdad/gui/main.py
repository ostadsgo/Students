import phonebook
import os

contact = phonebook.Phonebook()

def display_menu():
        menu_items = [
            "Add Contact",
            "Edit Contact",
            "Delete Contact",
            "Find Contact",
            "Display Contact",
            "Exit",
        ]

        for index, item in enumerate(menu_items):
            print(f"[{index+1}] {item}")

operations = {
    "1": contact.add,
    "2": contact.edit,
    "3": contact.delete,
    "4": contact.find,
    "5": contact.display,
    "6": exit,
    }

while True:
    os.system('clear')

    display_menu()
    response = input("Choice from menu...\n> ")
    
    if operations.get(response) is not None:
        operations[response]()
    else:
        print("Wrong Choice")
    
    input('Press any to back to menu...')
