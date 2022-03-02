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

print("_______________________")

pattern2 = r"^gr..$"			# using ^ to match beginning of string, $ to match end of string
if re.match(pattern2, "gray"):
	print("Match gray!")
if re.match(pattern2, "grey"):
	print("Match grey!")
else:
	print("No match!")

print("_______________________")

pattern3 = r"^gr{a||e}y$"		# using {a || e} to match a or e	
if re.match(pattern3, "gray"):
	print("Match gray!")
if re.match(pattern3, "grey"):
	print("Match grey!")
else:
	print("No match!")

print("_______________________")

pattern5 = r"^gr[a,e]y$"		# using [a,e] to match 2 specific characters
if re.match(pattern5, "gray"):
	print("Match gray!")
if re.match(pattern5, "grey"):
	print("Match grey!")
else:
	print("No match!")

print("_______________________")

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

print("_______________________")

pattern7 = r"eggs(bacon)*"		# using * to match 0 or more of the preceding pattern	
if re.match(pattern7, "eggsbacon"):
	print("Match eggsbacon!")
else:
	print("No match!")

if re.match(pattern7, "eggs"):
	print("Match eggs!")
else:
	print("No match!")

if re.match(pattern7, "eggsbaconbacon"):
	print("Match eggsbaconbacon!")
else:
	print("No match!")

if re.match(pattern7, "eggsbaconbaconbacon"):
	print("Match eggsbaconbaconbacon!")
else:
	print("No match!")

if re.match(pattern7, "tracyvierra"):
	print("Match tracyvierra!")
else:
	print("No match!")

print("_______________________")

pattern8 = r"eggs(bacon)*"		# using + to match 1 or more of the preceding pattern
if re.match(pattern8, "eggsbacon"):
	print("Match eggsbacon!")
else:
	print("No match!")

if re.match(pattern8, "eggs"):
	print("Match eggs!")
else:
	print("No match!")

if re.match(pattern8, "eggsbaconbacon"):
	print("Match eggsbaconbacon!")
else:
	print("No match!")

if re.match(pattern8, "tracyvierra"):
	print("Match tracyvierra")
else:
	print("No match!")

print("_______________________")

pattern9 = r"eggs(bacon)?"		# using ? to match 0 or 1 of the preceding pattern
if re.match(pattern9, "eggsbacon"):
	print("Match eggsbacon!")
else:
	print("No match!")

if re.match(pattern9, "eggs"):
	print("Match eggs!")
else:
	print("No match!")

if re.match(pattern9, "eggsbaconbacon"):
	print("Match eggsbaconbacon!")
else:
	print("No match!")

if re.match(pattern9, "tracyvierra"):
	print("Match tracyvierra")
else:
	print("No match!")

if re.match(pattern9, "bacon"):
	print("Match bacon!")
else:
	print("No match!")

print("_______________________")

pattern10 = r"bread(eggs)*bread"		# using () to group patterns
if re.match(pattern10, "breadeggseggsbread"):
	print("Match breadeggseggseggsbread!")
else:
	print("No match!")

if re.match(pattern10, "bread eggs eggs eggs bread"):
	print("Match bread eggs eggs eggs bread!")
else:
	print("No match!")

if re.match(pattern10, "breadbread"):
	print("Match bread bread!")
else:
	print("No match!")

if re.match(pattern10, "breadeggsbread"):
	print("Match bread eggs bread!")
else:
	print("No match!")

print("_______________________")




print("_______________________")