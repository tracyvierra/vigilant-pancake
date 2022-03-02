# Author: Tracy Vierra
# Date Created: 3/2/2022
# Date Modified: 3/2/2022

# Description:

# Usage:

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


n = int(input("Enter a number: "))
print(factorial(n))


