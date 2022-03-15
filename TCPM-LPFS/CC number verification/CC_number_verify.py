# Author: Tracy Vierra
# Date Created: 3/15/2022
# Date Modified: 3/15/2022

# Description: CC number verification program using the Luhn Algorithm

# Usage:

# example: 5610591081018250
card_num = input("Enter a credit card number: ")
odd_sum = 0
double_list = []
even_sum = 0
number = list(card_num)
double_string = ""

for (idx, val) in enumerate(number):
	if idx % 2 != 0:
		odd_sum += int(val)
	else:
		double_list.append(int(val) * 2)

# converting the list back to a string.
double_string = ""
for x in double_list:
	double_string += str(x)

# Converting the string back to a list.
double_list = list(double_string)

for x in double_list:
	even_sum += int(x)

net_sum = odd_sum + even_sum
if net_sum % 10 == 0:
	print("The number is valid.")
else:
	print("The number is invalid.")


# print(double_list)
# print(double_string)
# print(odd_sum)
# print(even_sum)

