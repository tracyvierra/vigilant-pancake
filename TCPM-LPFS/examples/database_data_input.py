# Author: Tracy Vierra
# Date Created: 3/4/2022
# Date Modified: 3/7/2022

# Description:

# Usage:

import psycopg2

def create_table():
	try:
		conn = psycopg2.connect(database="studentdb", user="postgres", password="Tr1cky1!", host="localhost", port="5432")
		cur = conn.cursor()
		cur.execute('''CREATE TABLE new_students(ID SERIAL, NAME TEXT, AGE TEXT, ADDRESS TEXT);''')

		conn.commit()
		conn.close()
		print("Table created successfully in PostgreSQL ")
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		
def insert_data():
	conn = psycopg2.connect(database="studentdb", user="postgres", password="Tr1cky1!", host="localhost", port="5432")
	cur = conn.cursor()
	name = input("Enter name: ")
	age = input("Enter age: ")
	address = input("Enter address: ")

	query = '''INSERT INTO new_students (NAME, AGE, ADDRESS) VALUES (%s, %s, %s);'''
	cur.execute(query,(name,age,address))

	conn.commit()
	conn.close()
	print("Record inserted successfully into new_students table")
	print(" ")




while True:
	print("1. Create table")
	print("2. Insert data")
	print("3. Exit")
	print(" ")
	choice = int(input("Enter choice: "))
	if choice == 1:
		create_table()
	elif choice == 2:
		insert_data()
	elif choice == 3:
		break
	else:
		print("Invalid choice")


