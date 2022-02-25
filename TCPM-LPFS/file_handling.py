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

file5 = open("demo3.txt", 'w') # open file in write mode
file5.write("This is the first line of the file.") # write to file
file5.write("\nThis is the second line of the file.") # write to file
file5.close() # close file

file3 = open("demo3.txt", 'r') # open file in read mode
print(file3.read()) # read file
print(file3.readline(2)) # read line
file3.close() # close file

file4 = open("demo3.txt", 'r') # open file in read mode
content = file4.read() # read file
print(content)
second_line = file4.readline(2) # read line"
print(second_line)
file4.close() # close file


