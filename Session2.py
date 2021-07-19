"""
    This is Session2 and is suppose to explore Model
    Here we will see Single Value and Multi Value Containers
    This documentation comment should always be in the beginning

    :author Ishant Kumar
    :email er.ishant@gmail.com
    :date 19th July, 2021
    :team ATPL Education
"""
# This is a comment

# __doc__ is a magic variable to see documentation of python module/script
print(__doc__)
print("Search the Candle rather than cursing the darkness")

"""
MODEL
1. Single Value Container
    Holds a single value
2. Multi Value Container
    Holds multiple values
        2.1 homo
        2.2 hetro
"""

# create a single value storage container in RAM
# store 10 in it
# put the hash code of 10 in a
# hence, a is a reference variable which will hold HashCode of 10
# CREATE/UPDATE
a = 10
b = 10

# READ
print("a is:", a, type(a), id(a), hex(id(a)), oct(id(a)), bin(id(a)))
print("b is:", b, type(b), id(b), hex(id(b)), oct(id(b)), bin(id(b)))

# UPDATE
# a = 20.22
# print("a now is:", a, type(a), id(a), hex(id(a)), oct(id(a)), bin(id(a)))
# print("b now is:", b, type(b), id(b), hex(id(b)), oct(id(b)), bin(id(b)))

# DELETE
# del a
# print("a is:", a, type(a), id(a), hex(id(a)), oct(id(a)), bin(id(a)))
# print("b is:", b, type(b), id(b), hex(id(b)), oct(id(b)), bin(id(b)))

numbers1 = 10, 20, 30, 40, 50
numbers2 = 10.22, 20, 30.33, 40, 50

print(numbers1, type(numbers1))
print(numbers2, type(numbers2))