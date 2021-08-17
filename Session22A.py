import mysql.connector as db

"""
    create table Customer(
        id int primary key auto_increment,
        name varchar(256),
        phone varchar(256),
        email varchar(256),
        temperature float,
        intime varchar(256),
        outtime varchar(256)
    );
"""
class Customer:

    def __init__(self):
        self.name = input("Enter Name:")
        self.phone = input("Enter Phone:")
        self.email = input("Enter Email:")
        self.temperature = float(input("Enter Temperature:"))
        self.intime = input("Enter In Time:")
        self.outtime = input("Enter Out Time:")


class DB:

    def __init__(self):
        self.connection = db.connect(user='root', password='auribises',
                                  host='127.0.0.1',
                                  database='gw2021py1')
        self.cursor = self.connection.cursor()
        print("[DB] CONNECTION ESTABLISHED")

    def execute_sql_query(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        print("[DB] SQL EXECUTED")

    # whenever we will del the object
    def __del__(self):
        self.connection.close()
        print("[DB] CONNECTION RELEASED")

def main():

    my_db = DB()

    while True:
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. Fetch Customers")
        print("5. To Quit ")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            customer = Customer()
            sql = "insert into Customer values(null, '{name}', '{phone}', '{email}', {temperature}, '{intime}', '{outtime}')".format_map(vars(customer))

            my_db.execute_sql_query(sql)

        elif choice == 5:
            break

    del my_db

if __name__ == '__main__':
    main()