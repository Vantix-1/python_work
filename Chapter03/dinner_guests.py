# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (pages 41–42), use len() to print a message indicating the number of people you’re inviting to dinner.

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
guest = ['amy','bill','judy']
message = (f"I would like to formally invite you {guest[0].title()} to dinner this Friday.")
print(message)
message = (f"I would like to formally invite you {guest[1].title()} to dinner this Friday.")
print(message)
message = (f"I would like to formally invite you {guest[2].title()} to dinner this Friday.")
print(message)
print(len(guest))