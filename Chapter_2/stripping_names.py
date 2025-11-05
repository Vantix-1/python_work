# 2-7. Stripping Names: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

first_name = " \tjohn"
last_name = "\ncena  "
full_name = f"{first_name} {last_name}"
#print(full_name)
#print(full_name.lstrip())
#print(full_name.rstrip())
print(full_name.strip().title())
