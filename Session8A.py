"""
    Standardize the Object :)
    Making Objects which will have same attributes :)
"""

class Customer:

    # CONSTRUCTOR
    # 1st input is self
    # self is a reference variable
    # it will hold Hash Code of the CURRENT OBJECT
    def __init__(self):
        print("Constructor Executed")
        print("self is:", self)
        print("type of self is:", type(self))
        print("hashcode of self is:", hex(id(self)))

        self.name = None
        self.phone = None
        self.email = None
        self.gender = None
        self.address = None

def main():
    customer1 = Customer()
    customer2 = Customer()
    customer3 = customer1


    print("customer1:", customer1)
    print("customer1 hashcode is:", hex(id(customer1)));

    print("customer2:", customer2)
    print("customer2 hashcode is:", hex(id(customer2)));

    print("customer3:", customer3)
    print("customer3 hashcode is:", hex(id(customer3)));

    # READ OPERATION
    print("DATA IN OBJECTS NOW: ")
    print(vars(customer1))
    print(vars(customer2))
    print(vars(customer3))

if __name__ == '__main__':
    main()
