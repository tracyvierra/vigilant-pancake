# Author: Tracy Vierra
# Date Created: 2/25/2022
# Date Modified: 2/25/2022

# Description:

# Usage:

# to get around errors that you can anticipate use a try and except block

try:
    a = 20
    b = 0
    print(a/b)    # do something
except:
    # handle the error
    ZeroDivisionError
    print("You can't divide by zero")
