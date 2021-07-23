"""
    Search Sort and Filter
"""

drivers = [
    {
        "name": "John",
        "status": 0,
        "distance": 5
    },
    {
        "name": "George",
        "status": 1,
        "distance": 15
    },
    {
        "name": "Fionna",
        "status": 1,
        "distance": 3
    },
    {
        "name": "Lee",
        "status": 1,
        "distance": 8
    },
    {
        "name": "Mike",
        "status": 1,
        "distance": 14
    },
    {
        "name": "Leo",
        "status": 1,
        "distance": 7
    },
]

print("DRIVERS")
for driver in drivers:
    print("~" * 10)
    print("{name}\n{status} | {distance}".format_map(driver))
    print("~" * 10)
    print()

print("SEARCH THE DRIVER")
status = int(input("Enter Offline(0) Online(1) Status: "))
distance = int(input("Enter Distance: "))

found = False

for driver in drivers:
   if driver["status"] == status and driver["distance"] == distance:
       print("*" * 10)
       print("{name}\n{status} | {distance}".format_map(driver))
       print("*" * 10)
       found = True
       break

if not found:
    print("Sorry! Driver Not Found")


print("FILTER THE DRIVERS")
filter1 = int(input("Enter filter1 for status(0/1) :"))
filter2 = int(input("Enter filter2 for distance :"))

for driver in drivers:
   if driver["status"] == filter1 and driver["distance"] <= filter2:
       print("*" * 10)
       print("{name}\n{status} | {distance}".format_map(driver))
       print("*" * 10)

# SORTING
# https://visualgo.net/en/sorting
"""
numbers = [10, 20, 15, 8, 11]
print("numbers before is:", numbers)
# SORTED IN DESCENDING ORDER
for i in range(0, len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("numbers after is:", numbers)
"""
print("SORTED DRIVERS")
for i in range(0, len(drivers)):
    for j in range(0, len(drivers) - i - 1):
        if drivers[j]["distance"] > drivers[j+1]["distance"]:
            drivers[j], drivers[j+1] = drivers[j+1], drivers[j]

for driver in drivers:
    print("^" * 10)
    print("{name}\n{status} | {distance}".format_map(driver))
    print("^" * 10)


