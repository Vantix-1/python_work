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

message = (f"I would like to formally invite you {guest[0].title()} to dinner this Friday.")
print(message)
message = (f"I would like to formally invite you {guest[1].title()} to dinner this Friday.")
print(message)
message = (f"I would like to formally invite you {guest[2].title()} to dinner this Friday.")
print(message)
message = (f"I would like to formally invite you {guest[3].title()} to dinner this Friday.")
print(message)
message = (f"I would like to formally invite you {guest[4].title()} to dinner this Friday.")
print(message)
message = (f"I would like to formally invite you {guest[5].title()} to dinner this Friday.")
print(message)