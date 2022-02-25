# Author: Tracy Vierra
# Date Created: 2/25/2022	
# Date Modified: 2/25/2022

# Description:

# Usage:

file = open("demo.txt", 'w') # open file in write mode
file.write("This is a test") # write to file
file.close() # close file

file2 = open("demo2.txt", 'w') # open file in write mode
file2.write("This is another test") # write to file
file2.close() # close file

file3 = open("demo3.txt", 'r') # open file in read mode
print(file3.read()) # read file
print(file3.readline(2)) # read line
file3.close() # close file

