"""
    value vs reference
    search sort filter
    functions
"""

a = 10
b = a # Reference Copy -> Single Value Container

print("a is:", a, "hashcode is:", hex(id(a)))
print("b is:", b, "hashcode is:", hex(id(b)))

# Manipulation results in new object in memory
# hence, b will refer to a new object
b += 5

print("a now is:", a, "hashcode is:", hex(id(a)))
print("b now is:", b, "hashcode is:", hex(id(b)))