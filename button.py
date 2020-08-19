from tkinter import *

root = Tk()

def onClick():
    myLabel = Label(root, text="I clicked a button!")
    myLabel.pack()

myButton = Button(root, text="Click me", command=onClick, fg="blue", bg="#00FFFF", padx=50, pady=50)
myButton.pack()

root.mainloop()