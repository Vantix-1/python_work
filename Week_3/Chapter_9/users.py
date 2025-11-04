# 9-3. Users: Make a class called User. Create two attributes called first_name and last_name
# -and then create several other attributes that are typically stored in a user profile. 
# -Make a method called describe_user() that prints a summary of the user’s information.
# -Make another method called greet_user() that prints a personalized greeting to the user.
# -Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self, first_name, last_name,):
        """"Initialize First and Last Name"""
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(f"Users first name is: {self.first_name}, and last name is: {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}")

user1 = User('Bill','Nye')
user1.describe_user()
user1.greet_user()

user2 = User('Edward','Hands')
user2.describe_user()
user2.greet_user()

user3 = User('Bart','Simpson')
user3.describe_user()
user3.greet_user()