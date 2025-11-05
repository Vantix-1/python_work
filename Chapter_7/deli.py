# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# -Then make an empty list called finished_sandwiches.
# -Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
# -As each sandwich is made, move it to the list of finished sandwiches. 
# -After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['tuna','meatball','italian']
finished_sandwichs = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I have made your {current_order} sandwich.")
    finished_sandwichs.append(current_order)
print("\nThese sandwich orders are completed: ")
for completed_orders in finished_sandwichs:
    print(completed_orders)