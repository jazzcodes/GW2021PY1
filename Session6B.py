"""
    Functions -> can be created anywhere
    Methods   -> are created inside a class :)

    y = x*x + 1
    f(x) = y

    what is a function ?
        function is a piece of logic, which can be executed again and again
        we can write lot of code inside a function
        whatever we will write in a function will be executed in a sequence

    how to create a function ?
        a function is created with def keyword in python
        a function can take either no input or as many as we wish to send

    how can we execute a function ?
        name_of_function(...)

    WHY functions ?
        when we are writing the same code snippets again and again
        we need functions :)

        i.e. we wish to execute a piece of logic again and again :)
"""

# Defining a Function
def f(x):
    y = x*x + 1
    print("y is:", y)


# Execution
f(1)
f(10)

print("f is:", f, "hashcode is:", hex(id(f)))

my_fun = f # Reference Copy
print("my_fun is:", my_fun, "hashcode is:", hex(id(my_fun)))
my_fun(3)


def find_max(data):

    max = data[0]

    for number in data:
        if number > max:
            max = number

    # print("MAX IS:", max)
    return max
    # print("Awesome") # UNREACHABLE STATEMENT

marks = [75, 80, 50, 60, 88]
heights = [155, 145, 165, 135, 120, 133, 102, 121]
product_prices = [90, 92, 88, 89, 93, 91]

print(find_max(marks))
print(find_max(heights))
print(find_max(product_prices))

print(max(marks))
print(max(heights))
print(max(product_prices))

result = find_max(marks)


"""
# Assume
max = marks[0]
for number in marks:
    if number > max:
        max = number

print("max in marks is:", max)

max = heights[0]
for number in heights:
    if number > max:
        max = number

print("max in heights is:", max)

max = product_prices[0]
for number in product_prices:
    if number > max:
        max = number

print("max in product_prices is:", max)
"""

