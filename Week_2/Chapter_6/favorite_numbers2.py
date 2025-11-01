# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number.
# -Then print each person’s name along with their favorite numbers.

favorite_number = {
    'bob':['1','2'],
    'tom':['6','12'],
    'jerry':['7','4'],
    'rick':['8','24','32'],
    'morty':['33','36']
    }

for name, favorite in favorite_number.items():
    print(f"\n{name.title()}'s favorite number/numbers is/are:")
    print(f"\t{favorite}")
