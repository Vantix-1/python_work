# 10-8.	Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file.
# -Write a program that tries to read these files and print the contents of the file to the screen
# -Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing.
# -Move one of the files to a different location on your system, and make sure the code in the except block executes properly.

from pathlib import Path
def pet_names(filename):
    """Show stored pet names"""
    try:
        path = Path(filename)
        contents = path.read_text(encoding='utf-8').strip()
    except FileNotFoundError:
        print(f"Sorry {filename} could not be found")
    else:
        if 'dog' in filename:
            print('\nPet names for dogs:')
        elif 'cat' in filename:
            print('\nPet names for cats:')
        else:
            print(f"\nPet names from {filename}")
        print(contents)

petnames = ['Chapter10/dogs.txt', 'cats.txt']
for petname in petnames:
    pet_names(petname)