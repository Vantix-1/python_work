# 9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
# Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges.

class User:
    def __init__(self, username):
        """"Initialize Username"""
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print(f"Username: {self.username}")

    def greet_user(self):
        print(f"Hello, {self.username}")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Login Attempts Incremented: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login Attempts has been reset. Current attempts: {self.login_attempts}")

class Privileges:
    """A class to store and display privileges"""
    def __init__(self):
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user'
        ]
    
    def show_privileges(self):
        """Shows a list of current privileges"""
        print("Your current privileges are: ")
        for privilege in self.privileges:
            print(f"\t{privilege}")

class Admin(User):
    """Initializes User Admin"""
    def __init__(self, username='admin'):
        super().__init__(username)
        self.privileges = Privileges()

admin = Admin('admin')
admin.privileges.show_privileges()