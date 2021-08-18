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

    def __init__(self, update_mode=False):

        if update_mode:
            return

        self.input_details()


    def __str__(self):
        return "{id} | {name} | {phone} | {email} | {temperature} | {intime} | {outtime}".format_map(vars(self))


    def input_details(self, old_customer=None):

        if old_customer is not None:

            self.id = old_customer.id

            self.name = input("Enter Name:")
            if len(self.name) == 0: self.name = old_customer.name

            self.phone = input("Enter Phone:")
            if len(self.phone) == 0: self.phone = old_customer.phone

            self.email = input("Enter Email:")
            if len(self.email) == 0: self.email = old_customer.email

            temp = input("Enter Temperature:")
            if len(temp) == 0: self.temperature = old_customer.temperature
            else: self.temperature = float(temp)

            self.intime = input("Enter In Time:")
            if len(self.intime) == 0: self.intime = old_customer.intime

            self.outtime = input("Enter Out Time:")
            if len(self.outtime) == 0: self.outtime =  old_customer.outtime
        else:
            self.name = input("Enter Name:")
            self.phone = input("Enter Phone:")
            self.email = input("Enter Email:")
            temp = input("Enter Temperature:")
            if len(temp) == 0: self.temperature = 0.0
            else:self.temperature = float(temp)
            self.intime = input("Enter In Time:")
            self.outtime = input("Enter Out Time:")

class DB:

    def __init__(self):
        self.connection = db.connect(user='root', password='auribises',
                                  host='127.0.0.1',
                                  database='gw2021py1')
        self.cursor = self.connection.cursor()
        print("[DB] CONNECTION ESTABLISHED")

    def show_row(self, row):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("{} | {} | {}".format(row[0], row[1], row[2]))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # write operation
    def execute_sql_write_operation(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        print("[DB] SQL EXECUTED")

    # read operation
    def execute_sql_read_operation(self, sql):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall() # return list of tuples
        # print(rows)
        # print(type(rows))

        if len(rows) == 0:
            print("Customer Not Found :(")
            choice = input("Would You Like to Add the Customer: ")
            if choice == "yes":
               pass #assignment
            else:
                for row in rows:
                    self.show_row(row)

        # For Update we will return customer as object
        if len(rows) == 1:
            customer = Customer(update_mode=True)
            customer.id = rows[0][0]
            customer.name = rows[0][1]
            customer.phone = rows[0][2]
            customer.email = rows[0][3]
            customer.temperature = float(rows[0][4])
            customer.intime = rows[0][5]
            customer.outtime = rows[0][6]

            return customer


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
        print("5. Fetch Customer By Phone")
        print("6. To Quit ")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            customer = Customer()
            sql = "insert into Customer values(null, '{name}', '{phone}', '{email}', {temperature}, '{intime}', '{outtime}')".format_map(vars(customer))

            my_db.execute_sql_write_operation(sql)

        elif choice == 2:
            phone = input("Enter Customer Phone Number to Update: ")
            sql = "select * from Customer where phone = '{}'".format(phone)
            customer = my_db.execute_sql_read_operation(sql)
            print("customer before:", customer)

            customer_to_update = Customer(update_mode=True)
            customer_to_update.input_details(old_customer=customer)

            print("customer to be updated:", customer_to_update)

            sql = "update Customer set name='{name}', phone='{phone}', email='{}', temperature={temperature}, intime='{intime}', outtime='{outtime}' where id = {id}".format_map(vars(customer_to_update))
            my_db.execute_sql_write_operation(sql)
            print(customer.name, " Updated")

        elif choice == 3:
            phone = input("Enter Customer Phone Number to Delete: ")
            sql = "delete from Customer where phone = '{}'".format(phone)
            my_db.execute_sql_write_operation(sql)

        elif choice == 4:
            sql = "select * from Customer"
            my_db.execute_sql_read_operation(sql)

        elif choice == 5:
            phone = input("Enter Customer Phone Number: ")
            # sql = "select id, name, phone from Customer where phone = '{}'".format(phone)
            sql = "select * from Customer where phone = '{}'".format(phone)
            my_db.execute_sql_read_operation(sql)

        elif choice == 6:
            break

    del my_db

if __name__ == '__main__':
    main()