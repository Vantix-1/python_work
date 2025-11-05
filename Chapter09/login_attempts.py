# 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3
# -Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
# -Write another method called reset_login_attempts() that resets the value of login_attempts to 0.

# Make an instance of the User class and call increment_login_attempts() several times
# -Print the value of login_attempts to make sure it was incremented properly,
# -and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

class User:
    def __init__(self, first_name, last_name):
        """"Initialize First and Last Name"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"Users first name is: {self.first_name}, and last name is: {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Login Attempts Incremented: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login Attempts has been reset. Current attempts: {self.login_attempts}")

new_user = User('Tom','Brady')
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()

print(f"\nCurrent Login Attempts: {new_user.login_attempts}")
new_user.reset_login_attempts()


