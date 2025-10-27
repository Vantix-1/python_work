# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
#   -Store the numbers 1 through 9 in a list
#   -Loop through the list.
#   -Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

numbers = ['1','2','3','4','5','6','7','8','9']
for number in numbers:
    if number == '1':
        ord ='1st'
    elif number == '2':
        ord = '\n2nd'
    elif number == '3':
        ord = '\n3rd'
    elif number == '4':
        ord = '\n4th'
    elif number == '5':
        ord = '\n5th'
    elif number == '6':
        ord = '\n6th'
    elif number == '7':
        ord = '\n7th'
    elif number == '8':
        ord = '\n8th'
    elif number == '9':
        ord = '\n9th'
    print(ord)