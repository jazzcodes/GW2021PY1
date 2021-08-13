"""
    Exceptions
"""

def main():

    print("Welcome to Lucky Number CashBacks App")
    print("~"*30)
    print("APP STARTED")

    cash_backs = [10, 30, 45, 21, 19, 100, 11, 18, 50, 77]
    additional_casback = 0

    try:
        number = int(input("Enter Your Lucky Number (0-9): "))
        print("CashBack Won \u20b9", cash_backs[number])
        additional_casback = 0.10*cash_backs[number]
        print("Additional CashBack Won \u20b9", additional_casback)
    except (IndexError, ValueError) as error:
        print("[INDEX] Something Went Wrong")
        print("Error is:", error)
    except Exception as e:
        print("Something Went Wrong")
        print("Error:", e)
    # except:
    #     print("Something Went Wrong")
    finally:
        # write_log_entry()
        print("Finally Executed")

    print("APP FINISHED")


if __name__ == '__main__':
    main()