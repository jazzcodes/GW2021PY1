from tkinter import *
from tkinter.ttk import *

def on_click():
    print(var.get())

window = Tk()
window.title("Radio Buttons")

lbl_gender = Label(window, text="Select Gender")

var = IntVar()

rb_female = Radiobutton(window, text="Female", value=1, variable=var)
rb_male = Radiobutton(window, text="Male", value=2, variable=var)
rb_not_to_say = Radiobutton(window, text="Not To Say", value=3, variable=var)

btn_submit = Button(window, text="Submit", command=on_click)

lbl_gender.grid(column=0, row=0)
rb_female.grid(column=0, row=1)
rb_male.grid(column=1, row=1)
rb_not_to_say.grid(column=2, row=1)
btn_submit.grid(column=0, row=2)

window.geometry("300x300")
window.mainloop()