print("Hello World!")

# square root without using a math module.
print(144**(1/2))

if 144**(1/2) == 12:
    print("The square root of 144 is 12.")
else:
    print("The square root of 144 is not 12.")

# to check if a number is even or odd:

num=int(input("Enter a number: "))
if num % 2 == 0:    # if the number is even a 0 is returned, if the number is odd a 1 is returned.
    print(f'{num} is even')
else:
    print(f'{num} is odd')


# to check if a number is positive or negative:
number=int(input("Enter a number: "))
if number > 0:
    print(f'{number} is positive')
elif number < 0:
    print(f'{number} is negative')
else:
    print(f'{number} is zero')

