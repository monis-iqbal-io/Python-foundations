print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input('Where you want to go? "left" or "Right"?').lower()
if choice1 == "left":
    choice2 =input('There is an island,Do you want to "swim" or "wait"').lower()
    if choice2=="wait":
        choice3=input('which door you want to choose? "Blue" ,"Yellow" , "Red"').lower()
        if choice3=="yellow":
           print("you have found the treasure!\nYou won")
        elif choice3=="red":
           print("Burned by fire.\nGame Over")
        elif choice3=="blue":
           print("Eaten by beast.\n Game over")
        else:
           print("you didn't choose any option.\n Game over")
    else:
     print("attacked by trout.\n Game Over")
else:
 print("Fall into the Hole.\nGame Over")
