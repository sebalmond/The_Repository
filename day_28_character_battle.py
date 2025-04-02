import random, os, time

round = 1
winner = None

player1name = ""
player1character = ""
player1health = 0
player1strength = 0

player2name = ""
player2character = ""
player2health = 0
player2strength = 0


def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_health():
  health = ((rollDice(6) * rollDice(12) / 2) + 10)
  return health

def roll_attack_strength():
  attack_strength = ((rollDice(6) * rollDice(12) / 2) + 12)
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
    


print ("⚔️ BATTLE TIME ⚔️")
print ("")
player1name = roll_name() + " the " + roll_character()
print("Welcome to the game", player1name) 
player1health = roll_health()
print ("HEALTH:", player1health)
player1strength = roll_attack_strength()
print ("STRENGTH:", player1strength)
print ("")
print ("Who are they battling?")
print ("")
player2name = roll_name()+ " the " + roll_character()
print("Welcome to the game", player2name) 
player2health = roll_health()
print ("HEALTH:", player2health)
player2strength = roll_attack_strength()
print ("STRENGTH:", player2strength)
print ("")

while True:
    time.sleep (5)
    os.system ("cls") 
    print ("⚔️ BATTLE TIME ⚔️")
    print ("")
    print ("The battle begins!")

    player1dice = rollDice (6)
    player2dice = rollDice (6)

    difference = abs(player1strength - player2strength) + 1

    if player1dice > player2dice:
        player2health -= difference
        if round == 1:
            print (player1name, "wins the first blow")
        else:
            print (player1name, "wins round", round)
    elif player2dice > player1dice:
        player1health -= difference
        if round == 1:
            print (player2name, "wins the first blow")
        else:
            print (player2name, "wins round", round)
    else:
        print ("Their swords clash and they draw round", round)
    print("")
    print (player1name)
    print ("HEALTH:", player1health)
    print ("STRENGTH:", player1strength)
    print("")
    print (player2name)
    print ("HEALTH:", player2health)
    print ("STRENGTH:", player2strength)
    print("")

    if player1health <= 0:
        print (player1name, "has died!")
        winner = player2name
        break
    elif player2health <= 0:
        print (player2name, "has died!")
        winner = player1name
        break
    else:
        print ("And they're both standing for the next round!")
        round += 1

time.sleep (5)
os.system ("cls")
print ("⚔️ BATTLE TIME ⚔️")
print ("")
print (winner, "has won in", round, "rounds!")    



    

   

   
