# Author: Tracy Vierra
# Date Created: 3/2/2022
# Date Modified: 3/2/2022

# Description:

# Usage:

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(numbers)			# print whole set
print(5 in numbers)		# check if 5 is in set
print(11 in numbers)		# check if 11 is in set
numbers.add(11)			# add 11 to set
print(11 in numbers)		# check if 11 is in set
print(numbers)			# print whole set
numbers.remove(11)		# remove 11 from set
print(numbers)			# print whole set
numbers.discard(11)		# remove 11 from set if it exists
print(numbers)			# print whole set
numbers.clear()			# remove all elements from set
print(numbers)			# print whole set


seta = {1, 2, 3, 4, 5}
setb = {4, 5, 6, 7, 8}

print(seta.union(setb))				# print union of seta and setb
print(seta.intersection(setb))			# print intersection of seta and setb
print(seta.difference(setb))			# print difference of seta and setb
print(seta.symmetric_difference(setb))		# print symmetric difference of seta and setb
print(seta.issubset(setb))			# check if seta is subset of setb
print(seta.issuperset(setb))			# check if seta is superset of setb
print(seta.isdisjoint(setb))			# check if seta and setb have no common elements

print(seta | setb)				# print union of seta and setb
print(seta & setb)				# print intersection of seta and setb
print(seta - setb)				# print difference of seta and setb
print(seta ^ setb)				# print symmetric difference of seta and setb
print(seta <= setb)				# check if seta is subset of setb
print(seta >= setb)				# check if seta is superset of setb
print(seta.isdisjoint(setb))			# check if seta and setb have no common elements
