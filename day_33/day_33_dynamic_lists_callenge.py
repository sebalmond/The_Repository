import random, os, time

toDoList = []

def colorChange(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")

def printList():
  print() 
  for item in toDoList:
    print(item)
  print() 

while True:
  time.sleep (3)
  os.system ("cls") 
  menu = input(f"{colorChange('white')}To Do List Manager\n\nDo you want to view, add or edit your to do list?:\n")
  if menu == "add":
    item = input(f"What should I add to the to do list?:\n{colorChange('purple')}")
    toDoList.append(item)
  elif menu == "edit":
    item = input(f"What should I remove from the to do list?:\n{colorChange('green')}")
    if item in toDoList:
      toDoList.remove(item)
    else:
      print(f"{item} was not in the to do list")
  printList()
  