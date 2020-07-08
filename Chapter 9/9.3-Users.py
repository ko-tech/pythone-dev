# 9-3: Users
class User():
    def __init__(self, first_name, last_name, username, company):
        """Initializing attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.company = company
    
    def describe_user(self):
        """Printing all attributes"""
        print("\nFirst Name: " + self.first_name.title())
        print("Last Name: " + self.last_name.title())
        print("Username: " + self.username)
        print("Company: " + self.company.title())
    
    def greet_user(self):
        """Personalized greeting Message"""
        print("Welcome " + self.first_name.title() + " " + self.last_name.title() + "!")
    

user1 = User("kevin", "osorio", "kosorio", "reach")
user1.describe_user()
user1.greet_user()

user2 = User("eddy", "varela", "evarela", "amazon")
user2.describe_user()
user2.greet_user()

user3 = User("michael", "gray", "mgray", "probel")
user3.describe_user()
user3.greet_user()

user4 = User("holly", "parrish", "hparrish", "matrix")
user4.describe_user()
user4.greet_user()
