from tkinter import *

window = Tk()
window.title("Frames")

# relief -> flat, sunken, groove

first_frame = Frame(borderwidth=4, bg="red", relief="raised")
second_frame = Frame(borderwidth=4, bg="yellow", relief="flat")


lbl1 = Label(master=first_frame, text="This is First Frame")
lbl1.pack()

lbl2 = Label(master=second_frame, text="This is Second Frame")
lbl2.pack()

first_frame.pack(side=LEFT)
second_frame.pack(side=RIGHT)

window.mainloop()

# Project Task
# GUI Exploration as per requirement