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
  os.system("cls") 
  print(f"{colorChange('white')}To Do List") 
  print()
  counter = 1 # add a counter
  for item in toDoList: # len counts how many items in a list
      print(f"{colorChange('purple')}{counter}: {item}")
      counter += 1
  time.sleep(1) 

while True:
  time.sleep (3)
  os.system ("cls") 
  menu = input(f"{colorChange('white')}To Do List Manager\n\n1. Add\n2: Remove\n3. Show\n4. Edit\n5. Delete\n")
  if menu == "1":
    item = input(f"What should I add to the to do list?:\n{colorChange('purple')}")
    if item in toDoList:
      print (f"{colorChange('purple')}{item}{colorChange('white')} is already on your list")
      time.sleep(1) 
    else:
      toDoList.append(item)
  elif menu == "2":
    item = input(f"What should I remove from the to do list?:\n{colorChange('green')}")
    if item in toDoList:
      remove = input(f"{colorChange('white')}Are you sure you want to remove {colorChange('green')}{item}{colorChange('white')} from the to do list?:\n")
      if remove == "yes":
        toDoList.remove(item)
      elif remove == "no":
        print (f"{colorChange('green')}{item}{colorChange('white')} was not removed from the to do list")
        time.sleep(1) 
    else:
      print(f"{item} was not in the to do list")
      time.sleep(1)
  elif menu == "4":
        item = input(f"{colorChange('white')}What item from the to do list would you like to edit?:\n{colorChange('red')}")
        new = input(f"{colorChange('white')}What do you want to change it to?:\n{colorChange('red')}")
        for i in range (0,len(toDoList)):
          if toDoList[i]==item:
            toDoList[i]=new
  elif menu == "5":
    delete = input(f"{colorChange('white')}Are you sure you want to {colorChange('blue')}DELETE {colorChange('white')} the entire list? \n")
    if delete == "yes":
      toDoList = []
    
  printList()
  