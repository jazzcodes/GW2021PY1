numbers = [10, 20, 30, 40, 50]
my_numbers = numbers # Reference Copy -> Multi Value Container

print("numbers is:", numbers, "and hashcode is:", hex(id(numbers)))
print("my_numbers is:", my_numbers, "and hashcode is:", hex(id(my_numbers)))

print("DATA IN NUMBERS BEFORE")
for number in numbers:
    print(number, hex(id(number)))

print("DATA IN MY NUMBERS BEFORE")
for number in my_numbers:
    print(number, hex(id(number)))

print()

for i in range(len(my_numbers)):
    my_numbers[i] += 5

print("numbers now is:", numbers, "and hashcode is:", hex(id(numbers)))
print("my_numbers now is:", my_numbers, "and hashcode is:", hex(id(my_numbers)))

print("DATA IN NUMBERS AFTER")
for number in numbers:
    print(number, hex(id(number)))

print("DATA IN MY NUMBERS AFTER")
for number in my_numbers:
    print(number, hex(id(number)))