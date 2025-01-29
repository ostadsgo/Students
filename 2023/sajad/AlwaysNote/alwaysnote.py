import os
import csv


def clear():
    if os.name == "nt":  # windows
        os.system("cls")
    else:  # Mac and Linux
        os.system("clear")


def format_menu(notes):
    s = ""
    for note in notes:
        s += "- " + note[0] + "\n"
    return s


def add_note(notes):
    title = input("title > ")
    descr = input("descr > ")
    note = (title, descr)
    notes.append(note)
    print("------------------")
    print("INFO: Note added")


def view_note(notes):
    title = input("title > ")
    found_note = False
    for note in notes:
        if note[0] == title:  # note[0] is the title of the note.
            print("------------------")
            print(note[1])  # note[1]  is the description of the note.
            found_note = True
            break

    if not found_note:
        print("------------------")
        print("ERROR: Unknown note")

def remove_note(notes):
    title = input("title > ")
    found_note = False
    note_index = 0
    for note in notes:
        if note[0] == title:  # note[0] is the title of the note.
            found_note = True
            break
        note_index += 1

    if found_note:
        del notes[note_index]
        print("------------------")
        print("INFO: Note deleted")
    else:        
        print("------------------")
        print("ERROR: Unknown note")

def load_notes():
    with open("notes.csv", "r") as notes_file:
        csvreader = csv.reader(notes_file)
        notes = list(csvreader)
    return notes

def save_notes(notes):
    with open("notes.csv", "w") as notes_file:
        csvwriter = csv.writer(notes_file)
        csvwriter.writerows(notes)
    print("------------------")
    print("SUCESS: Notes saved to file.")


menu_fmt = """
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

notes = load_notes()
running = True

while running:
    clear()
    formatted_notes = format_menu(notes)
    menu = menu_fmt.format(notes=formatted_notes)
    print(menu)
    user_choice = input("menu > ")
    print("------------------")

    if user_choice == "view":
        view_note(notes)
    elif user_choice == "add":
        add_note(notes)
    elif user_choice == "rm":
        remove_note(notes)
    elif user_choice == "exit":
        print("Saving notes in csv file ...")
        save_notes(notes)
        running = False
        continue
    else:
        print("ERROR: Unknown command.")

    print("------------------")
    input("Press enter key to continue ...")
