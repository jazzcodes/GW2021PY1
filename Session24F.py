from tkinter import *
from tkinter import filedialog

def on_click():
    file_path = filedialog.askopenfilename()
    print(file_path)

    with open(file_path) as file:
        print(file.read())




window = Tk()
window.title("File Picker")

menu = Menu()

item = Menu(menu)
item.add_command(label="New")
item.add_command(label="Save")
item.add_separator()
item.add_command(label="Exit")

menu.add_cascade(label="File", menu=item)

btn_select_file = Button(window, text="SELECT FILE", command=on_click)
btn_select_file.pack()

window.config(menu=menu)
window.mainloop()