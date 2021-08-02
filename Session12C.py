"""
    Song is Object
        track, artists, duration, next_song, previous_song
"""

# User Defined Data Type
class Song:

    # Constructor :) -> Whenever object is created in memory
    # self is a reference variable
    # it refers to the current object
    def __init__(self, name=None, artist=None, duration=None, next_song=None, previous_song=None):
        self.name = name
        self.artist = artist
        self.duration = duration
        self.next_song = next_song
        self.previous_song = previous_song


song1 = Song("Sach Keh Raha Hai", "John", 4.5)
song2 = Song("Bimariyan", "Fionna", 3.55)
song3 = Song("Permission to Dance", "Kim", 5.0)

song1.next_song = song2
song1.previous_song = song3

song2.next_song = song3
song2.previous_song = song1

song3.next_song = song1
song3.previous_song = song2

# Forward Iteration
# Reference Copy
song = song1

while song.next_song != song1:
    print("-" * 30)
    print("{}\t{}\t{}".format(song.name, song.artist, song.duration))
    print("-" * 30)
    print()

    song = song.next_song

print("-" * 30)
print("{}\t{}\t{}".format(song.name, song.artist, song.duration))
print("-" * 30)
print()

# song1, song2 and song3 are reference variables
# they are referring to the Objects in the memory
"""
song1.name = "Sach Keh Raha Hai"
song1.artist = "John"
song1.duration = 4.5
song1.next_song = song2
song1.previous_song = song3

song2.name = "Bimariyan"
song2.artist = "Fionna"
song2.duration = 3.55
song2.next_song = song3
song2.previous_song = song1

song3.name = "Permission to Dance"
song3.artist = "Kim"
song3.duration = 5.0
song3.next_song = song1
song3.previous_song = song2

print(song1)
print(song2)
print(song3)
"""

# print("Data for song1:", vars(song1))
# print("Data for song2:", song2.__dict__)
# print("Data for song3:", song3.__dict__)

