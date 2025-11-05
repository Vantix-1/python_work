# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). 
# -Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
# -Loop through your list of people. As you loop through the list, print everything you know about each person.


person = {
    'first_name': 'bill',
    'last_name':'nye',
    'age': '80',
    'city': 'portland',
}
person1 = {
    'first_name': 'bob',
    'last_name':'builder',
    'age': '20',
    'city': 'austin',
}
person2 = {
    'first_name': 'dora',
    'last_name':'explorer',
    'age': '18',
    'city': 'mexico city',
}
people = [person,person1,person2]
for info in people:
    print(people)