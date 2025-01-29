import requests


# send a request to the website to get some information. (cities list)
r = requests.get("https://8fzqlwv0jd.execute-api.eu-north-1.amazonaws.com/")
# if the request was ok
if r.ok:
    # convert content to json (python dict) which is structured data.
    data = r.json()
    # give the citites key to the `data` dict to get all cities
    cities = data.get("cities")
    print(".: JetSetsPets :.")
    print("-------------------")
    # iterate over cities list to print out all cities (with some string formating)
    for city in cities:
        print(f"- {city.title()}")

    print("-------------------")
    # get a city name from user
    selected_city = input("Select city: ").lower()
    print("-------------------")

    # if the user selected from `cities` list.
    if selected_city in cities:
        # print list of pets.
        pets = ["bird", "cat", "dog", "fish", "mouse", "rabbit"]
        for pet in pets:
            print(f"- {pet}")

        print("-------------------")
        # get selected pet from user
        selected_pet = input("Select a pet: ").lower()
        print("-------------------")

        # if user select a pet from `pets` list
        if selected_pet in pets:
            # send request for the `selected_city`
            user_req = requests.get(
                f"https://8fzqlwv0jd.execute-api.eu-north-1.amazonaws.com/{selected_city}"
            )
            if user_req.ok:
                # get city data like thier city, total , and all users
                user_info = user_req.json()
                # extract users data from responsed data (`user_info`)
                users = user_info.get("users")
                # iterate over all users to send request for each of them to get their pets
                for user in users:
                    # extract user id, forname and surname
                    userid = user.get("id")
                    forename = user.get("forename")
                    surname = user.get("surname")
                    # request user's id to get his/her animals
                    animal_req = requests.get(
                        f"https://8fzqlwv0jd.execute-api.eu-north-1.amazonaws.com/{selected_city}/{userid}"
                    )
                    # extract animal information
                    animal_info = animal_req.json()
                    # get list of animals
                    animals = animal_info.get("animals")
                    # iterate over animals
                    for animal in animals:
                        # get type of the animal
                        animal_type = animal.get("type")
                        # get name of the animal
                        animal_name = animal.get("name")
                        # compare `animal_type` with `selected_pet` if their was same pet type print the
                        # owner and pet information.
                        if animal_type == selected_pet:
                            print(
                                f"{forename} {surname} has a {animal_type} named {animal_name}"
                            )

        # if user was not select from `pets` list
        else:
            print("Error: pet not found.")
    # if user select the wrong city which is not in the `cities` list
    else:
        print("Error: city not found.")
