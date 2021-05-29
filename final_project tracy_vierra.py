'''
Code In Place 2021 Final Project -- Tracy Vierra

This program is a game tool that helps the GM roll odd sized dice for any role playing game, 
players in a board game can use it for any sized dice that are needed.  Authors and NPC (Non Player Characters)
designers can use it to generate random selections from lists used to create characters, plots, themes, adventures, etc.

'''
import random 

'''
The dice_roll function takes the number of sides entered by the user and "creates" the dice of that size.
The number of dice entered is the number of times to roll, and show the result.  Finally, in case it is needed,
the total of the rolls is also shown.  You can keep rolling as needed by entering y to continue or n to quit.  
'''
def dice_roll():
    NUM_SIDES = num_sides = int(input("Number of sides for the die or dice: ")) 
    NUM_DICE = num_dice = int(input("Number of dice to roll: ")) 
    MIN_SIDES = 1
    MAX_SIDES = NUM_SIDES
    total = 0

    print("")

    for i in range(NUM_DICE):
        die_roll = int(random.randint(MIN_SIDES,NUM_SIDES))
        print("Your " + str(NUM_SIDES) + " sided roll is: " + str(die_roll))
        total += die_roll
    
    print("")   
    print("Total = " + str(total))
    print("")
    return total
    



print("")
print("Welcome to Tracy's Dice roller app!")
print("")

dice_roll()                             # See above 

answer = input("roll again? ")          # Check if they want to continue.

while answer == "y":
    print("")
    dice_roll()                                     # Keep rolling while they enter y
    answer = input("roll again? ")                  # Ask again after the roll.
if answer == "n":       
    print("")
    print("Thank you for playing!")
    print("")
else:
    print("")
    print("please enter Yes (y) or No (n). ")       # Just in case they enter something other than y or n
    print("")
    answer = input("roll again? ")
    while answer == "y":
        dice_roll()                                 # Keep rolling while they enter y
        