
day = 1

print ("30 Days Down - What did you think?")
print ("")


for i in range (1,31):
    print (f"Day{day}:")
    response = input("")
    print ("")
    myText =  f"You thought Day {day} was"
    print (f"{myText:^30}")
    print (f"{response:^30}")
    print ("")
    day += 1
