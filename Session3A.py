# Multi Value Containers => TUPLE
# Read only Storage Container -> IMMUTABLE
# numbers = 10, 20, 30, 40, 50
numbers = (10, 20, 30, 10, 50)

instagram_followers = "john", "jennie", "jim", "jack", "joe"

print(numbers, hex(id(numbers)))
print(instagram_followers, hex(id(instagram_followers)))

# print(numbers[0], hex(id(numbers[0])))
# print(numbers[1], hex(id(numbers[1])))
# print(numbers[2], hex(id(numbers[2])))
# print(numbers[3], hex(id(numbers[3])))
# print(numbers[4], hex(id(numbers[4])))

# Iteration -> For
# idx = 0
# while idx < 5:
#     print(numbers[idx], hex(id(numbers[idx])))
#     # idx = idx + 1
#     idx += 1

# Iteration -> For
for idx in range(0, 5):
    print(numbers[idx], hex(id(numbers[idx])))

print(instagram_followers[0], hex(id(instagram_followers[0])))

# ERROR
# UPDATE NOT ALLOWED
# numbers[0] = 100

# DELETE NOT ALLOWED
# del numbers[1]

numbers = 1.1, 2.2, 3.3, 4.4, 50, "jennie"
print(numbers, hex(id(numbers)))

# Here, now we have number referring to a new tuple
# Old tuple is now not referred by any reference variable and hence will be deleted from memory
