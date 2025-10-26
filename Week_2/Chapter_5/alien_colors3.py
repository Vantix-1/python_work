# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#   -If the alien is green, print a message that the player earned 5 points.
#   -If the alien is yellow, print a message that the player earned 10 points.
#   -If the alien is red, print a message that the player earned 15 points.

alien_color = ['green']
if 'green' in alien_color:
    print("player earned 5 points")
elif 'yellow' in alien_color:
    print("player earned 10 points")
elif 'red' in alien_color:
    print("player earned 15 points")

alien_color = ['yellow']
if 'green' in alien_color:
    print("player earned 5 points")
elif 'yellow' in alien_color:
    print("player earned 10 points")
elif 'red' in alien_color:
    print("player earned 15 points")

alien_color = ['red']
if 'green' in alien_color:
    print("player earned 5 points")
elif 'yellow' in alien_color:
    print("player earned 10 points")
elif 'red' in alien_color:
    print("player earned 15 points")