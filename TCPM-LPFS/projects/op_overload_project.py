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
