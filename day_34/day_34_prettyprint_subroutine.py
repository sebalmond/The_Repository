import os, time
listOfEmail = []

def prettyPrint():
  os.system("cls") 
  print("listofEmail") 
  print()
  counter = 1 # add a counter
  for email in listOfEmail: # len counts how many items in a list
      print(f"{counter}: {email}")
      counter += 1
  time.sleep(1)

def spam (max):
  for i in range (0,max):
    print(f"Sending spam email to {listOfEmail[i]}...")
    print (f"""
    Email {i+1=})


    Dear {listOfEmail[i]},

    Congratulations! 🎉👽 You have been selected as the lucky winner of the Intergalactic Lottery, where the prizes are out of this world! Literally! 🌌

    You might be wondering, "How on Earth did I win a space lottery?" Well, let us assure you, your cosmic luck knows no bounds!

    As the chosen recipient, you are entitled to receive a grand prize package that includes:

    🚀 Your very own pet alien! (Disclaimer: May require interstellar travel for pickup)
    🌠 A year's supply of stardust (great for adding sparkle to your morning coffee!)
    🌌 A lifetime subscription to the Intergalactic News Network (stay updated on all the latest space gossip!)

    But wait, there's more! As a special bonus, we'll throw in a complimentary UFO joyride around the rings of Saturn! 🛸✨

    To claim your otherworldly prizes, simply click the button below and provide us with your Earthly details. Rest assured, your information will be kept safe and sound within our top-secret intergalactic database. 🛸🔒

    👽 Claim Your Prize Now! 👽

    Hurry! This cosmic offer won't last forever! And remember, in space, no one can hear you regret missing out on free stuff. 🌟🌌

    To infinity and beyond,

    Your Friendly Intergalactic Lottery Team 🚀🌠""")
    time.sleep(1)
    os.system("cls")

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  elif menu == "4":
    spam(10)
  time.sleep(1)
  os.system("cls")