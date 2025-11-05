# 9-2. Three Restaurants: Start with your class from Exercise 9-1.
# -Create three different instances from the class
# -and call describe_restaurant() for each instance.


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


#my_restaurant = Restaurant('Tacos', 'Mexican')
#print(my_restaurant.restaurant_name)
#print(my_restaurant.cuisine_type)

#my_restaurant.describe_restaurant()
#my_restaurant.open_restaurant()

restaurant1 = Restaurant('MCD', 'Burgers')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('BK', 'Burgers')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Panda','Chinese')
restaurant3.describe_restaurant()