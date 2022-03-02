# Author: Tracy Vierra
# Date Created: 3/2/2022
# Date Modified: 3/2/2022

# Description:

# Usage:

import re

string = "My name is John, Hi I'm John"

pattern = r"John"

newstring = re.sub(pattern, "Rob", string)	# replace all instances of John with Rob

print(string)
print(newstring)
