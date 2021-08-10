# Has-A Relation
# in one object we can have a reference to another object
# 1 to 1
# 1 to many
# many to many

class Menu:

    def __init__(self, name, dishes, num_of_dishes):
        self.name = name
        self.dishes = dishes # 1 to many
        self.num_of_dishes = num_of_dishes


class Dish:

    dishes = []

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    @classmethod
    def generate_dishes(cls):

        file = open("dishes.csv", "r")
        for line in file.readlines():
            data = line.split(",")
            ref = cls(int(data[0]), data[1], float(data[2]))
            cls.dishes.append(ref)

def main():
    Dish.generate_dishes()

    # HAS-A Relationship
    # 1 to many relationship
    menu = Menu(name="Veg Indian Menu", dishes=Dish.dishes, num_of_dishes=len(Dish.dishes))