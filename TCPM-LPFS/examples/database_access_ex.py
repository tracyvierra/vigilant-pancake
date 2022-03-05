# Author: Tracy Vierra
# Date Created: 3/4/2022
# Date Modified: 3/4/2022

# Description:

# Usage:

import psycopg2

conn = psycopg2.connect(database="studentdb", user="postgres", password="Tr1cky1!", host="localhost", port="5432")
cur = conn.cursor()
cur.execute('''CREATE TABLE new_students(ID SERIAL, NAME TEXT, AGE TEXT, ADDRESS TEXT);''')
cur.execute('''INSERT INTO new_students(NAME, AGE, ADDRESS) VALUES('Tracy Vierra', '52', '123 Main St');''')
cur.execute('''INSERT INTO new_students(NAME, AGE, ADDRESS) VALUES('John Smith', '23', '456 Main St');''')
cur.execute('''INSERT INTO new_students(NAME, AGE, ADDRESS) VALUES('Jane Doe', '34', '789 Main St');''')
cur.execute('''SELECT * FROM new_students;''')
conn.commit()
conn.close()
print("Opened database successfully")


