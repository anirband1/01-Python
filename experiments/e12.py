from tkinter import *

root = Tk()
root.title("calculator")

#box = Entry(root,width = 100)
#box.grid(row=0 ,column=0 ,columnspan=3)

def myclick():
    print("")
    


mybutton = Button(root, text="  button  ", command=myclick )
mybutton.pack()

root.mainloop()

print("\n \n")

