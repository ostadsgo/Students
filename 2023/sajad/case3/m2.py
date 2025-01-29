import os
import requests


def clear_screen():
    """Clear everything on the treminal screen."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_header():
    """Make header text for the program."""
    title = "Artists Database"
    print("-" * 50)
    print(f"{title:^50}")


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


def get_data(url, key):
    """Get url and key to send request and return json data."""
    request = requests.get(url)
    data = request.json()
    value = data.get(key)
    return value


def get_artists():
    """Return list of artists."""
    url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
    return get_data(url, "artists")


def get_artist(artist_id):
    """Return data for an specific artist."""
    url = f"https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/{artist_id}"
    print(get_data(url, "artist"))
    return get_data(url, "artist")


def print_artists():
    """Print all artists' name."""
    artists = get_artists()
    for artist in artists:
        print("|", artist["name"])


def print_profile(artist):
    """Print an specific artist information."""
    print("*" * 50)
    print(f"{artist['name']:^50}")
    print("*" * 50)
    print("| Members:", ", ".join(artist["members"]))
    print("| Geners:", ", ".join(artist["genres"]))
    print("| Years active:", ", ".join(artist["years_active"]))


def view_artist():
    """Get an artist name from user, if found the artist print artist information."""
    artist_name = input("| Artist name> ").lower()
    artists = get_artists()
    for artist in artists:
        if artist["name"].lower() == artist_name:
            artist_profile = get_artist(artist["id"])
            print_profile(artist_profile)
            break
    else:
        print("-" * 50)
        print(f"|\nERROR: Artist not found '{artist_name}'\n|")


def run(fn=None):
    """clearscreen and print header, print main menu and get input from user, if
    there is function (fn) execute it.
    """
    clear_screen()
    print_header()
    if fn:
        print("-" * 50)
        fn()
    print_main_menu()
    return input("Selection> ").lower()


def main():
    user_choice = run()
    while True:
        print("-" * 50)
        if user_choice == "l":
            user_choice = run(print_artists)
        elif user_choice == "v":
            user_choice = run(view_artist)
        elif user_choice == "e":
            print("SUCESS: Script exited successfuly")
            break
        else:
            print("Error: Unknown command")
            print("-" * 50)
            input("Press enter key to continue ... ")
            user_choice = run()


main()
