import os
import artist_database


def clear_screen():
    """Clear everything on the treminal screen."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_main_menu():
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


def main():
    """Program will be executed from here."""
    clear_screen()
    # header
    print("-" * 50)
    print(f"{'Artist Database':^50}")
    print_main_menu()
    user_input = input("Selection> ").lower()
    print("-" * 50)
    if user_input == "l":
        for artist in artist_database.list_artists():
            print("-", artist["name"])
    elif user_input == "v":
        artist_name = input("Artist name> ")
        print("-" * 50)
        artist = artist_database.get_artist(artist_name)
        if artist:
            # Print thses information if the artist was found
            print("Genres:", ", ".join(artist["genres"]))
            print("Years Active:", ", ".join(artist["years_active"]))
            print("Members:", ", ".join(artist["members"]))
        else:
            # print error if artist wasn't found
            print("ERROR: Artist not found.")
    elif user_input == "e":
        exit()
    else:
        print("ERROR: Unknown command")


main()
