"""
    GUI | Graphical User Interfaces
    >> figma (Design Your GUI First)

    tkinter
    PyQT -> Explore
"""

from tkinter import *
from Session23 import DB

entry_name = None
entry_phone = None
entry_email = None

def on_click():
    print("Button Clicked")

    customer = {
        "name": entry_name.get(),
        "phone": entry_phone.get(),
        "email": entry_email.get(),
    }

    my_db = DB()
    sql = "insert into Customer values(null, '{name}', '{phone}', '{email}', 0.0, '', '')"\
        .format_map(customer)
    my_db.execute_sql_write_operation(sql)

    print(customer)

def main():

    global entry_name
    global entry_phone
    global entry_email

    window = Tk()

    lbl_title = Label(window, text="CUSTOMER MANAGEMENT SYSTEM")
    lbl_title.pack()

    lbl_phone = Label(window, text="Enter Customer Name:")
    lbl_phone.pack()

    entry_name = Entry(window)
    entry_name.pack()

    lbl_phone = Label(window, text="Enter Customer Phone:")
    lbl_phone.pack()

    entry_phone = Entry(window)
    entry_phone.pack()

    lbl_email = Label(window, text="Enter Customer Email:")
    lbl_email.pack()

    entry_email = Entry(window)
    entry_email.pack()

    btn_submit = Button(window, text="Add Customer", command=on_click)
    btn_submit.pack()

    window.mainloop()

if __name__ == '__main__':
    main()