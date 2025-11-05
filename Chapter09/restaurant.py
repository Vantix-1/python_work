# 9-1. Restaurant: Make a class called Restaurant.
# -The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# -make a method called describe_restaurant() that prints these two pieces of information, 
# -and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# -Make an instance called restaurant from your class.
# -Print the two attributes individually, and then call both methods.

class Restaurant:
    """"Model for a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize Restaurant Name and Type of Cuisine"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Prints the Restaurant Name and Cuisine Type"""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")
    
    def open_restaurant(self):
        """Prints a message that the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")


my_restaurant = Restaurant('Tacos', 'Mexican')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()