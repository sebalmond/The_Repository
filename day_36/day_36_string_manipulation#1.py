
#Create a new string using an fString that combines the tidied up version of the first name and tidied up version of the last name.
#Add those new versions to a list.
#Do not allow duplicates.
#Each time you add a new name, you should print out the full list.
#firstname = ""
#surname = ""

myList = []

def printList():
    print() #this is just to add an extra space between items
    for fullname in myList:
        print(fullname)
    print() #this is just to add an extra space between items

#Create a list of people's names. Ask for first and last name (surname) separately.
#Strip any extra spaces.
#Store names in a capitalized version.
while True:
    firstname = input("What's your firstname?: ").strip().upper()
    surname = input("What's your surname?: ").strip().upper()
    fullname = f"{firstname} {surname}"
    if fullname not in myList:
        myList.append(fullname)
    else:
        print (fullname, "was already in the list")
    printList()
