from tkinter import *

root = Tk()

#Creazione dei label
myLabel1 = Label(root, text="Test")
myLabel2 = Label(root, text="Questo è un secondo messaggio")

#Grid sta per tabella, intabellazione
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
#Le posizioni sono relative, se mettessi ad esmepio una colonna 5 sarebbe comunque sotto di una posizione
#le colonne in mezzo sarebbero vuote e quindi non visualizzate

root.mainloop()
