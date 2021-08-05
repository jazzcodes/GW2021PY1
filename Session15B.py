"""
    Variable Arguments
    *args

    Keyword Arguments
    **kwargs
"""
# def add_numbers(*args):
# def add_numbers(*kuchbhinaam):

def add_numbers(*numbers):
    print(numbers)
    print(type(numbers))
    print(sum(numbers))


add_numbers(10, 20, 30)
add_numbers(10, 20, 30, 40, 50)
add_numbers(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

def add_numbers(numbers):
    print(numbers)
    print(type(numbers))

# add_numbers(10, 20, 30)
add_numbers(numbers=(10, 20, 30))


# def plot_map(**kwargs):
# def plot_map(**kuchbhinaam):

def plot_graph(**options):
    print(options)
    print(type(options))


plot_graph(color="red", x=100, y=100, type="line")

def fun(*args, **kwargs):
    print("args:", args, type(args))
    print("kwargs:", kwargs, type(kwargs))


fun(10, 20, 30, a=10, b=20, c=30)