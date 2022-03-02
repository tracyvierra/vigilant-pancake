# Author: Tracy Vierra
# Date Created: 3/2/2022
# Date Modified: 3/2/2022

# Description:

# Usage:


class MyClass:
	__hiddenvariable = 0			# creates a hidden variable inside the class

	def add (self, increment):
		self.__hiddenvariable += increment
		return self.__hiddenvariable
	
objectone = MyClass()
objectone.add(5)
print(objectone.add(5))
print(objectone.__hiddenvariable)


