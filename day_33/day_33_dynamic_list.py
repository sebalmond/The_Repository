myAgenda = []

def printList():
    print() #this is just to add an extra space between items
    for item in myAgenda:
        print(item)
    print() #this is just to add an extra space between items

while True:
    menu = input("add or remove?: ")
    if menu == "add":
        item = input("What's next on the Agenda?: ")
        myAgenda.append(item)
    elif menu == "remove":
        item = input("What do you want to remove?: ")
        if item in myAgenda:
            myAgenda.remove(item)
        else:
            print (f"{item} was not in the list")
    printList()