class Student:

    def __init__(self, roll, name, age):
        self._roll = roll # Protected
        self.name = name
        # Name Mangling -> __age will be renamed to _Student__age
        self.__age = age  # Private

    def show(self):
        print("Name:", self.name)
        print("Details:", self._roll, self.__age)


def main():
    student = Student(roll=101, name="John Watson", age=10)
    # print(vars(student))
    # print(student._roll) # Warning
    # print(student.name)
    # print(student.__age) # error
    # print(student._Student__age) # -> Name Mangling

    print(vars(student))

if __name__ == '__main__':
    main()

