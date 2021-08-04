from Session14A import Dish
"""
    Stack
        PUSH: Element will always be added in the end
        POP: Element will always be removed from the end
        ITERATE: Backward :)
        
        LIFO -> Last In , First Out
        
    Queue
        PEEK: Return the Head of Queue
        POLL: Remove the Head of Queue
        
        FIFO -> Fisrt In, First Out
"""

class Stack:

    size = 0
    idx = 0

    def __init__(self):
        self.head = None
        self.tail = None # current object

    def push(self, object):

        Stack.size += 1
        object.index = Stack.idx
        Stack.idx += 1

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

    def iterate(self):
        temporary = self.tail

        while True:
            # print(vars(temporary))
            # temporary.show_song()
            print(temporary)
            temporary = temporary.previous

            if temporary is self.tail:
                break

    def length(self):
        return Stack.size

    def pop(self):

        Stack.size -= 1

        last_object = self.tail
        self.tail = last_object.previous
        self.tail.next = self.head
        self.head.previous = self.tail

        del last_object


class Queue:

    size = 0
    idx = 0

    def __init__(self):
        self.head = None
        self.tail = None # current object

    def append(self, object):

        Queue.size += 1
        object.index = Queue.idx
        Queue.idx += 1

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

    def iterate(self):
        temporary = self.head

        while True:
            # print(vars(temporary))
            print(temporary)
            temporary = temporary.next

            if temporary is self.head:
                break

    def peek(self):
        return self.head

    def length(self):
        return Queue.size

    def poll(self):
        first_object = self.head
        self.head = first_object.next
        self.head.previous = self.tail
        self.tail.next = self.head

        del first_object

        # self.update_indexes(0)



def main():

    dish1 = Dish("Dal Makhani", 200, 1)
    dish2 = Dish("Paneer Makhani", 300, 1)
    dish3 = Dish("Butter Nan", 50, 1)
    dish4 = Dish("Burger", 50, 1)
    dish5 = Dish("Noodles", 150, 1)

    stack = Stack()
    stack.push(dish1)
    stack.push(dish2)
    stack.push(dish3)
    stack.push(dish4)
    stack.push(dish5)

    stack.iterate()
    stack.pop()
    print("~~~~~~~~~~")
    stack.iterate()

    print("~~~~~~~~~~")
    print("~~~~~~~~~~")

    queue = Queue()
    queue.append(dish1)
    queue.append(dish2)
    queue.append(dish3)
    queue.append(dish4)
    queue.append(dish5)

    queue.poll()
    queue.iterate()

    print("FIRST OBJECT:", queue.peek())

if __name__ == '__main__':
    main()