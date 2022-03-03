# Author: Tracy Vierra
# Date Created: 3/2/2022
# Date Modified: 3/2/2022

# Description:

# Usage:

import re

string = "abc"
pattern = r"a"

print(re.match(pattern, string))	# returns Match object at the start of the string
print(re.search(pattern, string))	# returns Match object by scanning the whole string
print(re.findall(pattern, string))	# returns list of Match objects

print(" ")
print("-------------------------------------")
if re.match(pattern, string):
	print("Match!")
else:
	print("No match!")

if re.search(pattern, string):	
	print("Match!")
else:
	print("No match!")

if re.findall(pattern, string):		
	print("Match!")
else:
	print("No match!")

print(" ")
print("-------------------------------------")
#
#

# Metacharacters - *, +, {...}, . , ^ , $

print("The * metacharacter: ")

if re.match(r"ab*c", "abc"):		# * matches zero or more of the preceding character
	print("Match!")
else:
	print("No match!")

if re.match(r"ab*c", "ac"):		# * matches zero or more of the preceding character
	print("Match!")
else:
	print("No match!")

print("-------------------------------------")	

print(" The + metacharacter: ")

if re.match(r"ab+c", "abbbc"):		# + matches one or more of the preceding character
	print("Match!")
else:
	print("No match!")

if re.match(r"ab+c", "ac"):		# + matches one or more of the preceding character
	print("Match!")
else:
	print("No match!")

print("-------------------------------------")

print("The {} metacharacter: ")

if re.match(r"ab{2}c", "abbbc"):	# {n} matches exactly n of the preceding character
	print("Match!")
else:
	print("No match!")

if re.match(r"ab{2}c", "abbc"):		# {n} matches exactly n of the preceding character
	print("Match!")
else:
	print("No match!")

print("-------------------------------------")

print("The . metacharacter: ")

if re.match(r"ab.c", "ab1c"):		# . matches any character except newline
	print("Match!")
else:
	print("No match!")

if re.match(r"ab.c", "ab\nc"):		# . matches any character except newline
	print("Match!")
else:
	print("No match!")

print("-------------------------------------")

print("The ^ metacharacter: ")

if re.match(r"^abc", "abc"):		# ^ matches the beginning of the string
	print("Match!")
else:
	print("No match!")

if re.match(r"^c", "c"):		# ^ matches the beginning of the string
	print("Match!")
else:
	print("No match!")

if re.match(r"ab^c", "abc"):		# ^ matches the beginning of the string
	print("Match!")
else:
	print("No match!")


print("-------------------------------------")

print("The $ metacharacter: ")

if re.match(r"abc$", "abc"):		# $ matches the end of the string
	print("Match!")
else:
	print("No match!")

if re.match(r"ab$", "abc"):		# $ matches the end of the string
	print("Match!")
else:
	print("No match!")


print("-------------------------------------")



print("-------------------------------------")