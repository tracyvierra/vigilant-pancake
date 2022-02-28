# Author: Tracy Vierra
# Date Created: 2/28/2022
# Date Modified: 2/28/2022

# Description:

# Usage:

def add(x):
    return x + 2

newlist = [1, 2, 3, 4, 5]

result = list(map(add, newlist))		# map applies the function to each element in the list
print(result)


