import os

goals = {"today": "Run 5 km", "tomorrow": "Lift 10 kg", "later": "Cycle 30 km"}
while True:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    menu = ".: THREE DAY PLANNER :.\n"
    menu += "-----------------------\n"
    menu += "    WORKOUT GOALS!\n"
    menu += "  ONE DAY AT A TIME.\n"
    menu += "-----------------------\n"
    menu += f"TODAY: {goals.get('today')}\n"
    menu += f"TOMORROW: {goals.get('tomorrow')}\n"
    menu += f"LATER: {goals.get('later')}\n"
    menu += "-----------------------\n"
    menu += "n | Next day\n"
    menu += "c | Change goal\n"
    menu += "e | Exit program\n"
    menu += "-----------------------"
    print(menu)
    user_choice = input("Operation > ")

    if user_choice == "n":
        goals["today"] = goals["tomorrow"]
        goals["tomorrow"] = goals["later"]
        goals["later"] = ""
        continue
    elif user_choice == "c":
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        title = ".: THREE DAY PLANNER :.\n"
        title += "-----------------------\n"
        title += "    WORKOUT GOALS!\n"
        title += "ONE DAY AT A TIME.\n"
        title += "-----------------------"
        print(title)
        print("0 | TODAY\n1 | TOMORROW\n2 | LATER")
        print("-----------------------")
        day = input("Change goal day > ")
        if day == "0":
            new_goal = input("Goal for today > ")
            goals["today"] = new_goal
        elif day == "1":
            new_goal = input("Goal for tomorrow > ")
            goals["tomorrow"] = new_goal
        elif day == "2":
            new_goal = input("Goal for later > ")
            goals["later"] = new_goal
        else:
            print("ERROR: Bad day\nINFO: Expected integer (0-2)")
    elif user_choice == "e":
        exit()
    else:
        print(f"ERROR: Unknown operation ({user_choice})")

    input("Press enter to continue...")
