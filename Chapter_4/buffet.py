# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
#   -Use a for loop to print each food the restaurant offers.
#   -Try to modify one of the items, and make sure that Python rejects the change.
#   -The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

menu_item = ('chicken','beef','pork','brocolli','green beans')

print("Our restaurants focus is on simplicity. We offer the five following foods in a variety of ways:")
for item in menu_item:
    print(item)

#menu_item[0] = "lamb"

menu_item = ('lamb','bison','pork','brocolli','green beans')
print("We have changed our menu items. The new basic ingredients for this season are:")
for seasonal_foods in menu_item:
    print(seasonal_foods)