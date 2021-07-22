menu = {
    "Burger": {
        "title":  "Veggie Spicy Burger",
        "price": 100,
        "delivery": 20
    },
    "Noodles": {
        "title":  "Chilli Garlic Noodles",
        "price": 200,
        "delivery": 10
    },
    "Platter": {
        "title":  "Chinese Veg Platter",
        "price": 300,
        "delivery": 30
    },
    "Dal": {
        "title":  "Dal Makhani",
        "price": 200,
        "delivery": 5
    },
    "Paneer": {
        "title":  "Paneer Butter Masala",
        "price": 300,
        "delivery": 12
    }
}

print("MENU")
# All the keys of menu dictionary
keys = list(menu.keys())

for key in keys:
    print("-" * 40)
    print("{}\t\t \u20b9{}".format(menu[key]['title'], menu[key]['price']))
    print("-" * 40)
    print()


shopping_cart = []
total = 0

while True:
    choice = input("Enter the Dish to Order: (no to quit)")

    if choice == "no":
        break

    if choice in menu:
        total += menu[choice]['price']
        shopping_cart.append(menu[choice])
    else:
        print("Sorry! We do not have this", choice, "at the moment")

print("SHOPPING CART [{}] ".format(len(shopping_cart)))
print("PLEASE PAY [\u20b9{}] ".format(total))
print(shopping_cart)
