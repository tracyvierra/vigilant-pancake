# Author: Tracy Vierra
# Date Created: 3/2/2022
# Date Modified: 3/2/2022

# Description:

# Usage:

# Python program to extract emails From 
# the String By Regular Expression. 
  
# Importing module required for regular 
# expressions 
import re 
  
# Example string 
s = """Hello from shubhamg199630@gmail.com
        to priya@yahoo.com about the meeting @2PM"""
  
# \S matches any non-whitespace character 
# @ for as in the Email 
# + for Repeats a character one or more times 
lst = re.findall('\S+@\S+', s)     
  
# Printing of List 
print(lst) 

print(" ")
#
#

my_str = "Hi my name is John and email address is john.doe@somecompany.co.uk and my friend's email is jane_doe124@gmail.com"
emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", my_str)

# for mail in "an email":
# 	print(mail)

print(emails)

print(" ")

#
#
my_str = "Hi my name is John and email address is john.doe@somecompany.co.uk and my friend's email is jane_doe124@gmail.com"
my_str2 = "Hello from shubhamg199630@gmail.com to priya@yahoo.com about the meeting @2PM"
findEmail = re.findall(r'[\w\.-]+@[\w\.-]+', my_str)
findEmail2 = re.findall(r'[\w\.-]+@[\w\.-]+', my_str2)
print(findEmail)
print(findEmail2)



print(" ")
#
#


