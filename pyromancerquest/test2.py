from tkinter import *

root=Tk()
root.title("Pyromancer")

e = Entry(root,width=50, borderwidth=10)
e.pack()
e.insert(0,"")

def click():
    welcome="welcome " +e.get()
    myLabel= Label(root, text=welcome)
    myLabel.pack()
    teamname=e.get()

myButton=Button(root, text="enter your team name: ", padx=50, pady=30, command=click)
myButton.pack()



