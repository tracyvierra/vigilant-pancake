# Author: Tracy Vierra
# Date Created: 3/11/2022
# Date Modified: 3/11/2022

# Description:

# Usage:

import bcrypt
import getpass
import sys

password = b"Thisismypassword"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

entered_password = input("Enter your password: ")
entered_password = entered_password.encode()
# entered_password = bytes(entered_password, encoding="utf-8")

# bcrypt.checkpw(entered_password, hashed)

if bcrypt.checkpw(entered_password, hashed):
    print("Password is correct")
else:
    print("Password is incorrect")

