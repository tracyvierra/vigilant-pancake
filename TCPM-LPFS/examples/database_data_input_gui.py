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






# def create_table():
# 	try:
# 		conn = psycopg2.connect(database="studentdb", user="postgres", password="Tr1cky1!", host="localhost", port="5432")
# 		cur = conn.cursor()
# 		cur.execute('''CREATE TABLE new_students(ID SERIAL, NAME TEXT, AGE TEXT, ADDRESS TEXT);''')

# 		conn.commit()
# 		conn.close()
# 		print("Table created successfully in PostgreSQL ")
# 	except (Exception, psycopg2.DatabaseError) as error:
# 		print(error)
		
# def insert_data():
# 	conn = psycopg2.connect(database="studentdb", user="postgres", password="Tr1cky1!", host="localhost", port="5432")
# 	cur = conn.cursor()
# 	name = input("Enter name: ")
# 	age = input("Enter age: ")
# 	address = input("Enter address: ")

# 	query = '''INSERT INTO new_students (NAME, AGE, ADDRESS) VALUES (%s, %s, %s);'''
# 	cur.execute(query,(name,age,address))

# 	conn.commit()
# 	conn.close()
# 	print("Record inserted successfully into new_students table")
# 	print(" ")




# while True:
# 	print("1. Create table")
# 	print("2. Insert data")
# 	print("3. Exit")
# 	print(" ")
# 	choice = int(input("Enter choice: "))
# 	if choice == 1:
# 		create_table()
# 	elif choice == 2:
# 		insert_data()
# 	elif choice == 3:
# 		break
# 	else:
# 		print("Invalid choice")


