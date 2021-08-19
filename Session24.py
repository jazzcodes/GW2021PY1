from tkinter import *
from Session23 import DB


class CustomerManagementApp:

    def __init__(self):
        self.db = DB()

    def on_click(self):
        print("Button Clicked")

        customer = {
            "name": self.entry_name.get(),
            "phone": self.entry_phone.get(),
            "email": self.entry_email.get(),
        }

        sql = "insert into Customer values(null, '{name}', '{phone}', '{email}', 0.0, '', '')" \
            .format_map(customer)

        self.db.execute_sql_write_operation(sql)
        print(self.entry_name.get(), "Added")

    def run_app(self):

        home_window = Tk()
        lbl_title = Label(home_window, text="CUSTOMER MANAGEMENT SYSTEM")
        lbl_title.pack()

        btn_add = Button(home_window, text="Add Customer", command=self.add_customer_gui)
        btn_add.pack()

        btn_update = Button(home_window, text="Update Customer")
        btn_update.pack()

        btn_delete = Button(home_window, text="Delete Customer")
        btn_delete.pack()

        btn_fetch_all = Button(home_window, text="Fetch Customers")
        btn_fetch_all.pack()

        btn_fetch = Button(home_window, text="Fetch Customer By Phone")
        btn_fetch.pack()

        home_window.mainloop()


    def add_customer_gui(self):
        add_customer_window = Tk()

        lbl_title = Label(add_customer_window, text="ADD CUSTOMER")
        lbl_title.pack()

        lbl_phone = Label(add_customer_window, text="Enter Customer Name:")
        lbl_phone.pack()

        self.entry_name = Entry(add_customer_window)
        self.entry_name.pack()

        lbl_phone = Label(add_customer_window, text="Enter Customer Phone:")
        lbl_phone.pack()

        self.entry_phone = Entry(add_customer_window)
        self.entry_phone.pack()

        lbl_email = Label(add_customer_window, text="Enter Customer Email:")
        lbl_email.pack()

        self.entry_email = Entry(add_customer_window)
        self.entry_email.pack()

        btn_submit = Button(add_customer_window, text="Add Customer", command=self.on_click)
        btn_submit.pack()

        add_customer_window.mainloop()

def main():
    app = CustomerManagementApp()
    app.run_app()

if __name__ == '__main__':
    main()