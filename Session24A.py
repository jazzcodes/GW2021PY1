# Reference of tkinter GUI Package: https://docs.python.org/3/library/tk.html

from tkinter import *
from tkinter.ttk import *

def on_click():
    print(combo_box.get())
    print(state.get())

window = Tk()
window.title("Auribises")

lbl_title = Label(window, text="Welcome to Auribises")
# lbl_title.pack()
lbl_title.grid(column=0, row=0)

btn_submit = Button(window, text="Submit", command=on_click)
btn_submit.grid(column=1, row=0)

combo_box = Combobox(window)
combo_box['values'] = ("Select City", "Ludhiana", "Chandigarh", "Delhi", "Bangalore")
combo_box.current(0)
combo_box.grid(column=0, row=2)

state = BooleanVar()
check_button = Checkbutton(window, text="I Agree Terms & Conditions", var=state)
state.set(False)

check_button.grid(column=0, row=3)

window.geometry('200x200')
window.mainloop()