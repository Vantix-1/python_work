# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
#   -Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#   -Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#   -Print a message to each of the two people still on your list, letting them know they’re still invited.
#   -Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#   -Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#   -Use insert() to add one new guest to the beginning of your list.
#   -Use insert() to add one new guest to the middle of your list.
#   -Use append() to add one new guest to the end of your list.
#   -Print a new set of invitation messages, one for each person in your list.

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite. 
#   -Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#   -Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#   -Print a second set of invitation messages, one for each person who is still in your list.
guest = ['amy','bill','judy']
#message = (f"I would like to formally invite you {guest[0].title()} to dinner this Friday.")
#print(message)
#message = (f"I would like to formally invite you {guest[1].title()} to dinner this Friday.")
#print(message)
#message = (f"I would like to formally invite you {guest[2].title()} to dinner this Friday.")
#print(message)

#message = (f"Unfortunately {guest[2].title()} is unable to make it.")
#print(message)
guest[2] = 'craig'
#print(guest)

#message = (f"I would like to formally invite you {guest[0].title()} to dinner this Friday.")
#print(message)
#message = (f"I would like to formally invite you {guest[1].title()} to dinner this Friday.")
#print(message)
#message = (f"I would like to formally invite you {guest[2].title()} to dinner this Friday.")
#print(message)

#message = (f"Hello {guest[0].title()}, {guest[1].title()}, {guest[2].title()}, I have found a bigger table for our dinner.")
#message.rstrip()
#print(message)

guest.insert(0, 'frank')
#print(guest)

guest.insert(2, "joe")
#print(guest)

guest.append('emma')
#print(guest)

#message = (f"I would like to formally invite you {guest[0].title()} to dinner this Friday.")
#print(message)
#message = (f"I would like to formally invite you {guest[1].title()} to dinner this Friday.")
#print(message)
#message = (f"I would like to formally invite you {guest[2].title()} to dinner this Friday.")
#print(message)
#message = (f"I would like to formally invite you {guest[3].title()} to dinner this Friday.")
#print(message)
#message = (f"I would like to formally invite you {guest[4].title()} to dinner this Friday.")
#print(message)
#message = (f"I would like to formally invite you {guest[5].title()} to dinner this Friday.")
#print(message)


#print(guest)
#message = (f"\tDear {guest[0].title()}, {guest[1].title()}, {guest[2].title()}, {guest[3].title()}, {guest[4].title()}, {guest[5].title()}, unfortunately a mixup occured and my reservation was cancelled. The new reservation only allows a table of 3. ")
#print(message)

#message = ("You can only invite two guests. Your reservation was mistakenly cancelled.")
#print(message)

frank = guest.pop(0).title()
message = (f"{frank} I apologize, due to a mixup I can't invite you to dinner.")
print(message)
print(guest)

joe = guest.pop(1).title()
message = (f"{joe} I apologize, due to a mixup I can't invite you to dinner.")
print(message)
print(guest)

emma = guest.pop(-1).title()
message = (f"{emma} I apologize, due to a mixup I can't invite you to dinner.")
print(message)
print(guest)

craig = guest.pop(-1).title()
message = (f"{craig} I apologize, due to a mixup I can't invite you to dinner.")
print(message)
print(guest)

message = (f"Congrats {guest[0].title()}! You've made the cut and you are still invited to dinner with me!")
print(message)

message = (f"Congrats {guest[1].title()}! You've made the cut and you are still invited to dinner with me!")
print(message)

print(guest)
guest.remove('amy')
print(guest)
guest.remove('bill')
print(guest)