firstname = input ("What is your first name?\n").strip().lower()
surname = input ("What is your surname?\n").strip().lower()
maidenname = input ("What is your mum's maiden name?\n").strip().lower()
birthplace = input ("Where were you born?\n").strip().lower()

starwarsname = f"{firstname[:3].capitalize()}{surname[:3]}"
starwarsname2 = f"{maidenname[:2].capitalize()}{birthplace[-3:]}"

print("Your Starwars name is\n",starwarsname,"",starwarsname2)

print ("What do you want to do ",starwarsname,"",starwarsname2, "?") 