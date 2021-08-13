"""
    Crash The Program Explicitly
"""

def main():

    print("App Started")

    # ref = IndexError()
    # raise ref

    raise IndexError("I am Crashing the App as Developer")

    print("App Finished")


if __name__ == '__main__':
    main()