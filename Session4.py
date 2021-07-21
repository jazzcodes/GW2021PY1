
student = {
    "roll": 101,
    "name": "John",
    "email": "john@example.com",
    "age": 20,
    "college": {
        "name": "GNDEC",
        "address": "Gill Road",
        "phone": "0161 - 5454422",
    }
}

marks = [97, 68, 88]

student["marks"] = marks

print(student)

keys = list(student.keys())

print(keys)

# for key in keys:
#     # print(key, student[key])
#     print("KEY:", key, "VALUE:", student[key])

for i in range(0, len(keys)):
    print("KEY:", keys[i], "VALUE:", student[keys[i]])