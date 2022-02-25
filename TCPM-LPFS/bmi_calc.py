# Author: Tracy Vierra
# Date Created: 2/25/2022
# Date Modified: 2/25/2022

# Description:

# Usage:

# US units: BMI = (weight (lb) ÷ height2 (in)) * 703

def bmi(w,h):
    bmi = w/(h**2) *703
    return bmi

input_weight = float(input("Enter your weight in pounds: "))
input_height = float(input("Enter your height in inches: "))

bmi = bmi(input_weight,input_height)
print("Your BMI is: ",bmi)
