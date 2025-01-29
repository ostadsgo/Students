import os
import requests


def clear():
    # if the operating system was Windows
    if os.name == "nt":
        os.system("cls")
    # if the operating system was Linux, Mac, ...
    else:
        os.system("clear")


def print_main_menu():
    menu_items = "| L | List artists\n| V | View artist profile\n| E | Exit application"
    print(menu_items)


def print_list_of_artists():
    # get artists from web api
    url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
    artists_req = requests.get(url)
    artists_data = artists_req.json()
    # -------------------------------
    # Artists list
    artists = artists_data["artists"]
    # Print each artist's name
    for artist in artists:
        # get the name of the artist
        print("|", artist["name"])


def print_artist_info(url, artists, artist_name):
    for artist in artists:
        # compare user entered artist name with each artist
        # Goal: find the artist user entered
        if artist["name"].lower() == artist_name:
            artist_id = artist["id"]
            artist_req = requests.get(url + artist_id)
            artist_data = artist_req.json()
            artist_info = artist_data["artist"]
            genres = artist_info["genres"]
            years_active = artist_info["years_active"]
            members = artist_info["members"]
            print("*************************************")
            print(f"     {artist_name.capitalize()}     ")
            print("*************************************")
            print("| Members:", ", ".join(members))
            print("| Geners:", ", ".join(genres))
            print("| Years active:", ", ".join(years_active))


def print_artist_profile():
    # get artists from web api
    url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
    artists_req = requests.get(url)
    artists_data = artists_req.json()
    # -------------------------------
    # Artists list
    artists = artists_data["artists"]
    # get artist's name from user
    artist_name = input("| Artist name> ").lower()
    # make  a list from artist name to compare it with artist name user entered
    artists_name_list = []
    for artist in artists:
        artists_name_list.append(artist["name"].lower())

    # if user entered correct artist name
    if artist_name in artists_name_list:
        # iterate each artice and find the artist user enterd
        print_artist_info(url, artists, artist_name)
    # if the user entered wrong artist name
    else:
        print("|")
        print(f"ERROR: Artist not found '{artist_name}'")
        print("|")


def run():
    running = True
    clear()
    print("-------------------------------------")
    print("             Artists Database        ")
    print("-------------------------------------")
    print_main_menu()
    print("-------------------------------------")
    user_input = input("| Selection> ")
    while running:
        if user_input == "l" or user_input == "L":
            clear()
            print("-------------------------------------")
            print("             Artists Database        ")
            print("-------------------------------------")
            print_list_of_artists()
            print("*************************************")
            print_main_menu()
            print("-------------------------------------")
            user_input = input("| Selection> ")
        # if the user input was 'v' or 'V'
        elif user_input == "v" or user_input == "V":
            clear()
            print("-------------------------------------")
            print("             Artists Database        ")
            print("-------------------------------------")
            print_artist_profile()
            print("-------------------------------------")
            print_main_menu()
            print("-------------------------------------")
            user_input = input("| Selection> ")

        # if the user input was 'e' or 'E'
        elif user_input == "e" or user_input == "E":
            print("SUCESS: Script exited successfuly")
            running = False
        # if user not choose from main menu.
        else:
            print("Error: Unknown command")
            input("Press enter key to continue ... ")
            clear()
            print("-------------------------------------")
            print("             Artists Database        ")
            print("-------------------------------------")
            print_main_menu()
            print("-------------------------------------")
            user_input = input("| Selection> ")


run()
