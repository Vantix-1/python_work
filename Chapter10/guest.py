# 10-4.	Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.

from pathlib import Path    
path = Path('week_4\Chapter_10\guest.txt')
guest = input('Enter your name: ')
path.write_text(guest)