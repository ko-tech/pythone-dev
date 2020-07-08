# 9-1 - Restaurant Class
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

#9-2 - Three Restaurants
"""Making instance for class and using attributes and methods"""
restaurant = Restaurant("hooters", "italian food")
print("My Restaurant " + restaurant.r_name.title() + " serves " + restaurant.r_cuisine.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()

"""Creating 2 additional instances and calling describe_restaurant for both"""
restaurant2 = Restaurant("taco bell", "mexican")
restaurant2.describe_restaurant()

restaurant3 = Restaurant("five guys", "american")
restaurant3.describe_restaurant()

