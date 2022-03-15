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

for (idx, val) in enumerate(number):
	if idx % 2 != 0:
		odd_sum += int(val)
	else:
		double_list.append(int(val) * 2)
		
		

print(double_list)
print(odd_sum)

	