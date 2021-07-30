"""
    Expense
    John -> Credit Card
    Month 1   10000
              10% interest
              -> bill -> 11000

    Month 2   8000

    Month 3   9000

    Clear Bill
    John can pay no more than 3000(example)

    prediction -> in which month his bill will be all clear

    # CASE 1
    John expense in 1st Month
    Month 1   10000
              10%
              11000
    Month 2   3000
    Month 3   3000
    Month 4   3000
    Month 5   2000

    # CASE 2
    John expense in 1st Month
    Month 1   10000
              10%
              11000
    Month 2   5000
              10%
              5500
              ----
              16500

              3000
    Month 3   3000
    Month 4   3000
    Month 5   2000

    1. Enter the fixed minimum payment amount (installment)
    2. to make an expense -> month will be taken care by algo
    3. to make a payment (fixed payment)
        give the forecast of the month where the bill will become 0


"""
# Empty List for Transactions
transactions = []
fix_amount = 0

def set_fix_amount(amount):
    fix_amount = amount
    print("We have Set a Fix Amount of \u20b9", fix_amount)


def show_welcome_message():
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to CredManager")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please Read the Instruction Menu and Enter Your Choice")
    print("[1] Enter Fixed Minimum Amount Payable Every Month")
    print("[2] Transact Any Amount")
    print("[3] Make a Payment. (Fixed Amount will be deducted automatically)")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def make_choice():
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        amount = int(input("Enter a Fix Amount to be paid every month: "))
        set_fix_amount(amount)


def main():
    show_welcome_message()
    make_choice()


if __name__ == '__main__':
    main()