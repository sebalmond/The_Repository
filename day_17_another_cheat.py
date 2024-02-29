from getpass import getpass as input
round = 1
player1score = 0
player2score = 0
print(" M O R E   E P I C    🪨  📄 ✂️    B A T T L E ")

while round < 4:
    print()
    print("Round", round)
    print()
    print("Select your move (R, P or S)")
    print()
    player1Move = input("Player 1 > ")
    print()
    player2Move = input("Player 2 > ")
    print()

    if player1Move == "R" and player2Move == "R":   
        print("You both picked Rock, draw!")
        round += 1
    elif player1Move == "R" and player2Move == "S":
        print("Player1 smashed Player2's Scissors into dust with their Rock!")
        round += 1
        player1score +=1
    elif player1Move == "R" and player2Move == "P":
        print("Player1's Rock is smothered by Player2's Paper!")
        round += 1
        player2score +=1
    elif player1Move == "P" and player2Move == "P":
        print("You both picked Paper, draw!")
        round += 1
    elif player1Move == "P" and player2Move == "S":
        print("Player2's Scissors make confetti out of Player1's Paper!")
        round += 1
        player2score +=1
    elif player1Move == "P" and player2Move == "R":
        print("Player2's Rock is smothered by Player1's Paper!")
        round += 1
        player1score +=1
    elif player1Move == "S" and player2Move == "S":
        print("You both picked Scissors, draw!")
        round += 1
    elif player1Move == "S" and player2Move == "P":
        print("Player1's Scissors make confetti out of Player2's Paper!")
        round += 1
        player1score +=1
    elif player1Move == "S" and player2Move == "R":
        print("Player1's Scissors are smashed by Player2's Rock!")
        round += 1
        player2score +=1
    else:
        print ("Invalid result, please try again!")

if player1score > player2score:
    print ()
    print ("Player 1 wins with", player1score, "victories")
elif player1score < player2score:
    print ()
    print ("Player 2 wins with", player2score, "victories")
elif player1score == player2score:
    print ()
    print ("It's a draw! Let's play something else!")