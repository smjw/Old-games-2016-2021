from tkinter import*
root=Tk()
root.title("beans")
root.geometry("400x400")

def show():
    myLabel=Label(root, text= clicked.get()).pack()

options=[
    "level1",
    "level2"

]

clicked= StringVar()
clicked.set(options[0])

drop= OptionMenu(root, clicked, *options)
drop.pack()

myButton=Button(root, text="show selection", command=show).pack()

root.mainloop()
