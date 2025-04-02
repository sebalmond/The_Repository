def newPrint(color, word):
    if color=="red":
        print("\033[31m", word, sep="", end="")
    elif color == "magenta":
        print("\033[35m", word, sep="", end="")
    elif color == "cyan":
        print("\033[36m", word, sep="", end="")
    elif color == "blue":
        print("\033[34m", word, sep="", end="")
    elif color == "yellow":
        print("\033[33m", word, sep="", end="")
    elif color == "green":
        print("\033[32m", word, sep="", end="")
    else:
        print("\033[0m", word, sep="", end="")

print (end= "\t \t")
newPrint ("red","=")
newPrint ("reset","=")
newPrint ("blue","=")
newPrint ("yellow", "Music App")
newPrint ("blue","=")
newPrint ("reset","=")
newPrint ("red","=")
print ("")
print("")
newPrint ("reset","🔥▶️\t Radio Gaga")
print("")
newPrint ("yellow", "\tQueen")
print("")
print("")
newPrint("reset","PREV")
print("")
newPrint("green","\tNEXT")
print("")
newPrint("magenta","\t\tPAUSE")
newPrint("reset","")
print("")
print("")
print("")

welcome = "WELCOME TO"
print (f"{welcome:^35}")
newPrint ("blue","")
armbook = "-- ARMBOOK --"
print(f"{armbook:^35}")
print("")
text = "Definitely not a rip off"
newPrint ("yellow","")
print (f"{text:>35}")
text = "of a certain other social"
newPrint ("yellow","")
print (f"{text:>35}")
text = "networking site."
newPrint ("yellow","")
print (f"{text:>35}")
print("")
newPrint ("red","")
honest = "Honest."
print (f"{honest:^35}")
print("")
newPrint("reset","")
username = "Username:"
password = "Password:"
print (f"{username:^35}")
print (f"{password:^35}")

#ANSWER def colorChange(color):
#  if color=="red":
#    return ("\033[31m")
#  elif color=="white":
#    return ("\033[0m")
#  elif color=="blue":
#    return ("\033[34m")
#  elif color=="yellow":
#    return ("\033[33m")
#  elif color == "green":
#    return ("\033[32m")
#  elif color == "purple":
#    return ("\033[35m")
#title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}= {colorChange('yellow')}Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}="
#print(f"        {title:^35}")
#print(f"🔥▶️\t{colorChange('white')}Radio Gaga")
#print(f"\t{colorChange('yellow')}Queen")
#prev = "prev"
#next = "next"
#pause = "pause"
#print(f"{colorChange('white')}{prev:<35}")
#print(f"{colorChange('green')}{next:^35}")
#print(f"{colorChange('purple')}{pause:>35}")
#print()
#print()
#text = "WELCOME TO"
#print(f"{colorChange('white')}{text:^35}")
#text = "--  ARMBOOK  --"
#print(f"{colorChange('blue')}{text:^35}")
#text = "Definitely not a rip off"
#print(f"{colorChange('yellow')}{text:>35}")
#text = "a certain other social"
#print(f"{colorChange('yellow')}{text:>35}")
#text = "networking site"
#print(f"{colorChange('yellow')}{text:>35}")
#text = "Honest."
#print(f"{colorChange('red')}{text:^35}")
#text = "Username: "
#username = input(f"{colorChange('white')}{text:^35}")
#text = "Password: "
#username = input(f"{colorChange('white')}{text:^35}")