print ("Math Game:")
print ("")

multiples = int(input("Name your multiples:"))
print ("")

guess = 1
correct_answer = guess*multiples
score = 0
answer = 0

for i in range (10) :
    print (guess, "x", multiples, "=")
    answer = int (input(""))
    if answer == correct_answer:
        print ("Great work!😀")
        print ("")
        score += 1
        guess += 1
        correct_answer += multiples
    else:
        print ("Nope! 😥 The answer was ", correct_answer)
        print ("")
        guess += 1
        correct_answer += multiples
if score == 10:
    print ("Congratulations! 🥳🥳🥳 You scored", score, "out of 10! ")
print ("You scored ", score, "out of 10!")

