# Author: Tracy Vierra
# Date Created: 3/1/2022
# Date Modified: 3/1/2022

# Description:

# Usage:


class Teddy:
	quantity = 200				# class attribute	
	def __init__(self, color, name):	# constructor
		self.color = color		# instance attribute
		self.name = name		# instance attribute


	def change_color(self, color):		# instance method
		print("This is a method")
		self.color = "White"

teddy1 = Teddy("Red", "Teddy")
print(teddy1.name)
print(teddy1.color)

teddy1.change_color("Blue")
print(teddy1.name)
print(teddy1.color)
