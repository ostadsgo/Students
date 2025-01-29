import os
import requests


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_header():
    header_title = "Artists Database"
    print("-" * 50)
    print("{:^50}".format(header_title))


def print_main_menu():
    items = (
        "| L | List artists",
        "| V | View artist profile",
        "| E | Exit application",
    )
    print("-" * 50)
    for item in items:
        print(item)
    print("-" * 50)


def get_artists():
    url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
    artists_req = requests.get(url)
    artists_data = artists_req.json()
    artists = artists_data.get("artists")
    return artists


def get_artist_profile(artist_id):
    url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
    artists_req = requests.get(url + artist_id)
    artists_data = artists_req.json()
    artist_profile = artists_data.get("artist")
    return artist_profile


def print_artists():
    artists = get_artists()
    for artist in artists:
        print("|", artist["name"])


def print_profile(artist):
    print("*" * 50)
    print("{:^50}".format(artist["name"]))
    print("*" * 50)
    print("| Members:", ", ".join(artist["members"]))
    print("| Geners:", ", ".join(artist["genres"]))
    print("| Years active:", ", ".join(artist["years_active"]))


def view_artist():
    artist_name = input("| Artist name> ").lower()
    artists = get_artists()
    for artist in artists:
        if artist["name"].lower() == artist_name:
            artist_profile = get_artist_profile(artist["id"])
            print_profile(artist_profile)
            break
    else:
        print("-" * 50)
        print(f"|\nERROR: Artist not found '{artist_name}'\n|")


def run(fn=None):
    clear_screen()
    print_header()
    if fn is not None:
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
