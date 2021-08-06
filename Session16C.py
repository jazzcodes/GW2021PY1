def declare_result(func):
    def inner(*args, **kwargs):

        if args[0] >= 40:
            print("Student PASSED")
        else:
            print("Student FAILED")

        func(*args, **kwargs)

    return inner

def grade(func):
    def inner(*args, **kwargs):

        if args[0] >= 40 and args[0] <=50:
            print("GRADE D")
        elif args[0] > 50 and args[0] <=70:
            print("GRADE C")
        elif args[0] > 70 and args[0] <90:
            print("GRADE B")
        elif args[0] >= 90:
            print("GRADE A")
        else:
            print("GRADE E")

        func(*args, **kwargs)

    return inner


@declare_result
@grade
def marks(total_marks):
    print("Marks Obtained:", total_marks)


marks(70)


def transaction(func):
    def inner(*args, **kwargs):

        # Pre Processing
        if kwargs['amount'] >= 100:
            print("We will Process the Transaction")
        else:
            print("Invalid Amount to Transact")
            return  # to terminate the function itself

        func(*args, **kwargs)   # Function to Execute

        # Post Processing
        print("Send an Email for Transaction")
        print("Send SMS for Transaction")

    return inner


@transaction
def pay(amount):
    print("Transacting the Amount...", amount)


pay(amount=1000)