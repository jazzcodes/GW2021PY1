from tkinter import *

window = Tk()
window.title("SpinBox")

spin_box = Spinbox(window, from_=1, to=10, width=10)
spin_box.pack()

# spin_box.get()

window.geometry("200x200")

window.mainloop()
