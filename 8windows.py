# Topic - Login Page
from tkinter import *

root = Tk()
root.geometry("800x800")
root.resizable(0,0) 
un1=Label(root,text="Enter Name:",font=("Arial",20))
#grid is used to create page with grid system so that elements can be placed into row and column.
###########################
# Name    : ------------- #
# Password: ------------- #
###########################
un1.grid(row=0,column=0,pady='25') #pady will leave space from top.
e1=Entry(root,font=("Arial",20))
e1.grid(row=0,column=1)
un2=Label(root,text="Enter Password:",font=("Arial",20))
un2.grid(row=1,column=0)
e2=Entry(root,font=("Arial",20))
e2.grid(row=1,column=1)
b1=Button(root,text="Click Me!!!!!",font=("Arial",20))
b1.grid(row=2,column=1)
root.mainloop()
