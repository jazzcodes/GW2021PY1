class Dish:

    # property of class
    dishes = 0

    def __init__(self, name="NA", price=0):
        # self.name and self.price -> property of object
        self.name = name
        self.price = price
        Dish.dishes += 1


def main():
    dish1 = Dish("Dal Makhani", 200)
    dish2 = Dish("Paneer Makhani", 300)
    # dish1.name = "Dal Makhani"
    # dish1.price = 200

    Dish.dishes = 100

    print("data for dish1:", vars(dish1))
    print("data for class Dish: ", vars(Dish))


if __name__ == '__main__':
    main()