"""
    Generator in Python
"""
# Upon execution of this function we will get generator as a result
def read_file(file_name=None):
    """
    yield 10
    yield 20
    yield 30
    """

    file = open(file_name, "r")
    for line in file.readlines():
        yield line


result = read_file(file_name="Session19C.py")
print(result, type(result))

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result, default="NA"))

# Generator can be iterated
for item in result:
    print(item, end="")

