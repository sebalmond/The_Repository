#comma
for i in range(0, 100):
  print(i, end=", ")

#new line
for i in range(0, 100):
  print(i, end="\n")

#tab indent
for i in range(0, 100):
  print(i, end="\t")

#vertical tab (cascading)
for i in range(0, 100):
  print(i, end="\v")

#change colour, no double spaces
print("If you put ", "\033[33m", "nothing as the ", "\033[35m", "end character ", "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="")

#no cursor
#import os, time
#print('\033[?25l', end="")
#for i in range(1, 101):
#  print(i)
#  time.sleep(0.2)
#  os.system("cls")

#print("\033[?25h", end="")