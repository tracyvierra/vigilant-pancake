# Author: Tracy Vierra
# Date Created: 2/25/2022
# Date Modified: 2/25/2022

# Description:

# Usage:

def function1():
    print("This is function 1")

def square_root(x):
    return x**0.5

print(" ")

function1()

print(" ")

print(square_root(2))
print(square_root(6))
print(square_root(9))
print(square_root(16))
print(square_root(25))
print(square_root(36))
print(square_root(49))
print(square_root(64))
print(square_root(81))
print(square_root(100))
print(square_root(121))
print(square_root(144))

# function arguments
def add(a,b):
    print(a+b)
    return a+b
print(" ")

add(3,4)
add(5,6)
add(7,8)
add(9,10)
add(11,12)

print(" ")

# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print("Inside the function : ", total)
   return total;

# Now you can call sum function
total = sum( 10, 20 );
print("Outside the function : ", total)

print(" ")


# pass one functions results to another function
def add(a,b):
    return a+b

def square(a):
    return a**2

print(square(add(3,4)))
print(square(add(2,3)))

print(" ")




