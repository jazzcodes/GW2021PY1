# Set
john_followers = {"fionna", "jim", "mike", "sia", "kim", "mike"}
print(john_followers)

list_numbers = list(range(10, 101, 10))
list_numbers.append(20)
list_numbers.append(50)
print(list_numbers)

set_numbers = set(list_numbers)
print(set_numbers)

set_numbers.add(101)
set_numbers.add(70)

print(set_numbers)

# set_numbers.update({1, 2, 3, 4, 5})
# set_numbers.update((11, 22, 33, 44, 55), {1, 2, 3, 4, 5})
set_numbers.update([11, 22, 33, 44, 55], {1, 2, 3, 4, 5})
print(set_numbers)

set_numbers.pop()
set_numbers.pop()
print(set_numbers)

print(len(set_numbers))
print(max(set_numbers))
print(min(set_numbers))

# set_numbers.remove(101)
set_numbers.discard(101)
print(set_numbers)

# set_numbers.remove(101)
set_numbers.discard(101)

john_followers = {"fionna", "jim", "mike", "sia", "kim", "mike"}
fionna_followers = {"jim", "kim", "mike"}
george_followers = {"harry", "jim", "kim", "mike", "ron"}
print("john_followers", john_followers)
print("fionna_followers", fionna_followers)
print("george_followers", george_followers)

# followers = john_followers.union(george_followers)
followers = john_followers.intersection(george_followers)
print(followers)

print(fionna_followers.issubset(john_followers))
print(john_followers.issuperset(fionna_followers))

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# C = A - B
# C = A.difference(B)

# C = A.symmetric_difference(B)
# C = A ^ B
# C = A | B
C = A & B
print(C)

# Frozen Set
data = (1, 2, 3, 4, 5, 1, 2)
f_set = frozenset(data)
print(f_set, type(f_set))

# Remove all elements from Set
C.clear()

# Enhanced For Loop, For Each Loop
for element in f_set :
    print(element)