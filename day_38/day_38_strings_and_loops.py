
#subroutine for colour change linked to each letter

def colorChange():
  if letter.lower() == "r":
    print('\033[31m', end='')
  elif letter.lower() == "b":
    print('\033[34m', end='')
  elif letter.lower() == "g":
    print('\033[32m', end='')
  elif letter.lower() == "p":
    print('\033[35m', end='')
  elif letter.lower() == "y":
    print('\033[33m', end='')
  elif letter == " ":
    print('\033[0m', end='')

#ask the user to input any sentence (string)
sentence = input("What sentence do you want rainbow-ising?\n")


#output the color changed string
#change the string into rainbow colours based on criteria

for letter in sentence:
  colorChange()
  print(letter, end="")
print()