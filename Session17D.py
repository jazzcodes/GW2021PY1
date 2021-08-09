from Session17 import Student

file = open("students.csv", "r")
lines = file.readlines()
students = []

for line in lines:
    # print(line, type(line))
    # DeSerialization
    data = line.split(",")
    student = Student(
        roll=int(data[0]),
        name=data[1],
        age=int(data[2]),
        gender=data[3],
        phone=data[4],
        standard=int(data[5])
    )
    students.append(student)

print(students)
for student in students:
    print(vars(student))
