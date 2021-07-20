# Nested Tuple, Nested List

# marks = ("john", (90, 80, 50), "jennie", (55, 95, 88))
# marks = ["john", [90, 80, 50], "jennie", [55, 95, 88]]

marks = ["john", (90, 80, 50), "jennie", (55, 95, 88)]

print(marks[0])
print(marks[1])
print(marks[1][0])
print(marks[1][1])
print(marks[1][2])

data1 = [10, 20, 30]
data2 = (10, 20, 30)

# Covert list to tuple and tuple to list
data3 = tuple(data1)
data4 = list(data2)