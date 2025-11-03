# 8-8. User Albums: Start with your program from Exercise 8-7.
# -Write a while loop that allows users to enter an album’s artist and title.
# -Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
# -Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, songs=None):
    """"Returns a dictionary of information about an Album"""
    album ={'Artist':artist_name, 'Album':album_title}
    if songs:
        album['Songs'] = songs
    return album

while True:
    print("\n Please choose an artist and album you'd like to add:")
    print("(Enter 'q' to QUIT!)")
    artist = input("Artist: ")
    if artist == 'q':
        break
    album = input("Album: ")
    if album =='q':
        break
    new_album = make_album(artist,album)
    print(f"You've just added {new_album} to the dictionary.")
