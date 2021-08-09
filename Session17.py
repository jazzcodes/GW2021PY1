"""
    COVID-19
    Project: School/College Class Scheduler
    Use your algorithms to allocate days of the week in a month to particular student
    file for every student has to be generated
    john_watson_1_september.csv
    1,coming
    2,not coming
    3,not coming
    .
    ...

    1. Add all Students first
    2. Run Algorithm
    3. Generate file, standard wise and month wise, for all students
"""


class Student:
    def __init__(self, roll, name, age, gender, phone, standard):
        self.roll = roll
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.standard = standard

    # User Defined Function
    def to_csv(self):
        return "{roll},{name},{age},{gender},{phone},{standard}\n".format_map(vars(self))

    def save(self):
        data = self.to_csv()
        file = open("students.csv", "a")
        choice = input("Would You Like to Save {}: (yes/no) ".format(self.name))
        if choice == "yes":
            file.write(data)
            print("Data Saved :)")
        else:
            print(data)


class Hospital:
    def __init__(self, name, address, phone, num_of_ambulance, is_ambulance_available, covid_beds, oxygen_cylinders, appointments_for_covid):
        pass


class Mall:
    def __init__(self, name, address, phone, capacity, present_capacity, threshold_capacity_as_covid):
        pass


class Product:
    def __init__(self, name, stock):
        pass


def main():
    student1 = Student(
        roll=1,
        name="John Watson",
        age=10,
        gender="male",
        phone="+91 99999 11111",
        standard=5
    )

    student2 = Student(
        roll=2,
        name="Fionna Flynn",
        age=10,
        gender="female",
        phone="+91 99999 22222",
        standard=5
    )

    student3 = Student(
        roll=3,
        name="Dave Dylon",
        age=10,
        gender="male",
        phone="+91 99999 33333",
        standard=5
    )

    # Persistence
    # Save data of Object
    # 1. File
    # 2. Local DB
    # 3. Cloud DB

    # SERIALIZATION -> When we save the state of an object in file

    # file = open("students.csv", "w")
    # file = open("students.csv", "a")
    # data = student2.to_csv()
    # file.write(data)
    # print("Data Saved in File :)")

    # student1.save()
    student2.save()
    student3.save()


if __name__ == '__main__':
    main()



