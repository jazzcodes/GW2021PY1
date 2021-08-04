# import Session14B
from Session14B import LinkedList

class Dish:

    dishes = 0 # property of class

    def __init__(self, name=None, price=None, quantity=None):
        Dish.dishes += 1

        self.index = -1
        self.name = name
        self.price = price
        self.quantity = quantity

    def increment(self):
        self.quantity += 1

    def decrement(self):
        self.quantity -= 1

    def __str__(self):
        return "[{}] {} | {} | {}".format(self.index, self.name, self.price, self.quantity)


def main():

    dish1 = Dish("Dal Makhani", 200, 1)
    dish2 = Dish("Paneer Makhani", 300, 1)
    dish3 = Dish("Butter Nan", 50, 1)
    dish4 = Dish("Burger", 50, 1)
    dish5 = Dish("Noodles", 150, 1)

    # menu = []
    # menu.append(dish1)
    # menu.append(dish2)
    # menu.append(dish3)
    # menu.append(dish4)
    # menu.append(dish5)
    #
    # for dish in menu:
    #     print(dish)


    menu = LinkedList()

    menu.append(dish1)
    menu.append(dish2)
    menu.append(dish3)
    menu.append(dish4)
    menu.append(dish5)

    print("MENU [{}]".format(menu.length()))
    menu.iterate_forward()

    dish = menu.get_object(2)
    print("DISH OBJECT DETAILS:", dish)

    # cart = LinkedList()
    # print(vars(cart))

if __name__ == '__main__':
    main()