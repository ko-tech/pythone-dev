# 9-8: Privileges
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

class Privileges():
    """Class for privileges alone"""
    def __init__(self, privilege=["can modify post", "can delete post", "can ban user"]): 
        self.privileges = privilege

    def show_privileges(self):
        print("These are " + self.first_name.title() + "'s privileges")
    for privilege in self.privileges:
        print(privilege.title())


class Admin(User):
    def __init__(self, first_name, last_name, username, company):
        """Initializing atttributes from parent class
        and adding attributes"""
        super().__init__(first_name, last_name, username, company)
        self.privileges = Privileges()


admin = Admin("kevin", "osorio", "kosorio", "reach")
admin.privileges.show_privileges()