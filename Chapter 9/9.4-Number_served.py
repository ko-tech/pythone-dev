# 9-4 - Number Served
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

    def increment_number_served(self, quantity):
        """Method to add people served"""
        self.number_served += quantity
    
    def describe_restaurant(self):
        """Method to describe restaurant"""
        print(self.r_name.title() + " serves " + self.r_cuisine.title() + ".")
    
    def open_restaurant(self):
        """Method to announce restaurant is open"""
        print(self.r_name.title() + " is now open!")

"""make new restaurant and use new method"""
restaurant4 = Restaurant("micky d", "trash")
print(restaurant4.number_served)
restaurant4.set_number_served(56)
print(restaurant4.number_served)

"""Use new method to show increase in people served in one business day"""
restaurant4.increment_number_served(120)
print(restaurant4.number_served)