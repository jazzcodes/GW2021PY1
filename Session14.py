class Dish:

    # Constructor
    """
    def __init__(self, price=None, quantity=None):
        # self contains the HashCode of the Object
        self.name = input("Enter Dish Name: ")
        self.price = price
        self.quantity = quantity
    """

    dishes = 0 # property of class

    def __init__(self, name=None, price=None, quantity=None):
        Dish.dishes += 1
        # self contains the HashCode of the Object
        self.name = name
        self.price = price
        self.quantity = quantity

    def increment(self):
        self.quantity += 1

    def decrement(self):
        self.quantity -= 1

def main():
    dish1 = Dish("Dal Makhani", 200, 1)
    dish2 = Dish("Paneer Makhani", 300, 1)
    dish3 = dish1

    print(vars(dish1), hex(id(dish1)))
    print(vars(dish2), hex(id(dish2)))
    print(vars(dish3), hex(id(dish3)))

    dish1.increment()
    dish2.increment()
    dish3.increment()

    dish1.increment()
    dish2.increment()

    dish3.decrement()
    dish1.decrement()

    dish2.increment()

    print(vars(dish1)) # quantity 2, 1
    print(vars(dish2)) # quantity 4, 3
    print(vars(dish3)) # quantity 2, 1
    print(vars(Dish))  # dishes 2


if __name__ == '__main__':
    main()