import array

# 3 Properties
# 1. Fixed Size
# 2. Homogeneous
# 3. Mutable

# Reference Link to array for making arrays of different types
# https://docs.python.org/3/library/array.html
numbers = array.array('i', (10, 20, 30, 40, 50))
print(numbers, type(numbers), hex(id(numbers)))

numbers[0] = 100
print(numbers[0])

print(numbers, type(numbers), hex(id(numbers)))