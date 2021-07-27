"""

    Standardize the Object :)
    WITH IMPROVEMENT
    Making Objects which will have same attributes :)
"""

class Customer:

    # CONSTRUCTOR
    # 1st input is self
    # self is a reference variable
    # it will hold Hash Code of the CURRENT OBJECT
    def __init__(self, name=None, phone=None, email=None, gender=None, address=None):
        print("Constructor Executed")
        print("self is:", self)
        print("type of self is:", type(self))
        print("hashcode of self is:", hex(id(self)))

        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.address = address

def main():
    customer1 = Customer("John", "+91 99999 11111", "john@example", "male", "redwood shoes")
    customer2 = Customer("Fionna")
    customer3 = customer1


    print("customer1:", customer1)
    print("customer1 hashcode is:", hex(id(customer1)));

    print("customer2:", customer2)
    print("customer2 hashcode is:", hex(id(customer2)));

    print("customer3:", customer3)
    print("customer3 hashcode is:", hex(id(customer3)));

    customer1.is_prime = True
    customer1.videos = True
    customer1.music = True
    customer1.free_deliveries = 5

    # READ OPERATION
    print("DATA IN OBJECTS NOW: ")
    print(vars(customer1))
    print(vars(customer2))
    print(vars(customer3))

if __name__ == '__main__':
    main()

# Assignment: Code an Object as per your Use Case