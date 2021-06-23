name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if age <= 17 or age >= 30:
    print("Sorry, {0} you are not in the correct age range for this Holiday trip.".format(name))
else:
    print("Welcome to the Holiday Trip!   Please follow Gopher and Julie ...")