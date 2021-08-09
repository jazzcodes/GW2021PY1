file = open("Session17B.py", "r")
# contents = file.read()

# contents = file.read(10) # 1st 10 characters
# print(contents)
#
# contents = file.read(20) # from 11th till 20th
# print(contents)

# print(type(contents))

# Move Cursor to 10
# file.seek(10)
# cursor_position = file.tell()
# print("cursor_position:", cursor_position)
# contents = file.read()
# print(contents)

# cursor_position = file.tell()
# print("cursor_position:", cursor_position)
# contents = file.read()
# cursor_position = file.tell()
# print("cursor_position now:", cursor_position)
#
# contents = file.read()
# print("contents:", contents)

lines = file.readlines()
print(lines)
print(len(lines))
print(type(lines))

for_loops = 0
for line in lines:
    print(line)
    if "for" in line:
        for_loops += 1

# Assignment -> Write Algo to find nested for loop :)

print("Total For Loops Found:", for_loops)

# Project #1
# Source Code Generator Like Siri/Alexa
# i.e. create a BOT

# Project #2
# Cource Code Analysis i.e. Profiling
# Tell/Compute the time complexity of Program