# Topic - Label
from tkinter import *

root = Tk()
root.minsize(100,100)
root.maxsize(300,300) # Max size is defined.
un = Label(root, text="Hello Avinash",font=("Arial",15))
un.pack()
root.mainloop()
