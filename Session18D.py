# Run Time Polymorphism

"""
# No Compile Time Polymorphism
class Math:

    def sum(self, num1, num2):
        result = num1 + num2
        print("result is:", result)

    # this redefining the same function again in same class
    # is not overloading
    # the previous function is no more in the meory
    # replacing the sum as reference variable with the hashcode of new function
    def sum(self, num1, num2, num3):
        result = num1 + num2 + num3
        print("result is:", result)
"""

"""
class User:
    pass

# RTP or Dynamic Typing
ref = 10
ref = 2.2
ref = [10, 20, 30]
ref = User()
"""

class Payment:

    def pay(self, amount):
        print("Paying an Amount: \u20b9", amount)


class NetBanking(Payment):

    def input_username_password(self):
        print("Entering User name and Password for User")

    # ReDefining
    def pay(self, amount):
        self.input_username_password()
        print("Paying an Amount: \u20b9", amount)


class UPI(Payment):

    def input_upi_id(self):
        print("Entering UPI ID for User")

    # ReDefining
    def pay(self, amount):
        self.input_upi_id()
        print("Paying an Amount: \u20b9", amount)

# Factory Design Pattern
class PaymentMethod:

    @classmethod
    def get_method(cls, type):

        ref = None

        if "netbanking" in type:
            ref = NetBanking()
        elif "upi" in type:
            ref = UPI()
        else:
            print("Invalid Option")

        return ref

def main():

    # Run Time Polymorphism
    """
    ref = Payment()
    ref.pay(amount=1000)

    print()

    ref = NetBanking()
    ref.pay(amount=1000)

    print()

    ref = UPI()
    ref.pay(amount=1000)
    """

    choice = input("How Would you Like to Pay? ")
    payment = PaymentMethod.get_method(type=choice)
    if payment is not None:
        payment.pay(amount=1000)


if __name__ == '__main__':
    main()