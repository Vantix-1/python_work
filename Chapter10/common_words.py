# 10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org) and find a few texts you’d like to analyze. Download the text files for these works, or copy the raw text from your browser into a text file on your computer.
# You can use the count() method to find out how many times a word or phrase appears in a string. For example, the following code counts the number of times 'row' appears in a string:
# Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text. This will be an approximation because it will also count words such as 'then' and 'there'. Try counting 'the ', with a space in the string, and see how much lower your count is.

from pathlib import Path

def common_words(filename):
    """Search text for common words"""
    try:
        contents = filename.read_text(encoding='utf-8')
        count_the = contents.count('the')
        count_the_space= contents.count('the ')
        print(f"  'the' appears: {count_the} times")
        print(f"  'the ' (with space) appears: {count_the_space} times")
        print(f"  Difference: {count_the - count_the_space} occurrences")

        return count_the_space
    except FileNotFoundError:
        print(f"Sorry {filename} was not found.")
        return None

filename = Path('Chapter10/theonlineworld.txt')
common_words(filename)