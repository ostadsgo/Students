import os
import csv


def clear():
    # clear screen
    if os.name == "nt":  # windows
        os.system("cls")
    else:  # Mac, Linux
        os.system("clear")


def read_people_database():
    f = open("database.csv")
    people = list(csv.reader(f))
    f.close()
    return people[1:]  # return without header


people = read_people_database()

main_menu = """
.: PEOPLES DATABASE :.
----------------------
get_id | Get person by ID
scan_f | List people by FORENAME
scan_s | List people by SURNAME
exit   | Exit program
----------------------"""

running = True
while running:
    clear()  # clear screen
    print(main_menu)
    user_choice = input("| menu > ")

    if user_choice == "get_id":
        person_id = input("ID = ")
        found = False
        print("----------------------")
        for person in people:
            if person[0] == person_id:
                print("| ID:", person[0])
                print("| FORENAME:", person[1])
                print("| SURNAME:", person[2])
                print("| GENDER:", person[3])
                print("| YEAR:", person[4])
                found = True
                break
        if found == False:
            print("Not found.")

    elif user_choice == "scan_f":
        forename = input("FORENAME = ")
        for person in people:
            if person[1] == forename:
                print(",".join(person))

    elif user_choice == "scan_s":
        surname = input("SURNAME = ")
        for person in people:
            if person[2] == surname:
                print(",".join(person))

    elif user_choice == "exit":
        running = False

    else:
        print("ERROR: Unknown command.")

    print("----------------------")
    input("Press enter key to continue ...")
