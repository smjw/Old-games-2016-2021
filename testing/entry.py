from tkinter import *

root = Tk()

e = Entry(root,width=50, bg="pink", borderwidth=10)
e.pack()
e.insert(0,"Enter your name")

def myClick():
        hello="Hello "+e.get()
        myLabel = Label(root, text=hello)
        myLabel.pack()

myButton = Button(root, text="Enter your name !", padx=50, pady=30, command=myClick, fg="blue", bg="yellow")
myButton.pack()

root.mainloop()
