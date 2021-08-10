# What is Inheritance ?
# IS-A Relationship -> Parent and Child
# Parent: John Watson
# Child: Fionna Watson
# Hence Fionna IS-A Watson :)

class Parent:

    def __init__(self):
        print("Parent Object Constructed")
        print("self is:", self)
        print("type of self is:", type(self))

    def show(self):
        print("Show of Parent")


# Inheritance
class Child(Parent):

    def __init__(self):
        print("Child Object Constructed")
        print("self is:", self)
        print("type of self is:", type(self))

    # Re Defining the Same Function
    # Overriding
    def show(self):
        print("Show of Child")

# RULE OF INHERITANCE
# Child can access property of Parent, iff child does not have it :)

def main():
    print("Property of Parent:", vars(Parent))
    print("Property of Child:", vars(Child))

    ref = Child()
    print("ref is:", ref)
    ref.show()

if __name__ == '__main__':
    main()