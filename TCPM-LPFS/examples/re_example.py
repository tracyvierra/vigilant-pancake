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
