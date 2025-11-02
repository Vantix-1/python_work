# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size 
# -and the text of a message that should be printed on the shirt. 
# -The function should print a sentence summarizing the size of the shirt and the message printed on it.
# -Call the function once using positional arguments to make a shirt. 
# -Call the function a second time using keyword arguments.

def make_shirts(size,message):
    """T-Shirt Maker, Choose Size and Message"""
    print(f"\nYou've chosen a size '{size}'")
    print(f"\tThe message on your T-shirt is: \n\t'{message}'")

make_shirts('L','Merry Christmas')
make_shirts(size='Large',message='Happy New Year!')