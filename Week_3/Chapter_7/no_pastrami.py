# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
# -Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
# -and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
# -Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['pastrami','tuna','pastrami','meatball','pastrami','italian']
finished_sandwichs = []
print("Sorry we are out of Pastrami at this time. ")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I have made your {current_order} sandwich.")
    finished_sandwichs.append(current_order)
print("\nThese sandwich orders are completed: ")
for completed_orders in finished_sandwichs:
    print(completed_orders)