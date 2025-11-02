# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# -Make a large shirt and a medium shirt with the default message, 
# -and a shirt of any size with a different message.

def make_shirts(size='Large',message='I Love Python!'):
    """T-Shirt Maker, Choose Size and Message"""
    print(f"\nYou've chosen a size '{size}'")
    print(f"\tThe message on your T-shirt is: \n\t'{message}'")

make_shirts()
make_shirts(size='Medium')
make_shirts(size='XL',message='Python Rocks!')