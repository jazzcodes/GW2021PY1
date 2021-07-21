"""
    CONTROLLER -> makes the algorithm
        1. Computation
            Operators
        2. Logical Decisions
            if/else, switch case
        3. Iterations
            for, while
"""
# Arithmetic Operators: +, -, *, **, /, //, %
num1 = 10
num2 = 20
num3 = num1 + num2

num4 = 3
num5 = num1 / num4      # floating point division
num5 = num1 // num4     # integral division
print(num5)

# Hashing :)
# hashfunction(data) -> hashcode
# f(x) = x*x + 1
# buckets = 13
# h(x) = x % buckets

bucket_size = 13
number = 100
hash_code = number % bucket_size
print("HashCode is:", hash_code)

result = 2**3
print("result is:", result)

# Assignment Operators: +=, -=, *=, **=, /=, //=, %=
quantity = 10
# quantity = quantity + 2
quantity += 2

quantity %= 3 # quantity = quantity % 3
print(quantity)

# Conditional Operators
# >, <, >=, <=, ==, !=

e_wallet = 300
cab_fare = 400

print("Can i book a cab? ", (cab_fare <= e_wallet))

# Logical Operators
# and or not
internet = False
gps = True

print("Can i Navigate on Google Maps:", (internet and gps))

# is and is not
print(e_wallet is not cab_fare)

# Bitwise Operators
# &, | ^

num1 = 8
num2 = 10
print(bin(num1))
print(bin(num2))
num3 = num1 & num2
print(bin(num3))
print("num3:", num3)

num4 = num1 | num2
print(bin(num4))
print("num4:", num4)

num5 = num1 ^ num2
print(bin(num5))
print("num5:", num5)

# Assignment: Explore a cryptography algorithm which uses bitwise operators

# Shift Operators
# >> <<
num1 = 8
num2 = 2

num3 = num1 >> 2    # divide num by 2 power n
num4 = num1 << 2    # multiply num by 2 power n
print("num3 is:", num3)
print("num4 is:", num4)

amount = 8
secret = 2

result1 = amount >> secret
print("result1:", result1)
result2 = result1 << secret
print("result2:", result2)

"""
    1 0 0 0
    >> 2
    _ _ 1 0
    0 0 1 0 -> 2
    
    0 0 0 0 1 0 0 0 
    << 2
    0 0 1 0 0 0 _ _
    0 0 1 0 0 0 0 0
"""
num1 = -11
num2 = 2
result = num1 >> num2
print("result is:", result)
"""
    11 -> 1 0 1 1
          0 1 0 0
                1
   -11 -> 0 1 0 1
   
   >> 2
          _ _ 0 1
          1 1 0 1
          
          0 0 1 0
                1
          0 0 1 1 -> -3            
"""

# Membership Testing | in, not in
data = [10, 20, 30]
print(10 in data)
print(100 not in data)



