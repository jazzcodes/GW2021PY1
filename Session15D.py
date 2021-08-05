"""
    META PROGRAMMING
        Decorators
"""


# Function is taking another function as input
def header(func):
    # Inner/Nested Function is returning the function as input to Outer Function
    def menu_bar():
        print("-"*30)
        print("File  Edit  View  Navigate  Code")
        print("-" * 30)
        func() # execute

    return menu_bar

# Rule: 1. Function must take a Function as Input
# Rule: 2. Function must have an internal/nested function
# Rule: 3. internal/nested function must execute the function passed as input to the outer function
# Rule: 4. outer function should return the inner function

@header
def home():
    print("Welcome to My App")
    print("John Watson")

# result = header(func=home)
# result()

home()
