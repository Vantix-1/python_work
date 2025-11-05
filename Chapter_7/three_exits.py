# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
# -Use a conditional test in the while statement to stop the loop.
# -Use an active variable to control how long the loop runs.
# -Use a break statement to exit the loop when the user enters a 'quit' value

#prompt = "\nMay I please have your age for this movie ticket?: "
#prompt += "\n (Enter 'quit' when finished)"

#while True:
#    age = input(prompt)
#    if age == 'quit':
#        break
#    age = int(age)
#    if age < 3:
#        print("Your ticket is free")
#    if age >= 3 and age <= 12:
#        print("Your ticket is $10")
#    if age > 12:
#        print("Your ticket is $15")

#prompt = "\nMay I please have your age for this movie ticket?: "
#prompt += "\n (Enter 'quit' when finished)"

#age = ""
#while age != 'quit':
#    age = input(prompt)
#    if age != 'quit':
#        age = int(age)
#        if age < 3:
#            print("Your ticket is free")
#        elif age <= 12:
#            print("Your ticket is $10")
#        else:
#            print("Your ticket is $15")

prompt = "\nMay I please have your age for this movie ticket?: "
prompt += "\n (Enter 'quit' when finished)"

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free")
        elif age <= 12:
            print("Your ticket is $10")
        else:
            print("Your ticket is $15")