from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("Scrolled Text")


scroll_text = scrolledtext.ScrolledText(window, width=240, height=100)
scroll_text.grid(column=0, row=0)

# scroll_text.get()

window.geometry("300x300")
window.mainloop()