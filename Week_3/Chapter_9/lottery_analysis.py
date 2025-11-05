# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
# -Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins.
# Print a message reporting how many times the loop had to run to give you a winning ticket.

import random
lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']
winner = random.sample(lottery, 4)
print(f"Any ticket matching these 4 numbers or letters wins a prize: {winner}")

my_ticket = [3, 7, 'A', 'E']
attempts = 0
while True:
    attempts += 1
    winner = random.sample(lottery, 4)
    if my_ticket == winner:
        print(f"My Numbers: {my_ticket}")
        print(f"Winning Numbers: {winner}")
        print(f"Attempts: {attempts:,}")
        break