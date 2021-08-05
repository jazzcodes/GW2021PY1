# Re Defining a Function

def add_numbers(num1=10, num2=20):
    sum = num1 + num2
    print("sum of 2 inputs", sum)


print("add_numbers is:", add_numbers) # HashCode of Function

# Re Define
def add_numbers(num1=0, num2=0, num3=0):
    sum = num1 + num2 + num3
    print("sum of 3 inputs", sum)


print("add_numbers now is:", add_numbers) # HashCode
add_numbers(num1=10, num2=20)

def show():
    print("Welcome to MyApp")

def show(name):
    print("Welcome to Your App. Dear,", name)

# show() -> error
show("John")