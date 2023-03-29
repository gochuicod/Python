from mysql.connector import connect
from tkinter import ttk
import tkinter as tk
import bcrypt

# creates database connection
conn = connect(
    host="localhost",
    user="gochuicod",
    password="20259388",
    database="pythondb",
)
# creates a cursor for the database
cursor = conn.cursor()

# initiates window creation
window = tk.Tk()

# sets window title
window.title("Student Database")

# set window size
window.geometry("1000x500")

# instantiates treeview
treeview = ttk.Treeview(window)

# removes empty column headings
treeview["show"] = "headings"

def generateStudentTree():
    cursor.execute("SELECT * FROM students")

    # this clears the treeview list items
    emptyTreeView()

    # define columns for the Treeview widget
    treeview['columns'] = ('Student ID','Firstname','Lastname','Course','Level')

    # set column headings
    treeview.heading('Student ID', text='Student ID')
    treeview.heading('Firstname', text='Firstname')
    treeview.heading('Lastname', text='Lastname')
    treeview.heading('Course', text='Course')
    treeview.heading('Level', text='Level')

    # add the data to the tree
    for item in reversed(cursor.fetchall()):
        treeview.insert("","0",values=(item[0],item[1],item[2],item[3],item[4]))

def generateUserTree():
    cursor.execute("SELECT * FROM users")

    # this clears the treeview list items
    emptyTreeView()

    # define columns for the Treeview widget
    treeview['columns'] = ('ID', 'Username','Password','Student ID')

    # set column headings
    treeview.heading('ID', text='ID')
    treeview.heading('Username', text='Username')
    treeview.heading('Password', text='Password')
    treeview.heading('Student ID', text='Student ID')

    # add the data to the tree
    for item in reversed(cursor.fetchall()):
        treeview.insert("","0",values=(item[0],item[1],item[2],item[3]))

def emptyTreeView():
    [treeview.delete(item) for item in treeview.get_children()]

# create a generate students button and then packs it
button = tk.Button(window, text="Generate Students", command=generateStudentTree)
button.pack()

# create a generate users button and then packs it
button = tk.Button(window, text="Generate Users", command=generateUserTree)
button.pack()

# packs the tree
treeview.pack()

# executes main loop
window.mainloop()

# closes database connection
conn.close()