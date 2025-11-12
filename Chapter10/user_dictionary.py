# 10-13. User Dictionary: The remember_me.py example only stores one piece of information, the username.
# Expand this example by asking for two more pieces of information about the user, then store all the information you collect in a dictionary. 
# Write this dictionary to a file using json.dumps(), and read it back in using json.loads().
# Print a summary showing exactly what your program remembers about the user.


from pathlib import Path
import json

from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored user information if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_user_info(path):
    """Prompt for new user information."""
    username = input("What is your name? ")
    age = input("How old are you? ")
    location = input("Where do you live? ")
    
    user_info = {
        'username': username,
        'age': age,
        'location': location
    }
    
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def greet_user():
    """Greet the user and show remembered information."""
    path = Path('user_info.json')
    user_info = get_stored_user_info(path)
    
    if user_info:
        print("\nWelcome back!")
        print_summary(user_info)
    else:
        user_info = get_new_user_info(path)
        print(f"\nWe'll remember you when you come back, {user_info['username']}!")
        print_summary(user_info)

def print_summary(user_info):
    """Print a summary of all stored user information."""
    print("\n--- Here's what I remember about you ---")
    for key, value in user_info.items():
        print(f"{key.capitalize()}: {value}")
    print("----------------------------------------\n")

# Run the program
greet_user()