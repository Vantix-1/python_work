# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#   -Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
#   -Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
#   -Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

# 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#   Modify your program to print a statement about each animal, such as A dog would make a great pet.
#   Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!

#pets = ['dog','cat','fish']
#for pet in pets:
#    print(f'A {pet} would make a great pet.')
#print("\nAny of these animals would make a great pet")


pets = ['dog','cat','fish','hamster','horse','bird','lizard','snake','ferret','goat']
print("The first three items in the list are:")
for pet in pets[:3]:
    print(pet)

print("The middle three items in the list are:")
for pet in pets [4:7]:
    print(pet)

print('The last three items in the list are:')
for pet in pets[-3:]:
    print(pet)