class LinkedList:

    size = 0
    idx = 0

    def __init__(self):
        self.head = None
        self.tail = None # current object

    def append(self, object):

        LinkedList.size += 1
        object.index = LinkedList.idx
        LinkedList.idx += 1

        if self.head is None:
            self.head = object
            self.tail = object
            # print("OBJECT ADDED AS HEAD AND TAIL")
        else:
            # let the next object of tail be the object which we are adding
            self.tail.next = object
            # let the object which we are adding has its previous as tail i.e. the last object added
            object.previous = self.tail

            self.head.previous = object

            self.tail = object
            self.tail.next = self.head
            # print("OBJECT ADDED AS TAIL")

    def iterate_forward(self):
        temporary = self.head

        while True:
            # print(vars(temporary))
            print(temporary)
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

    # Linear Search Algorithm
    def get_object(self, index):

        object = None

        temporary = self.head

        while True:

            if temporary.index == index:
                object = temporary
                break

            temporary = temporary.next

            if temporary is self.head:
                break

        return object


    def remove_first(self):
        pass

    def remove_last(self):
        pass

    def remove(self, index):
        pass