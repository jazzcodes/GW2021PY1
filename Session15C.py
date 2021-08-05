"""
    Pass Functions as Arguments
    Return Functions from Functions
    Nested Functions
"""

def welcome():
    print("-----------------")
    print("Welcome to MyApp")
    print("-----------------")

def welcome_v2():
    print("-----------------")
    print("Hello, Welcome All")
    print("-----------------")


def home_page(any_name):
    any_name()
    # print(any_name)
    # print(type(any_name))
    print("This is Home Page. Explore Latest Deals")

def profile_page(any_name):
    any_name()
    # print(any_name)
    # print(type(any_name))
    print("This is Profile Page. Manage Your Profile")


header = welcome_v2

home_page(any_name=header)
profile_page(any_name=header)


# Function Returning Function
def hello():
    return welcome_v2

result = hello()
result() # executable :)

def outer():
    print("This is from outer")

    def inner():
        print("This is from inner")

    inner()

    return inner

result = outer()
result()

