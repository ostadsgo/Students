import os
import json


def clear_screen():
    if os.name == "nt":  # windows
        os.system("cls")
    else:  # Mac and Linux
        os.system("clear")


def list_todo(todolist):
    for todo in todolist:
        if todo.get("status") == "done":
            print("[X]", todo.get("description"))
        else:
            print("[ ]", todo.get("description"))


def add_todo(todolist):
    todo_desc = input("Todo description: ")
    todo = {"description": todo_desc, "status": "notdone"}
    todolist.append(todo)
    print("--------------------------------")
    print("SUCESS: Todo added.")


def check_todo(todolist):
    x = 0
    # show all todos with a number in the left side
    for todo in todolist:
        if todo.get("status") == "done":
            print(x, "| [X]", todo.get("description"))
        else:
            print(x, "| [ ]", todo.get("description"))
        x += 1
    print("--------------------------------")
    # allow user to check the todo
    try:  # try to get the todo index and convert it to integer.
        todo_index = int(input("Todo index > "))
        todo = todolist[todo_index]
        print("--------------------------------")
        if todo.get("status") == "done":
            todo["status"] = "notdone"
            print("SUCESS: UNCHECKED -> CHECKED")
        else:
            todo["status"] = "done"
            print("SUCESS: CHECKED -> UNCHECKED")
    except ValueError:
        print("ERROR: Enter todo index please.")


def delete_todo(todolist):
    x = 0
    # show all todos with a number in the left side
    for todo in todolist:
        if todo.get("status") == "done":
            print(x, "| [X]", todo.get("description"))
        else:
            print(x, "| [ ]", todo.get("description"))
        x += 1
    print("--------------------------------")

    try:  # try to get the todo index and convert it to integer.
        todo_index = int(input("Todo index > "))
        todolist.pop(todo_index)
        print("--------------------------------")
        print("SUCESS: todo deleted.")
    except ValueError:
        print("ERROR: Enter todo index please.")


def load_todo():
    with open("todolist.json", "r") as json_file:
        todolist = json.load(json_file)
    return todolist


def save_todo(todolist):
    old_todos = load_todo()  # read todos from the json file.
    all_todos = old_todos + todolist  # combine todo from the file and program todos
    # Save todos into the json file.
    with open("todolist.json", "w") as json_file:
        json.dump(all_todos, json_file)
    print("SUCESS: Todos saved to file.")


def show_menu():
    items = [
        "list   | List todos",
        "add    | Add todo",
        "check  | Check todo",
        "delete | Delete todo",
        "--------------------------------",
        "save   | Save todos to file",
        "load   | Load todos from file",
        "--------------------------------",
    ]
    print("********************************")
    print("          Todoify               ")
    print("--------------------------------")
    for item in items:
        print(item)


def main():
    todolist = []
    while True:
        clear_screen()
        show_menu()
        user_input = input("Selection > ")
        print("--------------------------------")

        if user_input == "list":
            list_todo(todolist)
        elif user_input == "add":
            add_todo(todolist)
        elif user_input == "check":
            check_todo(todolist)
        elif user_input == "delete":
            delete_todo(todolist)
        elif user_input == "save":
            save_todo(todolist)
        elif user_input == "load":
            todolist = load_todo()
            print("SUCESS: Todos loaded from file.")
        else:
            print(f"Unknown command '{user_input}'")
        print("--------------------------------")
        input("Press enter key to continue ...")


main()
