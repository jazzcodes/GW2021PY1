def area_of_circle(radius):
    return 3.14 * radius * radius

# Reference Copy
func = area_of_circle

print(area_of_circle(5))
print(area_of_circle(7))
print(func(7))

print()

# Anonymous Function
# Lambdas will compute an expression and return the result
# ref = lambda radius: 3.14 * radius * radius
ref = lambda radius=2: 3.14 * radius * radius
print("ref:", ref)
print(ref(5))
print(ref(7))
print(ref())

ref = lambda x=2, y=2: x**y
print(ref())
print(ref(y=4))
print(ref(x=3, y=4))

# ref = lambda amount=100, taxes = 0.18: amount + (amount*taxes)
# print(ref())
# print(ref(amount=1000, taxes=0.25))

ref = lambda amount=float(input("Enter Amount: ")), taxes = float(input("Enter Taxes: ")): amount + (amount*taxes)
print(ref())

ref1 = lambda x, y: x+y
ref2 = lambda a, b: a*b

ref3 = lambda p, q: ref1(p, q) ** ref2(p, q)
print(ref3(2, 2))
