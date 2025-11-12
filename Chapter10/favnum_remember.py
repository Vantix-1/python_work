# 10-12. Favorite Number Remembered: Combine the two programs you wrote in Exercise 10-11 into one file.
#  If the number is already stored, report the favorite number to the user.
# If not, prompt for the user’s favorite number and store it in a file. 
# Run the program twice to see that it works.

from pathlib import Path
import json

def get_stored_favorite_number(path):
    """Get stored favorite number if available"""
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        return favorite_number
    else:
        return None
    
def read_favorite_number():
    """Read Favorite Number or Add a new number"""    
    path = Path('favorite_number.json')
    favorite_number = get_stored_favorite_number(path)
    if favorite_number:
        print(f"I know your favorite number! It's: {favorite_number}")
    else:
        favorite_number = input("What is your favorite number: ")
        contents = json.dumps(favorite_number)
        path.write_text(contents)
        print(f"I'll remember your favorite number is: {favorite_number}")

read_favorite_number()        
