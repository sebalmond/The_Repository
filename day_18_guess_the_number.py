print ("One-Million-To-One")
counter = 1
prize = 848618
guess = 0

while True: 
    guess = int(input("What is your guess?: "))
    if guess < 0:
        print ("Invalid guess - you're trying to cheat, I'm not playing!")
        exit ()
    elif guess > prize:
        print ("Too high")
        print ("")
        counter += 1
    elif guess < prize:
        print ("Too low")
        print ("")
        counter += 1
    elif guess == prize:
        print ("CORRECT! Well Done! You got it in ", counter, "tries!")
        break
    elif guess > 1000000:
        print ("Invalid guess - you're trying to cheat, I'm not playing!")
        exit()
