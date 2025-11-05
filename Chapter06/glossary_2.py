# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    'variable':
        "A named container that stores a value in memory.",
    'list':
        "An ordered, mutable collection of items enclosed in square brackets.",
    'dictionary':
        "A collection of key-value pairs enclosed in curly braces.",
    'function':
        "A reusable block of code that performs a specific task, defined with def and called by name.",
    'loop':
        "A control structure that repeats a block of code multiple times, such as for loops or while loops.",
    'string':
        "A sequence of characters enclosed in quotes, used to represent text.",
    'integer':
        "A whole number without a decimal point, like 5 or -10.",
    'boolean':
        "A data type that can only be True or False, used for logical operations.",
    'tuple':
        "An ordered, immutable collection of items enclosed in parentheses.",
    'method':
        "A function that belongs to an object and is called using dot notation.",
}
#print(f"Variable:\n\t{glossary['variable']}\n")
#print(f"List:\n\t{glossary['list']}\n")
#print(f"Dictionary:\n\t{glossary['dictionary']}\n")
#print(f"Function:\n\t{glossary['function']}\n")
#print(f"Loop:\n\t{glossary['loop']}\n")

for word, definition in glossary.items():
    print(f"\n{word.title()}:")
    print(f"\t-{definition}")