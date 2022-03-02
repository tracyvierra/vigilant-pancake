# Author: Tracy Vierra
# Date Created: 3/2/2022
# Date Modified: 3/2/2022

# Description:

# Usage:

class Point:							
    def __init__(self, x, y):					# def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)	# return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)	# return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)		# return Point(self.x * other, self.y * other)
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)		# return "({}, {})".format(self.x, self.y)

point1 = Point(1, 2)
point2 = Point(3, 4)
print(point1 + point2)
print(point1 - point2)
print(point1 * point2)


    
