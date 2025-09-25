# Dice roller game:
import random

# Here below we used while true to roll the dice or say run the code until user enter q to quit
while True:
    user = input("Enter 'yes' to roll a dice or 'no' or quit: ") # Here we are asking user to enter yes or no 
    if("yes" in user): # If yes then our dice will show the random number as the real dice
        dice = random.randint(1, 6)
        print(f"The number is: {dice}")
    elif("no" in user): # If no then the program will be ended
        print("The proram ended")
        break
    else: # If nothing is enterd then we will infrom user to enter something
        print("Please enter 'yes' or 'no'")