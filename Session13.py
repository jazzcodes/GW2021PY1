"""
    Dynamic List with links created automatically
    with programming approach
"""


# User Defined Data Type
class Song:

    def __init__(self, name=None, artist=None, duration=None):
        self.name = name
        self.artist = artist
        self.duration = duration

    def show_song(self):
        print("{name}\t{artist}\t{duration}".format_map(vars(self)))

    def __str__(self):
        return "{name}\n{artist}\t{duration}\n".format_map(vars(self))




class LinkedList:

    size = 0
    idx = 0

    def __init__(self):
        self.head = None
        self.tail = None # current object

    def append(self, object):

        LinkedList.size += 1

        if self.head is None:
            self.head = object
            self.tail = object
            # object.index = LinkedList.idx
            # LinkedList.idx += 1
            print("OBJECT ADDED AS HEAD AND TAIL")
        else:
            # let the next object of tail be the object which we are adding
            self.tail.next = object
            # let the object which we are adding has its previous as tail i.e. the last object added
            object.previous = self.tail

            self.head.previous = object

            self.tail = object
            self.tail.next = self.head
            print("OBJECT ADDED AS TAIL")


    def iterate_forward(self):
        temporary = self.head

        while True:
            print(vars(temporary))
            temporary = temporary.next

            if temporary is self.head:
                break

    def iterate_backward(self):
        temporary = self.tail

        while True:
            # print(vars(temporary))
            # temporary.show_song()
            print(temporary)
            temporary = temporary.previous

            if temporary is self.tail:
                break

    def length(self):
        return LinkedList.size

    def sort(self, reverse=False):
        pass

def main():

    song1 = Song("1 Sach Keh Raha Hai", "John", 4.5)
    song2 = Song("2 Bimariyan", "Fionna", 3.55)
    song3 = Song("3 Permission to Dance", "Kim", 5.0)
    song4 = Song("4 Kal ho na ho", "Sonu", 4.0)
    song5 = Song("5 Baarish", "Someone", 4.5)

    # Python Built In
    # play_list = list()
    # play_list = []
    # play_list.append(song1)
    # play_list.append(song2)
    # play_list.append(song3)

    # User Defined :)
    play_list = LinkedList() # __init_ will be executed automatically
    print(vars(play_list))

    # Add the Object
    play_list.append(song1)
    play_list.append(song2)
    play_list.append(song3)
    play_list.append(song4)
    play_list.append(song5)

    play_list.iterate_forward()
    print("~~~~~~~~~~~~~~~~")
    play_list.iterate_backward()

    print("Lenth of LinkedList:", play_list.length())

if __name__ == '__main__':
    main()

# Assignment: Implement Bubble Sort on LinkedList :)