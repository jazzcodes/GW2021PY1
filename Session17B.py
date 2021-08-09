# Time Complexity => O(n)
for i in range(1, 10):
    print(i)

# Time Complexity => O(n*n)
for i in range(1, 6):
    for j in range(1, 4):
        print(j)

# Time Complexity => O(n*n*n)
for i in range(1, 6):
    for j in range(1, 4):
        for k in range(1, 4):
            print(k)

# Total Time Complexity -> O(n) + O(n*n) + O(n*n*n) => O(n*n*n)
