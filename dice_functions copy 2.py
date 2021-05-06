import random 

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
    
def roll_again():
    roll_again = input("roll again? ")
    while roll_again == "y":
        print("")
        dice_roll()
        roll_again = input("roll again? ")
    if roll_again == "n":       
        print("")
        print("Thank you for playing!")
        print("")
    else:
        print("")
        print("please enter Yes (y) or No (n). ")
        print("")
        
        

print("")
print("Welcome to Tracy's Dice roller app!")
print("")

dice_roll()
roll_again()
while roll_again == "y":
    dice_roll()


