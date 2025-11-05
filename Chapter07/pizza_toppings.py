# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
# -As they enter each topping, print a message saying you’ll add that topping to their pizza.

prompt = "\nPlease enter a topping you would like on your pizza:"
prompt += "\n (Enter 'quit when you are finished.)"
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"Added '{topping}' to your pizza.")