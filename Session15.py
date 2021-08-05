"""
    Functions
"""


def add_numbers(num1, num2):
    result = num1 + num2
    print("result is:", result)


def calculate_bill_amount(amount, taxes=0.10, delivery_fee=0, packing_charge=0):
    total = amount + (0.18*taxes) + (delivery_fee+5) + packing_charge
    print("Total Amount is:", total)


# Reference Copy -> Will be Used to perform Monkey Patching
fun1 = add_numbers
fun2 = calculate_bill_amount

def main():
    add_numbers(10, 20)
    add_numbers(num1=10, num2=20)
    calculate_bill_amount(amount=2000)
    calculate_bill_amount(amount=2000, delivery_fee=20)
    calculate_bill_amount(amount=2000, delivery_fee=20, packing_charge=50)
    calculate_bill_amount(delivery_fee=20, packing_charge=50, amount=2000)

    print("add_numbers is:", add_numbers)
    print("calculate_bill_amount is:", calculate_bill_amount)

    fun1(num1=11, num2=33)
    fun2(amount=1200)

if __name__ == '__main__':
    main()