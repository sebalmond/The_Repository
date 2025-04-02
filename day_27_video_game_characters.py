import os, time
import random

name = ""
character = ""

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_health():
  roll_6_sided_dice = rollDice(6)
  roll_12_sided_dice = rollDice(12)
  health = ((roll_6_sided_dice * roll_12_sided_dice / 2) + 10)
  return health

def roll_attack_strength():
  roll_6_sided_dice = rollDice(6)
  roll_12_sided_dice = rollDice(12)
  attack_strength = ((roll_6_sided_dice * roll_12_sided_dice / 2) + 12)
  return attack_strength

def roll_name():
    roll_6_sided_dice = rollDice(6)
    if roll_6_sided_dice == 1:
        name = "Eric"
    elif roll_6_sided_dice == 2:
        name = "Chaz"
    elif roll_6_sided_dice == 3:
        name = "Barry"
    elif roll_6_sided_dice == 4:
        name = "Sheila"
    elif roll_6_sided_dice == 5:
        name = "Tarquin"
    elif roll_6_sided_dice == 6:
        name = "Fay"
    return name

def roll_character():  
    roll_12_sided_dice = rollDice(12)
    if roll_12_sided_dice == 1:
        character = "Bastard"
    elif roll_12_sided_dice == 2:
        character = "Relentless"
    elif roll_12_sided_dice == 3:
        character = "Twat"
    elif roll_12_sided_dice == 4:
        character = "Disgrace"
    elif roll_12_sided_dice == 5:
        character = "Mean"
    elif roll_12_sided_dice == 6:
        character = "Scary"
    elif roll_12_sided_dice == 7:
        character = "Naughty"
    elif roll_12_sided_dice == 8:
        character = "Idiot"
    elif roll_12_sided_dice == 9:
        character = "Brave"
    elif roll_12_sided_dice == 10:
        character = "Kind"
    elif roll_12_sided_dice == 11:
        character = "Lionheart"
    elif roll_12_sided_dice == 12:
        character = "Dim"
    return character
    
print("⚔️Random Character Generator⚔️")
print ("")
  

haveACharacter = "yes"

while haveACharacter == "yes":
    os.system("cls")
    print("Welcome to the game", roll_name(), "the", roll_character()) 
    print ("HEALTH:", roll_health())
    print ("STRENGTH:", roll_attack_strength())
    print ("")
    print ("May your name go down in Legend...")
    print ("")
    haveACharacter = input("Do you want to create another character? ")
   
