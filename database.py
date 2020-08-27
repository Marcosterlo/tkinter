from tkinter import *
from PIL import Image, ImageTk
import sqlite3

root = Tk()
root.title("Databases")
root.geometry("800x500")

# Databases

# Create a database or connect to one
conn = sqlite3.connect("login_list.db")

# Create a cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE login_list (
    first_name text,
    last_name text,
    address text,
    city text,
    state text, 
    zipcode integer
    )""")
'''

# Commit changes
conn.commit()

# Close connection
conn.close()

def submit():
    # Connect to database
    conn = sqlite3.connect('login_list.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO login_list VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': addr.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # Commit changes
    conn.commit()

    # close connection
    conn.close()

    # Clear the entries
    f_name.delete(0, END)
    l_name.delete(0, END)
    addr.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    return

def query():
    # Connect to database
    conn = sqlite3.connect('login_list.db')

    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM login_list")
    records = c.fetchall()
    print_record = ''
    for record in records:
        for instance in record:
            print_record += str(instance) + " "
        print_record += "\n"

    Label(root, text=print_record).grid(row=9, column=0, columnspan=2)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()
    return

def delete():
    conn = sqlite3.connect("login_list.db")
    c = conn.cursor()
    # Delete a record
    c.execute("DELETE from login_list WHERE oid=" + delete_box.get())
    delete_box.delete(0, END)
    conn.commit()
    conn.close()
    return

# Gui part
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
addr = Entry(root, width=30)
addr.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=2, padx=20)

# Create Text Box labels
f_name_lab = Label(root, text="First name").grid(row=0, column=0, padx=20)
l_name_lab = Label(root, text="Last name").grid(row=1, column=0, padx=20)
addr_lab = Label(root, text="Address").grid(row=2, column=0, padx=20)
city_lab = Label(root, text="City").grid(row=3, column=0, padx=20)
state_lab = Label(root, text="State").grid(row=4, column=0, padx=20)
zipcode_lab = Label(root, text="Zipcode").grid(row=5, column=0, padx=20)

# Create submit button
submit = Button(root, text="Submit", command=submit).grid(row=6, column=0, columnspan=2, sticky=E+W, padx=20, pady=10)

# Create query button
query_btn = Button(root, text="Show records", command=query).grid(row=7, column=0, columnspan=2, padx=20, pady=10, ipadx=137)

# Create a delete button
delete_btn = Button(root, text="Delete record", command=delete).grid(row=8, column=0, columnspan=2, padx=20, pady=10, sticky=E+W)

root.mainloop()