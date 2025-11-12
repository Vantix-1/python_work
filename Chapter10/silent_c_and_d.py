# 10-9.	Silent Cats and Dogs: Modify your except block in Exercise 10-7 to fail silently if either file is missing.

from pathlib import Path
def pet_names(filename):
    """Show stored pet names"""
    try:
        path = Path(filename)
        contents = path.read_text(encoding='utf-8').strip()
    except FileNotFoundError:
        pass
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