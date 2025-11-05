# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# -Add an attribute called number_served with a default value of 0. 
# -Create an instance called restaurant from this class.
# -Print the number of customers the restaurant has served, 
# -Print the number of customers the restaurant has served, 

#Add a method called set_number_served() that lets you set the number of customers that have been served.
# -Call this method with a new number and print the value again.

# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
# -Call this method with any number you like that could represent how many customers were served in, say, a day of business.

class Restaurant:
    """"Model for a restaurant"""
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initialize Restaurant Name and Type of Cuisine"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        """Prints the Restaurant Name and Cuisine Type"""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")
    
    def open_restaurant(self):
        """Prints a message that the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")
    def set_number_served(self, number_served):
        """Sets the number of people who have been served"""
        self.number_served = number_served
        print(f"Number Served: {number_served}")
    def increment_number_served(self, customers):
        """Add the total amount of customers00 served for the day"""
        self.number_served += customers
        print(f"Added {customers} customers. Total served: {self.number_served}")

restaurant = Restaurant('Tacos', 'Mexican')

restaurant.set_number_served(4)
restaurant.increment_number_served(10)