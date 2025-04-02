print ("KMA LOGIN SYSTEM")
print("")
myusername = "seb"
mypassword = "beardies4life"

def login():
    while True:
        yourusername = input("What is your name:")
        yourpassword = input("What is your password:")
        print ("")
        if yourusername == myusername and yourpassword == mypassword:
            print ("Welcome to KMA!")
            print ("")
            break
        else:
            print ("Whoops! I don't recognise that username or password, please try again")
            print ("")
login()
