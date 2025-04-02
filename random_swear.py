import random

print ("Random Dice Swear🎲")
print ("")

dice_sides = 8

def roll():
    roll_dice = random.randint (1,dice_sides)
    print ("You rolled", roll_dice)
    if roll_dice == 1:
        print ("Wanker") 
    elif roll_dice == 2:
        print ("Tosser")
    elif roll_dice == 3:
        print ("Bell-end")
    elif roll_dice == 4:
        print ("Knob") 
    elif roll_dice == 5:
        print ("Twat")
    elif roll_dice == 6:
        print ("Gobshite")
    elif roll_dice == 7:
        print ("Bollocks")  
    elif roll_dice == 8:
        print ("Slag")  
    print ("")
    roll_again = input("Roll again? ")
    if roll_again == "yes":
        roll()
    elif roll_again == "no":
        exit()
    else:
        roll()

roll()
