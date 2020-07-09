#9-6 Ice Cream Stand:
class Restaurant():
    """Simple Restaurant Class"""
    def __init__(self, r_name, r_cuisine):
        """Initialize name and cuisine attributes"""
        self.r_name = r_name
        self.r_cuisine = r_cuisine
        self.number_served = 10
    
    def set_number_served(self, number):
        """9-4 Continued - add method to set number served"""
        self.number_served = number
    
    def describe_restaurant(self):
        """Method to describe restaurant"""
        print(self.r_name.title() + " serves " + self.r_cuisine.title() + ".")
    
    def open_restaurant(self):
        """Method to announce restaurant is open"""
        print(self.r_name.title() + " is now open!")

class IceCreamStand(Restaurant):
    def __init__(self, r_name, r_cuisine):
        """Initialize attributs from parent class
        then add attributes specific to IceCreamStands"""
        super().__init__(r_name, r_cuisine)
        self.flavors = ["Vanilla", "Chocolate", "Cookies & Cream", "Mint"]
    
    def list_flavors(self):
        """List available flavors"""
        print("These are our available flavors: ")
        for flavor in self.flavors:
            print(flavor.title())


my_ice_cream_stand = IceCreamStand("frosty", "ice cream")
my_ice_cream_stand.list_flavors()