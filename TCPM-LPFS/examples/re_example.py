# Author: Tracy Vierra
# Date Created: 3/2/2022
# Date Modified: 3/2/2022

# Description:

# Usage:

import re

pattern = r"bacon"	

if re.match(pattern, "bacon"):
	print("Match bacon!") 
else:
	print("No match!")


if re.match(pattern, "eggs"):
	print("Match eggs!")
else:
	print("No match!")


if re.search(pattern, "bacon"): 	# using re.search instead of re.match
	print("Match bacon!")
else:
	print("No match!")


if re.findall(pattern, "bacon"):
	print("Match!") 
else:
	print("No match!")

print(re.match(pattern, "bacon"))
print(re.search(pattern, "bacon"))
print(re.findall(pattern, "bacon"))


