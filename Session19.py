"""
    Argument Parsing
        1. sys
        2. getopt (explore as HW)
        3. argparse
    Monkey Patching
    Duck Typing
    Exception Handling
"""
# system module :)
import sys


def write_in_file(data="Be Exceptional"):
    with open("data.txt", "a") as file:
        file.write(data+"\n")


def read_from_file():
    with open("data.txt", "r") as file:
        for line in file.readlines():
            print(line)


def main():
    print("Number of Arguments", len(sys.argv))
    print("Arguments:", sys.argv, type(sys.argv))

    if sys.argv[1] == "write":
        write_in_file()
    elif sys.argv[1] == "read":
        read_from_file()


if __name__ == '__main__':
    main()