# def pay(amount, taxes):
#     return amount + (taxes*amount)
#
#
# result = pay(1000, 0.10)
# print(result)

# Decorator
# 1. Outer Function must take function as reference for input
def compute_taxes(func):
    # 2. Create Inner Function
    #    write the logic to decorate
    def inner(amount, taxes):
        if amount <= 0:
            print("This is an Invalid Amount")
            return # terminate the inner function
        elif amount > 0 and amount < 2000:
            taxes = 0.18
        elif amount >= 200:
            taxes = 0.25
        # 3. Execution of the Function which was passed as input
        return func(amount, taxes)

    # 4. return inner function
    return inner


@compute_taxes
def pay(amount, taxes):
    return amount + (taxes*amount)


result = pay(10000, 0.10) # -> compute_taxes(pay)
print("Result is:", result)