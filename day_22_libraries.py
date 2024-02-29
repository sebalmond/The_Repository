import random

print ("Totally Random One-Million-To-One")
print ("")

counter = 1
prize = random.randint(1, 1000000)
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
        print ("")
        go_again = input("Click 'run' to try again with a different number: ")
        print ("")
        if go_again == "run":
            counter = 1
            guess = 0
            prize = random.randint(1, 1000000)
        else:
            exit ()
    elif guess > 1000000:
        print ("Invalid guess - you're trying to cheat, I'm not playing!")
        exit()



