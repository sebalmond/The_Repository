import random

print ("Infinity Dice 🎲")
print ("")

dice_sides = int(input("How many sides?"))

def roll():
  roll_dice = random.randint (1,dice_sides)
  print ("You rolled", roll_dice)
  print ("")
  roll_again = input("Roll again?")
  if roll_again == "yes":
    roll()
  elif roll_again== "no":
    exit()
  else:
    roll()

roll()

# import random
# print("Infinity Dice 🎲")
  
# sides = int(input("How many sides?: "))
# playGame = "yes"
  
# def rollDice(sides):
#   print("You rolled ", random.randint(1,sides))
# while playGame == "yes":
#     rollDice(sides)
#     playGame = input("Roll again?")