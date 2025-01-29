import requests


# the url we would like to send a request
url = "https://8fzqlwv0jd.execute-api.eu-north-1.amazonaws.com"
# send a request to `url`
response = requests.get(url)
# convert reterived data to python dict
data = response.json()
# Extract cities key from `data`
cities = data["cities"]

print(".: JetSetsPets :.")
print("-------------------")
# Iterate over cities list and print out each city.
for city in cities:
    print("- ", city.capitalize())
print("-------------------")

# get a city name from user
city_name = input("Select city: ").lower()
# check if the `city_name` is in the `cities` list
if city_name in cities:
    # Send a request based on city user entered
    users_resp = requests.get(url + "/" + city_name)
    # extract users list from the response (`users_resp`)
    users = users_resp.json()["users"]
    # Create list of pets
    animals = ["bird", "cat", "dog", "fish", "mouse", "rabbit"]
    # Show all animals name
    for animal in animals:
        print("-", animal.capitalize())
    # get the name of the animal from user
    animal_type = input("Select a pet: ").lower()
    # if the user entered correct animal name
    if animal_type in animals:
        # iterate over each user to get their animal's inforamtion
        for user in users:
            user_resp = requests.get(url + "/" + city_name + "/" + user["id"])
            # get all animal for the user (a user may have more than one animal)
            user_animal_list = user_resp.json()["animals"]
            # iterate over animals that user may have
            for user_animal in user_animal_list:
                # compare the user entred `animal_type` with the data reterived from website
                if animal_type == user_animal["type"]:
                    print(
                        user["forename"],
                        user["surname"],
                        "has a",
                        animal_type,
                        "named",
                        user_animal["name"],
                    )
    else:
        print("Error: pet not found.")
# if the city_name was not in the `cities`
else:
    print("Error: city not found.")
