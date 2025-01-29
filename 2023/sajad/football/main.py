import os
import football


def clear_screen():
    """Clear everything on the treminal screen."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def show_header():
    """Print header of the program."""
    titles = ["FOOTBALL FRENZY", "STAT VIWER", "1.0.0"]
    print("*" * 50)
    for title in titles:
        print(f"{title:^50}")


def show_menu():
    """Print main menu of the program."""
    items = ["| list | List available seasons", "| view | View available seasons"]
    print("-" * 50)
    for item in items:
        print(item)
    print("-" * 50)


def show_years():
    """Print years that games played."""
    years = football.list_years()
    for year in years:
        print("|", year)


def show_scoreboard():
    """Print scoreboard of the year."""
    year = input("Year > ")
    print("*" * 50)
    print("|")
    years = football.list_years()
    if year not in years:
        print(" Unknow Year.")
    else:
        scoreboard = football.get_scoreboard(year)
        # print formatted table of scoreboard
        # Format header of the scoreboard
        print(f"{'| Team':30}{'W':>5}{'D':>5}{'L':>5}{'P':>5}")
        print(" " + "-" * 29 + "  ---  ---  ---  ---")

        for team in scoreboard:
            team_name = team[0]
            team_info = team[1]
            wins = team_info["wins"]
            lose = team_info["lose"]
            draw = team_info["draw"]
            points = team_info["points"]
            print(f"| {team_name:28}{wins:>5}{draw:>5}{lose:>5}{points:>5}")


def main():
    """Program will start from here."""
    running = True
    while running:
        clear_screen()
        show_header()
        show_menu()
        user_input = input("| Selection > ")
        print("-" * 50)
        if user_input == "list":
            show_years()
        elif user_input == "view":
            show_scoreboard()
        else:
            print("Unknow selection.")
        print("-" * 50)
        input("Press ENTER key to continue ...")


main()
