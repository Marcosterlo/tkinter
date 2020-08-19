from tkinter import *

root = Tk()

#per creare un input box si usa il widget Entry

e = Entry(root, width=50, fg="blue", bg="#00FFFF")
e.insert(0, "Enter your name: ") #insert inserisce del testo coem se fosse inserito come input dall'utente

def onClick():
    hello = "Hello " + e.get()
    lab = Label(root, text=hello) #get prende come argomento quanto sritto in un'entry
    lab.pack()

butt = Button(root, padx=50, pady=50, fg="blue", bg="#00FFFF", text="Insert your name", command=onClick)
e.pack()
butt.pack()

root.mainloop()