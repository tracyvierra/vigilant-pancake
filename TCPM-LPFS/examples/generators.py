# Author: Tracy Vierra
# Date Created: 2/28/2022
# Date Modified: 2/28/2022

# Description:

# Usage:

def function():
    counter = 0
    while counter < 5:
        yield counter
        counter += 1

for x in function():
    print(x)

# 


def even_numbers(X):
    for x in range(X):
        if x % 2 == 0:
            yield x
print(" ")
print(list(even_numbers(20)))
print(" ")

