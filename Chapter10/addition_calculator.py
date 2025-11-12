# 10-7.	Addition Calculator: Wrap your code from Exercise 10-5 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.

print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit. ")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)+int(second_number)
    except ValueError:
        print("Please provide only numbers,no text **0,1,2,3**")
    else:
        print(answer)
