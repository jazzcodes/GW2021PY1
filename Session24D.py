from tkinter import *
from tkinter import messagebox


def on_click():
    # messagebox.showinfo("This is title", "This is Information Text Message in the Box")
    # messagebox.showerror("This is title", "This is Error Text Message in the Box")
    # messagebox.showwarning("This is title", "This is Warning Text Message in the Box")

    # response = messagebox.askquestion("Delete", "Would You Like to Delete the User?")
    response = messagebox.askyesnocancel("Delete", "Would You Like to Delete the User?")
    print("response is:", response)

    if response:
        print("DELETE from DB")

window = Tk()
window.title("Message Boxes")

btn_submit = Button(window, text="SHOW", comman=on_click)
btn_submit.pack()

window.mainloop()
