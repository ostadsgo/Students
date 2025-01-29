from math import ceil

menu = [
    "2 hotdogs",
    "3 hotdogs",
    "2 vegan hotdogs",
    "3 vegan hotdogs",
]

orders = {}
total_students_number = 0
print("How many students wants... ")
for item in menu:
    students_number = int(input(item + " > "))
    if item == "2 hotdogs":
        orders["2 hotdogs"] = 2 * students_number

    elif item == "3 hotdogs":
        orders["3 hotdogs"] = 3 * students_number

    elif item == "2 vegan hotdogs":
        orders["2 vegan hotdogs"] = 2 * students_number

    elif item == "3 vegan hotdogs":
        orders["3 vegan hotdogs"] = 2 * students_number
    else:
        print("Invliad choice")
    total_students_number += students_number

# calculate the number of packages required.
meat_packages_number = ceil((orders["2 hotdogs"] + orders["3 hotdogs"]) / 8)
vegan_packages_number = ceil(
    (orders["2 vegan hotdogs"] + orders["3 vegan hotdogs"]) / 4
)


cost_meat_packages = 20.95 * meat_packages_number
cost_vegan_packages = 34.95 * vegan_packages_number
cost_dirnks = 13.95 * total_students_number

print("Meat: ", cost_meat_packages)
print("vegan: ", cost_vegan_packages)
print("drinks: ", cost_dirnks)
