people = [
    {
        "Name": "Daniel Radcliffe",
        "Gender": "male",
        "Hair color": "brown",
        "Eye color": "brown",
    },
    {
        "Name": "Rupert Grint",
        "Gender": "male",
        "Hair color": "red",
        "Eye color": "blue",
    },
    {
        "Name": "Emma Watson",
        "Gender": "female",
        "Hair color": "brown",
        "Eye color": "brown",
    },
    {
        "Name": "Selena Gomez",
        "Gender": "female",
        "Hair color": "brown",
        "Eye color": "brown",
    },
]

gender = input("Gender: ")
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")

matched_people = []
for person in people:
    if (
        person["Gender"] == gender
        and person["Hair color"] == hair_color
        and person["Eye color"] == eye_color
    ):
        matched_people.append(person["Name"])

if matched_people != []:
    print(", ".join(matched_people))
else:
    print("No match!")
