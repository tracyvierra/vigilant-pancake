from stanfordkarel import *

"""
File: Max5Karel.py
------------------------------
Karel should place 5 beepers in the bottommost row of the world if the world is more than 5 columns wide.
If the world is less than 5 columns wide, Karel should fill the bottommmost row with beepers and not walk through any walls.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    place_ten_beepers()
    while front_is_clear():
        move()
        place_ten_beepers()
    

    

def place_ten_beepers():
    for i in range(10):
        put_beeper()






        


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()