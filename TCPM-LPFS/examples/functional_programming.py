# Author: Tracy Vierra
# Date Created: 2/28/2022
# Date Modified: 2/28/2022

# Description:

# Usage:

def add_ten(x):
    return x+10

def twice(func, arg):
    return func(func(arg))

print(twice(add_ten, 5))
