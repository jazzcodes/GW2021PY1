

base_fare = 50
type_of_cab = input("Enter Type of Cab: ")

cabs = {"mini": 50, "sedan": 100, "bike": 20}

print("Please Pay: \u20b9", base_fare+cabs.get(type_of_cab, -base_fare))

"""
if type_of_cab in cabs:
    print(type_of_cab, "booked. Please pay: \u20b9", base_fare+cabs[type_of_cab])
else:
    print("Please Select the Cab to Proceed")
"""

"""
# Ladder if/else
if type_of_cab == "mini":
    base_fare += 50
    print("MINI CAB BOOKED. Please Pay \u20b9", base_fare)
elif type_of_cab == "sedan":
    base_fare += 100
    print("SEDAN BOOKED. Please Pay \u20b9", base_fare)
elif type_of_cab == "bike":
    base_fare += 20
    print("BIKE BOOKED. Please Pay \u20b9", base_fare)
else:
    print("Please Select the Cab to Proceed")
"""

# Python has no switch case.
# rather we can use dictionary to make a switch case
switch = {
    1: "upi",
    2: "net banking",
    3: "debit card",
    4: "credit card",
    5: "cash"
}

print(switch)
print(type(switch))

print(switch.get(13, "Invalid Choice"))

print("THANK YOU :)")


