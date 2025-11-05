# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet.
# -In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. 
# -Next, loop through your list and as you do, print everything you know about each pet.

animal0 = {
    'type': 'dog',
    'owner':'bill',
}
animal1 = {
    'type': 'cat',
    'owner':'bob',
}
animal2 = {
    'type': 'bird',
    'owner':'dora',
}
pets = [animal0,animal1,animal2]
for pet in pets:
    print(pet)