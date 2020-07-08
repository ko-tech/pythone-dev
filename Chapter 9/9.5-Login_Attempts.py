# 9-5: Login Attempts
class User():
    def __init__(self, first_name, last_name, username, company):
        """Initializing attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.company = company
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        """Method to increase login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts (self):
        """Method to reset login attempts"""
        self.login_attempts = 0
    
    def describe_user(self):
        """Printing all attributes"""
        print("\nFirst Name: " + self.first_name.title())
        print("Last Name: " + self.last_name.title())
        print("Username: " + self.username)
        print("Company: " + self.company.title())
    
    def greet_user(self):
        """Personalized greeting Message"""
        print("Welcome " + self.first_name.title() + " " + self.last_name.title() + "!")

user5 = User("dennis", "crissy", "dcrissy", "reach")
user5.increment_login_attempts()
user5.increment_login_attempts()
user5.increment_login_attempts()
user5.increment_login_attempts()
print(user5.login_attempts)
user5.reset_login_attempts()
print(user5.login_attempts)