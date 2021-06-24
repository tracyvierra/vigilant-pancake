'''ask for name and age
check if person is the right age to go on an 18-30 holiday 
(they must be over 18 and under 30)
If they are eligible print a welcome message, if not a polit message refusing them entry.
'''
print(" ")
name = input("Please enter your name: ")
age = int(input("Please enter your age, {0}: ".format(name)))
print(" ")

if age <= 17 or age >= 30:
    print("Sorry, {0} you are not in the correct age range for this Holiday trip.".format(name))
    print(" ")
else:
    print("Welcome to the Holiday Trip, {0}!   Please follow Gopher and Julie ...".format(name))
    print("\a")
    print(" ")