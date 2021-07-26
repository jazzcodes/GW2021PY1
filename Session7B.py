"""
def find_max(data):

    max = data[0]
    for number in data:
        if number > max:
            max = number

    return max  # last statement
"""
# write some code
# and make recursive algo
def find_max(data, length):
    if length == 1:
        return data[0]
    else:
        result = find_max(data, length-1)
        if result > data[length-1]:
            return result
        else:
            return data[length-1]

def main():
    numbers = [10, 20, 30]
    print(numbers)
    max = find_max(numbers, len(numbers))
    print("MAX IS:", max)


if __name__ == '__main__':
    main()