import os
import artist_database


def clear_screen():
    """Clear everything on the treminal screen."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def show_menu():
    """Show menu items."""
    items = (
        "| L | List artists",
        "| V | View artist profile",
        "| E | Exit application",
    )
    print("-" * 50)
    for item in items:
        print(item)
    print("-" * 50)


def show_artists():
    """
    Print all artists.
    """
    artists = artist_database.list_artists()
    for artist in artists:
        print(f"- {artist['name']}")


def view_profile():
    """
    Get an artist name from user and print the artist profile if found
    If the artist not found will print approprate error message.
    """
    artist_name = input("Artist Name: ")
    print("-" * 50)

    result = artist_database.get_artist(artist_name)
    if result["status"] == "ok":
        value = result["value"]
        print(value["name"])
        print("*" * 50)
        print(", ".join(value["genres"]))
        print(", ".join(value["years_active"]))
        print(", ".join(value["members"]))
    else:
        print(value["value"])


def main():
    """
    The main function of the program.
    Program will run from here.
    """
    clear_screen()
    show_menu()
    user_choice = input("Selection > ").lower()
    print("-" * 50)

    if user_choice == "l":
        show_artists()
    elif user_choice == "v":
        view_profile()
    elif user_choice == "e":
        exit()
    else:
        print("ERROR: Wrong choice.")


# execute main function.
main()
