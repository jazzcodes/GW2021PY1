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
        first_object = self.head
        self.head = first_object.next
        self.head.previous = self.tail
        self.tail.next = self.head

        del first_object

        # self.update_indexes(0)

    def remove_last(self):

        LinkedList.size -= 1
        LinkedList.idx -= 1

        last_object = self.tail
        self.tail = last_object.previous
        self.tail.next = self.head
        self.head.previous = self.tail

        del last_object

    def remove(self, index):

        if index == 0:
            self.remove_first()
        elif index == LinkedList.size-1:
            self.remove_last()
        else:
            object_to_delete = self.get_object(index)
            object_to_delete.previous.next = object_to_delete.next
            object_to_delete.next.previous = object_to_delete.previous

            del object_to_delete

            # self.update_indexes(index)

        # Assignment -> Manage Indexing i.e. update indexes of the elements afterwardss

    def update_indexes(self, start_index):
        pass

    def insert(self, index):
        pass