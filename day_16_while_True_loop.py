print ("Fill-in the blank Lyrics!")
print ("(type in the blank lyrics, see if you're as cool as me")
print ("")

counter = 0
while True:
    print ("Finished with my woman, cos she couldn't help me with my ____!")
    answer = input("")
    counter += 1
    if answer == "mind":
        print ("Well Done! it only took you", counter, "attempts!")
        print ("")
        break
    else:
        print("Nope, try again.")
        print ("")   
print("Bye!")