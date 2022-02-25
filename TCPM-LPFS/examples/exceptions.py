# Author: Tracy Vierra
# Date Created: 2/25/2022
# Date Modified: 2/25/2022

# Description:

# Usage:

# to get around errors that you can anticipate use a try and except block
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)

x = float(input("Enter a number: "))
y = float(input("Enter the number to divide by: "))

divide(x, y)


'''
try:
    a = 20
    b = 0
    print(a/b)    # do something
except:
    # handle the error
    ZeroDivisionError
    print("You can't divide by zero")

finally:
    # do something regardless of the error
    print("I'm done")

'''