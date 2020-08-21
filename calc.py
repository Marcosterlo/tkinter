from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=3)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(i):
   current = e.get()
   e.delete(0, END)
   e.insert(0, str(current) + str(i))
   return

def button_add():
   primo = e.get()
   global first
   global operation
   operation = "add"
   first = int(primo)
   e.delete(0, END)
   return

def button_sub():
   primo = e.get()
   global first
   global operation
   operation = "sub"
   first = int(primo)
   e.delete(0, END)
   return

def button_mul():
   primo = e.get()
   global first
   global operation
   operation = "mul"
   first = int(primo)
   e.delete(0, END)
   return

def button_div():
   primo = e.get()
   global first
   global operation
   operation = "div"
   first = int(primo)
   e.delete(0, END)
   return

def button_clear():
   e.delete(0, END)
   return

def button_equal():
   secondo = e.get()
   e.delete(0, END)
   if operation == "add":
      e.insert(0, first + int(secondo))
   elif operation == "sub":
      e.insert(0, first - int(secondo))
   elif operation == "mul":
      e.insert(0, first * int(secondo))
   elif operation == "div":
      e.insert(0, first / int(secondo))
   return

butt_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
butt_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
butt_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
butt_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
butt_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
butt_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
butt_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
butt_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
butt_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
butt_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
butt_add = Button(root, text="+", padx=39, pady=20, command=button_add)
butt_sub = Button(root, text="-", padx=41, pady=20, command=button_sub)
butt_mul = Button(root, text="x", padx=40, pady=20, command=button_mul)
butt_div = Button(root, text=":", padx=41, pady=20, command=button_div)
butt_equal = Button(root, text="=", padx=90, pady=20, command=button_equal)
butt_clear = Button(root, text="Clear", padx=130, pady=20, command=button_clear)

butt_1.grid(row=3, column=0)
butt_2.grid(row=3, column=1)
butt_3.grid(row=3, column=2)

butt_4.grid(row=2, column=0)
butt_5.grid(row=2, column=1)
butt_6.grid(row=2, column=2)

butt_7.grid(row=1, column=0)
butt_8.grid(row=1, column=1)
butt_9.grid(row=1, column=2)

butt_0.grid(row=4, column=0)
butt_add.grid(row=5, column=0)
butt_sub.grid(row=5, column=1)
butt_mul.grid(row=6, column=0)
butt_div.grid(row=6, column=1)
butt_equal.grid(row=4, column=1, columnspan=2)
butt_clear.grid(row=7, column=0, columnspan=3)

root.mainloop()