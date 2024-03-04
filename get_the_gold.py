print("Welcome to Gold Rooms ! \nYour mission is to find gold.") 
choice1 = input("You're at a turning point, left or right? ").lower()

if choice1 == "right":
    choice2 = input("There's an open door in front of you, room is dark. You can't see anything there. Wait or go ? ").lower()
    if choice2 == "wait":
        choice3 = input("Which door would you step into ? Red, Blue or Yellow ? ")
        if choice3 == "red":
            print("You won ! ")
        else:
            print("You got attacked ! Game over!")
    else: 
        print("You got crushed! Game over!")
else:
    print("There was a demolition!! Game over !")