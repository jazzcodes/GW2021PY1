"""
    MODEL
        Single Value Container
            int, float, string etc...
        Multi Value Container
            tuple, list, set, arrays, dict

    VIEW
        always works with strings
        Textual Interface
"""

print("Hello, What is Your Name?")
name = input("We will like to know your name. Please Enter the same: ")
print("Thank You", name, type(name))

age = int(input("Enter Your Age: "))
print("Age is:", age, type(age))
