# Topic - Button
from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(0,0) 
b1=Button(root,text="Click Me!!",font=("Arial",12),bg="Green")
b1.pack()
root.mainloop()
