import os
import csv

menu = """
.: PEOPLES DATABASE :.
----------------------
get_id | Get person by ID
scan_f | List people by FORENAME
scan_s | List people by SURNAME
exit | Exit program
----------------------"""


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def read_people():
    f = open("database.csv")
    people = list(csv.reader(f))
    return people


def search_by_id(person_id):
    people = read_people()
    for row in people:
        if person_id == row[0]:
            print("----------------------")
            print("| ID:", row[0])
            print("| FORENAME:", row[1])
            print("| SURNAME:", row[2])
            print("| GENDER:", row[3])
            print("| YEAR:", row[4])
            break


def search_by_forename(forename):
    people = read_people()
    for row in people:
        if forename == row[1]:
            print(",".join(row))


def search_by_surname(surname):
    people = read_people()
    for row in people:
        if surname == row[2]:
            print(",".join(row))


while True:
    # clear screen
    clear_screen()

    # print menu and get input from user
    print(menu)
    user_input = input("| menu > ")
    print("----------------------")

    # select action based on user input
    if user_input == "get_id":
        person_id = input("| ID = ")
        search_by_id(person_id)
    elif user_input == "scan_f":
        forename = input("| FORENAME = ")
        search_by_forename(forename)
    elif user_input == "scan_s":
        surname = input("| SURNAME = ")
        search_by_surname(surname)
    elif user_input == "exit":
        break
    else:
        print("ERROR: unknown command")

    print("----------------------")
    input("Press enter to continue...")
