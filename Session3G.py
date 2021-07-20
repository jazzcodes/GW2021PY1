# Use of Data Structures
restaurant = {
    "name": "Table By Basant",
    "cuisines": ["north indian", "chinese", "continental", "italian"],
    "timings": "11 AM to 11 PM",
    "delivery_reviews": 4.2,
    "user_reviews": 4.5,
    "image_url": "https://somehost.com/image.png"
}

dish1 = {
    "title": "Dal Makhani",
    "price": 200,
    "discount": 0.20,
    "votes": 3.5
}

dish2 = {
    "title": "Paneer",
    "price": 350,
    "discount": 0.20,
    "votes": 4.5
}

dish3 = {
    "title": "Noodles",
    "price": 250,
    "discount": 0.20,
    "votes": 2.5
}

dish4 = {
    "title": "Burger",
    "price": 150,
    "discount": 0.20,
    "votes": 5.0
}

dish5 = {
    "title": "Platter",
    "price": 300,
    "discount": 0.20,
    "votes": 3.5
}

menu = [dish1, dish2, dish3, dish4, dish5]

restaurant["menu"] = menu

print(restaurant)

# Assignment:
# Represent COVID 19 data in data structures
# https://www.covid19india.org/