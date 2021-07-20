# Multi Value Containers => LIST
# Read+Write Storage Container -> MUTABLE

numbers = [10, 20, 30, 10, 50]
print(numbers, type(numbers), hex(id(numbers)))

numbers[1] = 222
print(numbers, type(numbers), hex(id(numbers)))

del numbers[4]
print(numbers, type(numbers), hex(id(numbers)))

# append adds data in the list in the end
numbers.append(100)
print(numbers, type(numbers), hex(id(numbers)))

