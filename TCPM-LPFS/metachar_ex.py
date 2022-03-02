# Author: Tracy Vierra
# Date Created: 3/2/2022
# Date Modified: 3/2/2022

# Description:

# Usage:

import re

pattern = r"gr.y"			# using . to match any character
if re.match(pattern, "gray"):
	print("Match gray!")
if re.match(pattern, "grey"):
	print("Match grey!")
else:
	print("No match!")

pattern2 = r"^gr..$"			# using ^ to match beginning of string, $ to match end of string
if re.match(pattern2, "gray"):
	print("Match gray!")
if re.match(pattern2, "grey"):
	print("Match grey!")
else:
	print("No match!")

pattern3 = r"^gr{a||e}y$"		# using {a || e} to match a or e	
if re.match(pattern3, "gray"):
	print("Match gray!")
if re.match(pattern3, "grey"):
	print("Match grey!")
else:
	print("No match!")



pattern5 = r"^gr[a,e]y$"		# using [a,e] to match 2 specific characters
if re.match(pattern5, "gray"):
	print("Match gray!")
if re.match(pattern5, "grey"):
	print("Match grey!")
else:
	print("No match!")


pattern6 = r"[A-Z][A-Z][0-9]"		# using [A-Z] to match any capital letter, [0-9] to match any number
if re.match(pattern6, "ABC123"):
	print("Match ABC123!")
else:
	print("No match!")

if re.match(pattern6, "AB3"):
	print("Match AB3!")
else:
	print("No match!")

if re.match(pattern6, "GB4"):
	print("Match GB4!")
else:
	print("No match!")


