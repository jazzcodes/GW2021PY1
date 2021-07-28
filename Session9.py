"""
    Sequences in Python
    List
    Tuple
    Set
    Dictionary
    String

    Properties of Sequences
    1. Indexing
    2. Negative Indexing
    3. Slicing
    4. Concatenation
    5. Multiplicity
    6. Membership Testing

"""

"""
class User:

    def register(self):
        print("User Registered")

    def get_age(self):
        return 15


user1 = User()
user1.register()
print(user1.get_age())
"""

# List
# Empty List
# my_data = []
# List with Data
my_data = [10, 20, 30]
print(type(my_data), hex(id(my_data)), len(my_data))
print(max(my_data), min(my_data))

# Hetro
my_data = [1, "John", 15, "Redwood Shores", 85.7]
# print(max(my_data), min(my_data)) -> Error

# Nested List
my_data = ["john", [70, 67, 88], "fionna", [77, 95, 89]]
print(len(my_data))
print(len(my_data[0]))
print(len(my_data[1]))

# Negative Indexing
print(my_data[0]) # john
print(my_data[1]) # -> [70, 67, 88]
print(my_data[1][2])

print(my_data[-1])
print(my_data[-2])

print(my_data[-1][-2])

# Slicing
# numbers = [10, 20, 30, 40, 50]
numbers = list(range(10, 101, 10))
print(numbers)
print(numbers[5:])  # from 5 to end
print(numbers[: 3]) # beginning to less than 3
print(numbers[3:7]) # from 3 to 6 i.e. less than 7

print(numbers[: -5]) # 10 to 50
print(numbers[-5: -2])

# Concatenation
data1 = [10, 20, 30]
data2 = [40, 50, 60]

data3 = data1 + data2

print("data1:", data1)
print("data2:", data2)
print("data3:", data3)

data4 = data1 * 3
print("data4:", data4)

print(10 in data4)
print(100 in data4)

print(200 not in data4)