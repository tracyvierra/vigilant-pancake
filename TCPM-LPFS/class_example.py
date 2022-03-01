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

# teddy1 = Teddy()
# print(teddy1.quantity)
# teddy2 = Teddy()
# print(teddy2.quantity)
# teddy1.quantity = 300  			# change the class attribute
# print(teddy1.quantity)
# print(teddy2.quantity)
print("\n")

teddy3 = Teddy("blue", "Teddy")
print(teddy3.name)
print(teddy3.color)
print(teddy3.quantity)

print("\n")

teddy4 = Teddy("green", "Ted")
print(teddy4.name)
print(teddy4.color)
print(teddy4.quantity)

print("\n")

teddy5 = Teddy("pink", "Tedwina")
print(teddy5.name)
print(teddy5.color)
print(teddy5.quantity)

print("\n")



