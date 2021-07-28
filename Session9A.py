
numbers = list(range(10, 101, 10))
numbers.append(70)
numbers.append(70)
numbers.append(30)
print(numbers)

reversed_numbers = list(reversed(numbers))
print(sorted(reversed_numbers))

print(numbers)
print(reversed_numbers)

print(numbers.index(50))
print(numbers.count(70))

print()

data = [70, 30, 50, 10, 20]
print(data)
data.sort()
print(data)

data.reverse()
print(data)

data.remove(50)
print(data)

data.pop(1)
print(data)

data.pop()
print(data)

data.append(100)
print(data)

data.insert(2, 77)
print(data)

# remove all elements from list
data.clear()
print(data, len(data))

