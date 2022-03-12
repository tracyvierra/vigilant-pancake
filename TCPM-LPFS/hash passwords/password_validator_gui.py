# Author: Tracy Vierra
# Date Created: 3/11/2022
# Date Modified: 3/11/2022

# Description:

# Usage:

from turtle import position
from wsgiref import validate
import bcrypt
import tkinter as tk
from tkinter import ttk


# password = b"Thisismypassword"
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# print(hashed)

# entered_password = input("Enter your password: ")
# entered_password = entered_password.encode()


# entered_password = bytes(entered_password, encoding="utf-8")

# bcrypt.checkpw(entered_password, hashed)

# if bcrypt.checkpw(entered_password, hashed):
#     print("Password is correct")
# else:
#     print("Password is incorrect")

def hash_password(password):
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed

def validate(password):
    hashed = b'$2b$12$inUWKlF.24S/qsPLJNr91.uC.NtxVPke7na9fnirXdbQBvQhnJ7q6'
    password = bytes(password, encoding="utf-8")

    if bcrypt.checkpw(password, hashed):
        print("Password is correct")
    else:
        print("Password is incorrect")

root = tk.Tk()
root.title("Password Validator")
root.geometry("300x100")

label1 = tk.Label(root, text="Enter your password:")
label1.pack()

password_entry = tk.Entry(root)
password_entry.pack()

button_hash = tk.Button(root, text="Validate", command=lambda: validate(password_entry.get()))
button_hash.configure(background="green", foreground="white")
button_hash.pack()

button_exit = tk.Button(root, text="Exit", command=root.destroy)
button_exit.configure(background="red", foreground="black")
button_exit.pack(padx=5, pady=5)

root.mainloop()