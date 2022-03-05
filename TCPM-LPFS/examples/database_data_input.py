# Author: Tracy Vierra
# Date Created: 3/4/2022
# Date Modified: 3/4/2022

# Description:

# Usage:

import psycopg2

def create_table():
	conn = psycopg2.connect(database="studentdb", user="postgres", password="Tr1cky1!", host="localhost", port="5432")
	cur = conn.cursor()
	cur.execute('''CREATE TABLE new_students(ID SERIAL, NAME TEXT, AGE TEXT, ADDRESS TEXT);''')

	conn.commit()
	conn.close()
	print("Table created successfully in PostgreSQL ")

def insert_data():
	conn = psycopg2.connect(database="studentdb", user="postgres", password="Tr1cky1!", host="localhost", port="5432")
	cur = conn.cursor()
	cur.execute('''INSERT INTO new_students (NAME, AGE, ADDRESS) VALUES (%s, %s, %s);''', ('Jerry', '21', '1123 Main St.'))
	cur.execute('''INSERT INTO new_students (NAME, AGE, ADDRESS) VALUES (%s, %s, %s);''', ('Tom', '25', '1456 Main St.'))
	cur.execute('''INSERT INTO new_students (NAME, AGE, ADDRESS) VALUES (%s, %s, %s);''', ('Mary', '26', '7819 Main St.'))

	conn.commit()
	conn.close()
	print("Records created successfully in PostgreSQL ")


def input_create_table():
	dbname = input("Enter the name of the database: ")
	username = input('Enter the username: ')
	password = input('Enter the password: ')
	host = input('Enter the host: ')
	port = input('Enter the port: ')
	
	table_name = input("Enter table name: ")
	
	conn = psycopg2.connect(database=dbname, user=username, password=password, host=host, port=port)
	cur = conn.cursor()
	cur.execute('''CREATE TABLE dbname();''')
	conn.commit()
	conn.close()
	print("Table created successfully in PostgreSQL ")

	num_columns = int(input("Enter the number of columns: "))
	while num_columns != 0:
		column_name = input("Enter the column name: ")
		column_type = input("Enter the column type: ")
		cur = conn.cursor()
		cur.execute('''INSERT INTO table_name (column_name) VALUES (%s, %s, %s);''', ('Tom', '25', '1456 Main St.'))
		
		num_columns = num_columns - 1
	
	# conn = psycopg2.connect(database="studentdb", user="postgres", password="Tr1cky1!", host="localhost", port="5432")
	conn = psycopg2.connect(database=dbname, user=username, password=password, host=host, port=port)

	cur = conn.cursor()
	cur.execute('''CREATE TABLE table_name(ID SERIAL, NAME TEXT, AGE TEXT, ADDRESS TEXT);''')

	conn.commit()
	conn.close()
	print("Table created successfully in PostgreSQL ")

	


