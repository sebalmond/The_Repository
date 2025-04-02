
def newPrint(color, word):
    if color=="red":
        print("\033[31m", word, sep="", end="")
    elif color == "magenta":
        print("\033[35m", word, sep="", end="")
    elif color == "cyan":
        print("\033[36m", word, sep="", end="")
    else:
        print("\033[0m", sep="", end="")

print ("Super Subroutine")
print ("")
print ("With my", end="")
newPrint("magenta"," new program ")
newPrint("reset", "")
print ("I can just call red('and')") 
newPrint("red", " and ")
newPrint("reset", "")
print ("that word will appear in the colour I set it to." )
print ("")
print ("With no", sep="", end="")
newPrint("cyan"," weird gaps ")
print ("")
newPrint("reset", "")
print ("Epic")
