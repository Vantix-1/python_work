# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
#print(names)
#print(names[0].title())
#print(names[1].upper())
#print(names[2].lower())
#print(names[3])
#print(names[-1])
message = f"Hope you have a great day {names[0]}!"
print(message)
message = f"Hope you have a great day {names[1].title()}!"
print(message)
message = f"Hope you have a great day {names[2].upper()}!"
print(message)
message = f"Hope you have a great day {names[3].lower()}!"
print(message)
message = f"Hope you have a great day {names[-1].title()}!"
print(message)