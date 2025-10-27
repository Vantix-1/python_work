# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#   - Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
#   - Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

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
}
print(f"Variable:\n\t{glossary['variable']}\n")
print(f"List:\n\t{glossary['list']}\n")
print(f"Dictionary:\n\t{glossary['dictionary']}\n")
print(f"Function:\n\t{glossary['function']}\n")
print(f"Loop:\n\t{glossary['loop']}\n")