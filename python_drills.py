characters = [
    {"first_name": "Zade", "last_name": "Meadows"},
    {"first_name": "Rhysand", "last_name": "Archeron"},
    {"first_name": "Rhysand", "last_name": "Nightcourt"},
    {"first_name": "Lucien", "last_name": "Vanserra"}
]
for i in range(3):
    for character in characters:
        if character['first_name'] == "Rhysand":
            print ("Wedding crasher!")