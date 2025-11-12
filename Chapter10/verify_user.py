# 10-14. Verify User: The final listing for remember_me.py assumes either that the user has already entered their username or that the program is running for the first time.
# We should modify it in case the current user is not the person who last used the program.
# Before printing a welcome back message in greet_user(), ask the user if this is the correct username. If it’s not, call get_new_username() to get the correct username.

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
    print("\nLet's collect some information about you:")
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

def verify_user(stored_username):
    """Verify that the current user is the correct person."""
    verification = input(f"Is '{stored_username}' your username? (y/n): ")
    return verification.lower() == 'y'

def greet_user():
    """Greet the user and show remembered information."""
    path = Path('user_info.json')
    user_info = get_stored_user_info(path)
    
    if user_info:
        # Verify this is the correct user
        if verify_user(user_info['username']):
            print(f"\nWelcome back, {user_info['username']}!")
            print_summary(user_info)
        else:
            # Current user is different - get new information
            print("\nLet me get your information instead.")
            user_info = get_new_user_info(path)
            print(f"\nWe'll remember you when you come back, {user_info['username']}!")
            print_summary(user_info)
    else:
        # First-time user
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