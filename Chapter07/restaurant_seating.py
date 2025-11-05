# 7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. 
# -If the answer is more than eight, print a message saying they’ll have to wait for a table
# -Otherwise, report that their table is ready.

tables = input("How many people will be in your dinner group tonight?")
tables = int(tables)
if tables >= 8:
    print('\nTheir will be a wait for your table.')
else:
    print("\n Your table is ready")