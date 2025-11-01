# 6-9. Favorite Places: Make a dictionary called favorite_places. 
# -Think of three names to use as keys in the dictionary, and store one to three favorite places for each person.
# -To make this exercise a bit more interesting, ask some friends to name a few of their favorite places.
# -Loop through the dictionary, and print each person’s name and their favorite places.
favorite_places = {
'mickey':['house','park'],
'mando':['mandoloria','space'],
'dora':['jungle','ocean'],
}
for name, favorite in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for fav in favorite:
        print(fav)