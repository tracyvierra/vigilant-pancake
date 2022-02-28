# Author: Tracy Vierra
# Date Created: 2/28/2022
# Date Modified: 2/28/2022

# Description:

# Usage:

newlist = [1, 3, 4, 5, 7, 2, 9, 11, 13]

result = list(filter(lambda x: x % 2 == 0, newlist))		# filter applies the lambda to each element in the list

print(result)
