# Author: Tracy Vierra
# Date Created: 2/24/2022
# Date Modified: 2/24/2022

# Description:
# interest calculator

# Usage:
print("Welcome to our simple interest:\n")
p = int(input('Please enter the principal amount: '))
n = int(input('Please enter the number of years: '))
r = int(input('Please enter the rate of interest: '))
print("\n")
si = (p*n*r)/100            # simple interest calculation
print("simple interest: ")
print(si)

