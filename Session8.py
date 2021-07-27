"""
    OOPS in Python
    Object Oriented is basically a software design methodology

    STEP #1 Collect or Create Requirements for Development of Software

    REQUIREMENT #1:
    Therapy Center
    We have a Customer. Customer is allocated 1 Package
    Package has sittings -> Spine Package [12 sitting in a month]

    Staff -> Therapist

    Mark time stamps of entry exit of Customer
    Therapy Timings to be clocked

    Stats -> For every customer we need to have history of visits and time spent

    REQUIREMENT #2
    COVID Concern
    Malls -> We must have a limit of how many people can be in the mall in number
    eg: not more than 200

    Customer will walk in and we will mark the entry and when customer walks out, we will mark the exit

     REQUIREMENT #3
     Home Intelligent Inventory
     Note the inventory of products so as to perform ML and AI on data in future

     REQUIREMENT for our Learning Purpose:
     Zomato -> Food Delivery App
     Customer shall see list of restaurants
     Every Restaurant will have A menu of dishes which can be categorized
     Custoner can put the dishes in cart and can use payment options to pay
     Restaurant can accept or reject the order
     Valet is required to pickup and drop the order
     Customer will have Address where Order shall be delivered

    Step #2
    Find Objects from Requirements
    Object is a storage container with lot of data associated
    eg: Customer is an Object
        id, name, phone, email, gender, address etc..
        Gather as much data as you can...

    # CAN BE PARENT -> Details: id, name, phone, email

    Customer: id, name, phone, email, gender, addresses
    Restaurant: id, name, phone, email, addresses, operating_hours, ratings, category
    Menu: title, num_of_dishes, dishes
    Dish: title, price, description, ratings
    Order: id, date, time, customer, restaurant, dishes, total
    Valet: id, name, phone, email, work_experience, ratings

    Step #3
    Create Classes in Code which represents or create the Type of Object
    class represent the type of object

    Principle of OOPS:
    1. Think of Objects
    2. Write Attributes of Objects
    3. Create Relations in Objects
        HAS-A : 1 to 1, 1 to many, many to 1, many to many
        IS-A  : inheritance
    4. Create Classes i.e. Type of Object in Your Program
    5. From the Classes Create Real Objects in Memory :)

"""
# PEP Style Guide for how to write Code
# Reference: https://pep8.org/

class Customer:
    pass


class Restaurant:
    pass


class Menu:
    pass


class Dish:
    pass


# Main Function to execute the App
def main():
    # Object Construction Statement
    customer1 = Customer()
    customer2 = Customer()
    # REFERENCE COPY OPERATION
    customer3 = customer1

    print("customer1:", customer1)
    print("customer1 hashcode is:", hex(id(customer1)));

    print("customer2:", customer2)
    print("customer2 hashcode is:", hex(id(customer2)));

    print("customer3:", customer3)
    print("customer3 hashcode is:", hex(id(customer3)));

    # print(customer1.__dict__)
    # print(customer2.__dict__)
    # print(customer3.__dict__)

    print(vars(customer1))
    print(vars(customer2))
    print(vars(customer3))

    # 1. Write Data
    customer1.name = "John"
    customer1.email = "john@example.com"
    customer3.phone = "+91 99999 11111"

    customer2.full_name = "Fionna Flynn"
    customer2.email = "fionna@example.com"
    customer2.phone_number = "+91 99999 33333"
    customer2.address = "ABC, XYZ Town"

    # 2. Update Data
    customer3.name = "John Watson"

    # 3. Delete Operation
    del customer1.phone

    # 4. READ OPERATION
    print("DATA IN OBJECTS NOW: ")
    print(vars(customer1))
    print(vars(customer2))
    print(vars(customer3))

if __name__ == '__main__':
    main()