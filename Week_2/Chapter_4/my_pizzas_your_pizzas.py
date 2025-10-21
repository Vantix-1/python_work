# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#   -Add a new pizza to the original list.
#   -Add a different pizza to the list friend_pizzas.
#   -Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.


# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#   Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
#   Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
#pizzas = ['pepperoni','sausage','mushroom']
#for pizza in pizzas:
#    print(F'{pizza}')
#    print(f'{pizza.title()}, is one of my all time favorite pizzas.')
#print(f'\nI really love pizza')

my_pizzas = ['pepperoni','sausage','mushroom']
friend_pizzas = my_pizzas[:]

#print(my_pizzas)
#print(friend_pizzas)
my_pizzas.append('olive')
#print(my_pizzas)
friend_pizzas.append('peppers')
#print(friend_pizzas)

print("My favorite pizza toppings are:")
for pizza in my_pizzas:
    print(pizza)

print("My friends favorite pizza toppings are:")
for pizza in friend_pizzas:
    print(pizza)