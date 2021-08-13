
# User Defined Exception
class BankingError(Exception):
    def __init__(self, message):
        super().__init__(message)

class BankAccount:

    bank_account_branch_number = 302561240
    bank_account_number = 1
    min_balance = 2000
    min_attempts = 3

    def __init__(self, name=None):
        self.name = name
        self.account_number = BankAccount.bank_account_branch_number + BankAccount.bank_account_number
        BankAccount.bank_account_number += 1
        self.balance = 10000
        self.attempts = 0
        print("Bank Account Opened")

    def withdraw(self, amount):
        self.balance -= amount

        if self.balance < BankAccount.min_balance:
            self.balance += amount
            print("[WITHDRAW] Failed for {} for amount \u20b9{}".format(self.name, amount))
            print("BALANCE IS LOW :(")
            self.attempts += 1

            if self.attempts == BankAccount.min_attempts:
                # raise ValueError("Illegal Attempts")
                raise BankingError(message="Illegal Attempts")
            return

        print("[WITHDRAW] Success for {} for amount \u20b9{}".format(self.name, amount))
        print("Balance is: \u20b9{}".format(self.balance))

    def deposit(self, amount):
        self.balance += amount
        print("[DEPOSIT] Success for {} for amount \u20b9{}".format(self.name, amount))
        print("Balance is: \u20b9{}".format(self.balance))

    def transaction(self, account_from, account_to):
        pass

def main():
    print("BANKING APP STARTED")

    account1 = BankAccount(name="John")
    account2 = BankAccount(name="Fionna")

    print("Account1 Data:", vars(account1))
    print("Account1 Data:", vars(account2))

    account1.deposit(amount=5000)
    account1.deposit(amount=7000)

    try:
        for i in range(500000):
            account2.withdraw(amount=3000)
    except Exception as e:
        print("Something Went Wrong", e)


    print("Account1 Data:", vars(account1))
    print("Account1 Data:", vars(account2))

    print("BANKING APP FINISHED")

if __name__ == '__main__':
    main()