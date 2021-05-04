import random 

def dice_roll():
    NUM_SIDES = num_sides = int(input("Number of sides for the die or dice: ")) 
    NUM_DICE = num_dice = int(input("Number of dice to roll: ")) 
    MIN_SIDES = 1
    MAX_SIDES = NUM_SIDES
    j = 0
    print("")

    for i in range(NUM_DICE):
        die_roll = int(random.randint(MIN_SIDES,NUM_SIDES))
        print("Your " + str(NUM_SIDES) + " sided roll is: " + str(die_roll))
        j = die_roll + j
    
    total = j 
    print("")   
    print("Total = " + str(total))
    print("")
    roll_again = input("roll again? ")
    while roll_again == "Yes" or "Y":
        dice_roll()
    if roll_again == "No" or "N":
        print("Thank you for playing!")
    else:
        print("please enter Yes (Y) or No (N). ")

print("Welcome to Tracy's Dice roller app!")
print("")

dice_roll()

