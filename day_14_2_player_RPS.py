from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()
player1Move = input("Player 1 > ")
print()
player2Move = input("Player 2 > ")
print()

if player1Move == "R" and player2Move == "R":   
    print("You both picked Rock, draw!")
elif player1Move == "R" and player2Move == "S":
    print("Player1 smashed Player2's Scissors into dust with their Rock!")
elif player1Move == "R" and player2Move == "P":
    print("Player1's Rock is smothered by Player2's Paper!")
elif player1Move == "P" and player2Move == "P":
    print("You both picked Paper, draw!")
elif player1Move == "P" and player2Move == "S":
    print("Player2's Scissors make confetti out of Player1's Paper!")
elif player1Move == "P" and player2Move == "R":
    print("Player2's Rock is smothered by Player1's Paper!")
elif player1Move == "S" and player2Move == "S":
    print("You both picked Scissors, draw!")
elif player1Move == "S" and player2Move == "P":
    print("Player1's Scissors make confetti out of Player2's Paper!")
elif player1Move == "S" and player2Move == "R":
    print("Player1's Scissors are smashed by Player2's Rock!")
else:
    print ("Invalid result, please try again!")