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

months = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December"
}

# Empty List for Transactions
transactions = []
fix_amount = 0

def transact_amount(amount):
    if len(transactions) == 0:
        transaction_record = {
            "month": 0,
            "amount": amount,
            "charges": amount * 0.10,
            "total": amount + amount * 0.10,
            "dues": amount + amount * 0.10,
        }
        transactions.append(transaction_record)
    else:
        transaction_record = {
            "month": transactions[len(transactions)-1]["month"]+1,
            "amount": amount,
            "charges": amount * 0.10,
            "total": amount + amount * 0.10,
            "dues": (amount + amount * 0.10) + transactions[len(transactions)-1]["dues"],
        }
        transactions.append(transaction_record)

    print("Amount Transacted \u20b9", amount)


def show_transaction_history():
    for transaction in transactions:
        print("-"*30)
        print("Month: {}".format(months[transaction["month"]]))
        print("Transacted Amount: \u20b9{amount}"
              "\nBilling Amount: \u20b9{total}\nTotal Dues: \u20b9{dues}".format_map(transaction))
        print("-" * 30)
        print()


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
    print("[4] Transaction History")
    print("[5] Quit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def make_choice():
    while True:
        choice = int(input("Enter Your Choice[1-5]: "))
        if choice == 1:
            amount = int(input("Enter a Fix Amount to be paid every month: "))
            set_fix_amount(amount)
        elif choice == 2:
            amount = int(input("Enter Transaction Amount: "))
            transact_amount(amount)
        elif choice == 3:
            pass
        elif choice == 4:
            show_transaction_history()
        else:
            break


def main():
    show_welcome_message()
    make_choice()


if __name__ == '__main__':
    main()

