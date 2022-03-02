# Author: Tracy Vierra
# Date Created: 3/2/2022
# Date Modified: 3/2/2022

# Description:

# Usage:

from itertools import count, accumulate, takewhile

n = int(input("Enter a number less than 10: "))
for i in count(n):
    print(i)
    if i >= 10:
        break

numbers = list(accumulate(range(8)))	
print(numbers)

print(list(takewhile(lambda x: x < 10, numbers)))

