# Author: Tracy Vierra
# Date Created: 3/7/2022
# Date Modified: 3/7/2022

# Description:

# Usage:

from tkinter import *
import tkinter as tk 
import psycopg2

root = Tk()
root.title("Database Data Input")
# root.geometry("900x500")
canvas = Canvas(root, width = 900, height = 500)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text="Student Database Data Input",)
label.grid(row=0, column=1,)

label = Label(frame, text="Name:")
label.grid(row=1, column=0)

label = Label(frame, text="Age:")
label.grid(row=2, column=0)

label = Label(frame, text="Address:")
label.grid(row=3, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

button = Button(frame, text="Submit", command=lambda: get_data(entry_name.get(), entry_age.get(), entry_address.get()))
button.grid(row=4, column=1)

button_clear = Button(frame, text="Clear", command=lambda: clear_data())
button_clear.grid(row=5, column=1)


label_search = Label(frame, text="Search:")
label_search.grid(row=8, column=0)

id_search = Entry(frame)
id_search.grid(row=8, column=1)
button_search = Button(frame, text="Search", command=lambda: search_data(id_search.get()))
button_search.grid(row=9, column=1)


def search_data(id):
	try:
		conn = psycopg2.connect(database="studentdb", user="postgres", password="Tr1cky1!", host="localhost", port="5432")
		cur = conn.cursor()
		id = id_search.get()
		query = '''SELECT * FROM new_students WHERE ID = %s;'''
		cur.execute(query,(id,))
		row = cur.fetchone()
		print(" ")
		print("ID: ", row[0])
		print("Name: ", row[1])
		print("Age: ", row[2])
		print("Address: ", row[3])
		print(" ")
		conn.commit()
		conn.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)



def clear_data():
	entry_name.delete(0, END)
	entry_age.delete(0, END)
	entry_address.delete(0, END)


def get_data(name,age,address):
	try:
		conn = psycopg2.connect(database="studentdb", user="postgres", password="Tr1cky1!", host="localhost", port="5432")
		cur = conn.cursor()
		name = entry_name.get()
		age = entry_age.get()
		address = entry_address.get()

		query = '''INSERT INTO new_students (NAME, AGE, ADDRESS) VALUES (%s, %s, %s);'''
		cur.execute(query,(name,age,address))

		conn.commit()
		conn.close()
		print("Record inserted successfully into new_students table")
		print(" ")
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)	



root.mainloop()


