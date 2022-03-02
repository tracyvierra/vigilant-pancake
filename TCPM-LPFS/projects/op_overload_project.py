# Author: Tracy Vierra
# Date Created: 3/2/2022
# Date Modified: 3/2/2022

# Description:

# Usage:

class Oddity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x * other.y
    
    def __mul__(self, other):
        return self.x + other.y


oddity1 = Oddity(1, 2)
oddity2 = Oddity(3, 4)
print(oddity1 + oddity2)
print(oddity1 * oddity2)


# Their solution: 

class Number:

    def __init__(self,x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return x

number_a = Number(3)

number_b = Number(4)

print(number_a * number_b)

