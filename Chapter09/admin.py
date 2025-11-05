# 9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167).
# Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. 
# Write a method called show_privileges() that lists the administrator’s set of privileges.
# Create an instance of Admin, and call your method.

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

class Admin(User):
    """Initializes User Admin"""
    def __init__(self, username='admin'):
        super().__init__(username)
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user'
        ]
    
    def show_privileges(self):
        """Shows a list of your current privileges as user 'Admin' """
        print("Your current privileges are: ")
        for privilege in self.privileges:
            print(f"\t{privilege}")

admin = Admin('admin')
admin.show_privileges()