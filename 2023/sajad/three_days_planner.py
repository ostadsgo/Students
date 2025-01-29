import os


todolist = ["Run 5 km", "Lift 10 kg", "Cycle 30 km"]

menu_fmt = """.: THREE DAY PLANNER :.
-----------------------
TODAY: {today}
TOMORROW: {tomorrow}
LATER: {later}
-----------------------
n | Next day
c | Change goal
e | Exit program
-----------------------"""

menu_change = """ : THREE DAY PLANNER :.
-----------------------
    WORKOUT GOALS!    
  ONE DAY AT A TIME.  
-----------------------
0 | TODAY
1 | TOMORROW
2 | LATER
-----------------------"""


def clear():
    # clear screen
    if os.name == "nt":  # windows
        os.system("cls")
    else:   # Mac, Linux
        os.system("clear")


while True:
    clear()  # clear screen
    menu = menu_fmt.format(today=todolist[0], tomorrow=todolist[1], later=todolist[2])
    print(menu)
    choice = input("operation > ")

    if choice == "n":
        todolist.pop(0)  # remove today (first item in the todolist.)
        todolist.append("")  # add empty string last item aka later.
        continue
    elif choice == "c":
        clear()
        print(menu_change)
        day = int(input("Change goal for day > "))
        if 0 <= day <= 2:
            goal = input("The goal: ")
            todolist[day] = goal  # replace today(index 0) with the user goal
        else:
            print("Unknown day!!")
    elif choice == "e":
        break
    else:
        print("Unknown operation.")

