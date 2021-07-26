# Recursion
# -> let the function be repeatedly executed
#    just like a loop

# we need to execute the same function from itself

# for i in range(10, 0, -1):
#     print(i)



def print_number(num):
    if num < 8:
        return
    else:
        print(num)
        num -= 1
        print_number(num)

# this print_number(data) execution has been started from the main
data = 10
print_number(data)
# print_number(9)
# print_number(8)
# print_number(7)


