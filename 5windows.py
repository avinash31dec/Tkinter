# Topic - Label
from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(0,0) 
#Adding Background and Foreground Color.
#Width will fix that number of character width.
#Height will fix that number of line.
un = Label(root, text="Hello Avinash",font=("Arial",15),bg="black",fg="green", width='15',height='3') 
un.pack()
root.mainloop()
