# 10-5.	Guest Book: Write a while loop that prompts users for their name. 
# Collect all the names that are entered, and then write these names to a file called guest_book.txt.
# Make sure each entry appears on a new line in the file.

from pathlib import Path    
path = Path('week_4\Chapter_10\guest_book.txt')
guest_book = []
while True:
    name = input("Enter your name: (or 'q' to quit): ")
    if name == 'q':
        break
    guest_book.append(name)

path.write_text('\n'.join(guest_book))