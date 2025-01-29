import os
import json


def clear_screen():
    if os.name == "nt":  # windows
        os.system("cls")
    else:  # Mac and Linux
        os.system("clear")


def update_menu(menu, notes):
    titles = []
    for note in notes:
        title = f"- {note.get('title')}\n"
        titles.append(title)

    s = "".join(titles)
    return menu.format(notes=s)


def view(notes):
    title = input("title > ")
    for note in notes:
        if note.get("title") == title:
            print("------------------")
            print(note.get("descr"))
            print("------------------")
            break
    else:  # no break will execuate.
        print("------------------")
        print("ERROR: Unknown note")
        print("------------------")


def add(notes):
    title = input("title > ")
    descr = input("descr > ")
    note = {"descr": descr, "title": title}
    notes.append(note)
    print("------------------")
    print("INFO: Note added")
    print("------------------")


def rm(notes):
    title = input("title > ")
    found = False
    x = 0
    for note in notes:
        if note.get("title") == title:
            found = True
            break
        x += 1

    # delete if the title of note was found
    if found == True:
        notes.pop(x)
        print("------------------")
        print("INFO: Note deleted")
        print("------------------")
    else:  # no break will execuate.
        print("------------------")
        print("ERROR: Unknown note")
        print("------------------")


def load():
    with open("notes.json", "r") as json_file:
        notes = json.load(json_file)
    return notes


def save(notes):
    with open("notes.json", "w") as json_file:
        json.dump(notes, json_file)
    print("SUCESS: Notes saved to file.")


menu_format = """
.: ALWAYSNOTE :.
-- gold edition --
******************
{notes}
------------------
view | view note
add  | add note
rm   | remove note
exit | exit program
------------------"""
notes = load()  # all notes which are empty in the begining of the program.
while True:
    clear_screen()
    menu = update_menu(menu_format, notes)
    print(menu)
    user_input = input("menu > ")
    print("------------------")

    if user_input == "view":
        view(notes)
    elif user_input == "add":
        add(notes)
    elif user_input == "rm":
        rm(notes)
    elif user_input == "exit":
        # Save before exit
        print("Saving notes in json file ...")
        save(notes)
        break
    else:
        print("ERROR: Unknown command.")
        print("------------------")

    input("Press enter key to continue ...")
